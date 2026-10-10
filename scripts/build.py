#!/usr/bin/env python3
"""Assembla, valida e impacchetta il plugin cima-scrittura.

Uso:
    python3 scripts/build.py           # build completa in dist/
    python3 scripts/build.py --check   # solo validazione, in una cartella temporanea

Passaggi:
1. copia plugin/ (senza condivisi/) in dist/cima-scrittura/
2. inietta nucleo/*.md in ogni skill, in references/nucleo/
3. inietta plugin/condivisi/<dominio>/ (anche sottocartelle, solo .md) in
   references/ di ogni skill del dominio (dominio = prefisso del nome)
4. valida manifest, frontmatter, nomi, riferimenti, caratteri vietati
5. crea dist/cima-scrittura.plugin (Cowork) e dist/skills/<nome>.zip (chat)
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NUCLEO = ROOT / "nucleo"
SRC = ROOT / "plugin"
CONDIVISI = SRC / "condivisi"
DIST = ROOT / "dist"
PROVE = ROOT / "prove"
PLUGIN_NAME = "cima-scrittura"

PREFISSI = ("generale-", "paper-", "proposte-", "progetti-")
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# Caratteri vietati nei testi del plugin: il modello imita gli esempi che legge.
VIETATI = {"—": "trattino em", "·": "punto medio"}
# File in cui compaiono solo per nominarli come vietati.
VIETATI_ESENTI = {"anti-pattern-ai.md"}
MAX_DESCRIZIONE = 1024
COLORI_AGENTE = {"blue", "cyan", "green", "yellow", "magenta", "red"}
MODELLI_AGENTE = {"inherit", "sonnet", "opus", "haiku"}
# Nomi di prodotto: la description e' cio' che legge l'utente, e gli ambienti
# sono esempi di una modalita', non la modalita' (CONTEXT.md).
PRODOTTI = ("Cowork", "Claude Code", "claude.ai")

errori: list[str] = []
avvisi: list[str] = []


def errore(msg: str) -> None:
    errori.append(msg)


def avviso(msg: str) -> None:
    avvisi.append(msg)


def frontmatter(path: Path) -> dict[str, str] | None:
    """Legge un frontmatter YAML semplice (chiavi di primo livello)."""
    testo = path.read_text(encoding="utf-8")
    if not testo.startswith("---\n"):
        return None
    fine = testo.find("\n---", 4)
    if fine == -1:
        return None
    blocco = testo[4:fine]
    campi: dict[str, str] = {}
    chiave = None
    for riga in blocco.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s?(.*)$", riga)
        if m:
            chiave = m.group(1)
            campi[chiave] = m.group(2).strip()
        elif chiave:
            campi[chiave] += "\n" + riga
    for k, v in campi.items():
        v = v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        campi[k] = v
    return campi


def valida_nucleo() -> None:
    if not NUCLEO.is_dir():
        errore("manca la cartella nucleo/")
        return
    for f in sorted(NUCLEO.glob("*.md")):
        if f.name in VIETATI_ESENTI:
            continue
        testo = f.read_text(encoding="utf-8")
        for c, nome in VIETATI.items():
            if c in testo:
                errore(f"{nome} in nucleo/{f.name}")


def valida_condivisi() -> None:
    if not CONDIVISI.is_dir():
        return
    domini = {p.rstrip("-") for p in PREFISSI}
    for d in sorted(CONDIVISI.iterdir()):
        if not d.is_dir():
            errore(f"condivisi/{d.name}: atteso solo cartelle di dominio")
        elif d.name not in domini:
            errore(f"condivisi/{d.name}: dominio sconosciuto (ammessi: {', '.join(sorted(domini))})")


def valida_manifest(base: Path) -> None:
    mf = base / ".claude-plugin" / "plugin.json"
    if not mf.is_file():
        errore("manca .claude-plugin/plugin.json")
        return
    try:
        dati = json.loads(mf.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errore(f"plugin.json non valido: {e}")
        return
    if dati.get("name") != PLUGIN_NAME:
        errore(f"plugin.json: name deve essere '{PLUGIN_NAME}'")
    versione = str(dati.get("version", ""))
    if not re.match(r"^\d+\.\d+\.\d+$", versione):
        errore("plugin.json: version deve essere semver (es. 0.1.0)")
    else:
        valida_prove(versione)


def valida_prove(versione: str) -> None:
    """Ogni versione ha la sua cartella di prove (prove/README.md)."""
    if not PROVE.is_dir():
        avviso("manca la cartella prove/")
        return
    if not any(d.is_dir() and d.name.startswith(versione) for d in PROVE.iterdir()):
        avviso(f"prove/: nessuna cartella per la versione {versione} (vedi prove/README.md)")
    prove_ignorate()


def prove_ignorate() -> None:
    """Un materiale di prova che git ignora non arriva a chi deve provare."""
    file = [p for p in PROVE.rglob("*") if p.is_file()]
    if not file:
        return
    try:
        esito = subprocess.run(
            ["git", "check-ignore", "--stdin"],
            input="\n".join(str(p) for p in file),
            capture_output=True, text=True, cwd=ROOT, timeout=30,
        )
    except (OSError, subprocess.SubprocessError):
        return  # senza git il controllo si salta, non fallisce
    for riga in esito.stdout.splitlines():
        if riga.strip():
            avviso(f"{riga.strip()}: ignorato da git, quindi non arriva a chi deve provare")


def nomi_agenti(base: Path) -> set[str]:
    cartella = base / "agents"
    return {p.stem for p in cartella.glob("*.md")} if cartella.is_dir() else set()


def valida_skill(skill_dir: Path, agenti: set[str] = frozenset()) -> None:
    nome = skill_dir.name
    rel = f"skills/{nome}"
    if not KEBAB.match(nome):
        errore(f"{rel}: nome non in kebab-case")
    if not nome.startswith(PREFISSI):
        errore(f"{rel}: il nome deve iniziare con {', '.join(PREFISSI)}")
    sk = skill_dir / "SKILL.md"
    if not sk.is_file():
        errore(f"{rel}: manca SKILL.md")
        return
    fm = frontmatter(sk)
    if fm is None:
        errore(f"{rel}/SKILL.md: frontmatter assente o malformato")
        return
    if fm.get("name") != nome:
        errore(f"{rel}/SKILL.md: name '{fm.get('name')}' diverso dalla cartella")
    desc = fm.get("description", "")
    if not desc:
        errore(f"{rel}/SKILL.md: description mancante")
    elif len(desc) > MAX_DESCRIZIONE:
        errore(f"{rel}/SKILL.md: description di {len(desc)} caratteri (max {MAX_DESCRIZIONE})")
    elif "Non usare" not in desc:
        avviso(f"{rel}/SKILL.md: description senza clausola 'Non usare per…' (vedi docs/instradamento.md)")
    if "<" in desc or ">" in desc:
        errore(f"{rel}/SKILL.md: description con parentesi angolari")
    for prodotto in PRODOTTI:
        if prodotto in desc:
            avviso(f"{rel}/SKILL.md: description nomina '{prodotto}'; usare 'modalita' agenti' o 'modalita' chat'")

    corpo = sk.read_text(encoding="utf-8")
    parole = len(corpo.split())
    if parole > 3000:
        avviso(f"{rel}/SKILL.md: {parole} parole (consigliato < 3000)")
    if "references/nucleo/vincoli.md" not in corpo:
        avviso(f"{rel}/SKILL.md: non richiama references/nucleo/vincoli.md")

    # Una skill che usa agenti deve funzionare anche in chat (docs/adr/0006).
    citati = sorted(a for a in agenti if re.search(rf"(?<![\w-]){re.escape(a)}(?![\w-])", corpo))
    for titolo in ("Modalità agenti", "Modalità chat"):
        if citati and not re.search(rf"^##\s+{titolo}\s*$", corpo, re.MULTILINE):
            errore(f"{rel}/SKILL.md: nomina {', '.join(citati)} ma manca la sezione '## {titolo}'")

    # Riferimenti a file references/ citati nel testo devono esistere.
    for ref in sorted(set(re.findall(r"references/[\w./-]+\.md", corpo))):
        if not (skill_dir / ref).is_file():
            errore(f"{rel}/SKILL.md: cita {ref} che non esiste")


def valida_agente(path: Path) -> None:
    nome = path.stem
    rel = f"agents/{path.name}"
    if not KEBAB.match(nome) or not nome.startswith(PREFISSI):
        errore(f"{rel}: nome non kebab-case o senza prefisso di dominio")
    fm = frontmatter(path)
    if fm is None:
        errore(f"{rel}: frontmatter assente o malformato")
        return
    if fm.get("name") != nome:
        errore(f"{rel}: name '{fm.get('name')}' diverso dal nome file")
    if "<example>" not in fm.get("description", ""):
        errore(f"{rel}: description senza blocchi <example>")
    if fm.get("model") not in MODELLI_AGENTE:
        errore(f"{rel}: model deve essere uno tra {sorted(MODELLI_AGENTE)}")
    if fm.get("color") not in COLORI_AGENTE:
        errore(f"{rel}: color deve essere uno tra {sorted(COLORI_AGENTE)}")


def controlla_caratteri_vietati(base: Path) -> None:
    for f in base.rglob("*.md"):
        if f.name in VIETATI_ESENTI:
            continue
        for n, riga in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            for c, nome in VIETATI.items():
                if c in riga:
                    errore(f"{f.relative_to(base)}:{n}: {nome}")


def assembla(dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    base_ignore = shutil.ignore_patterns(".DS_Store", ".gitkeep")

    def ignora(cartella: str, nomi: list[str]) -> set[str]:
        esclusi = set(base_ignore(cartella, nomi))
        if Path(cartella) == SRC:
            esclusi.add("condivisi")
        return esclusi

    shutil.copytree(SRC, dest, ignore=ignora)
    for skill_dir in sorted((dest / "skills").glob("*/")):
        target = skill_dir / "references" / "nucleo"
        if target.exists():
            errore(f"skills/{skill_dir.name}: il sorgente non deve contenere references/nucleo/")
            shutil.rmtree(target)
        target.mkdir(parents=True)
        for f in sorted(NUCLEO.glob("*.md")):
            shutil.copy2(f, target / f.name)

        dominio = skill_dir.name.split("-", 1)[0]
        cond = CONDIVISI / dominio
        if not cond.is_dir():
            continue
        refs = skill_dir / "references"
        for f in sorted(cond.rglob("*.md")):
            rel = f.relative_to(cond)
            if rel.parts[0] == "nucleo":
                errore(f"condivisi/{dominio}/nucleo/: nome riservato al nucleo")
                continue
            if (refs / rel).exists():
                errore(f"skills/{skill_dir.name}: references/{rel.as_posix()} è in condivisi/{dominio}/, togliere la copia dal sorgente")
            (refs / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, refs / rel)


def comprimi(cartella: Path, archivio: Path) -> None:
    archivio.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archivio, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(cartella.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(cartella))


def comprimi_skill(skill_dir: Path, archivio: Path) -> None:
    """Zip per caricamento in chat: la cartella della skill come radice."""
    archivio.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archivio, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill_dir.rglob("*")):
            if f.is_file():
                z.write(f, Path(skill_dir.name) / f.relative_to(skill_dir))


def main() -> int:
    solo_check = "--check" in sys.argv
    valida_nucleo()
    valida_condivisi()

    tmp = None
    lavoro = DIST / PLUGIN_NAME
    if solo_check:
        tmp = Path(tempfile.mkdtemp(prefix="cima-scrittura-check-"))
        lavoro = tmp / PLUGIN_NAME
    assembla(lavoro)

    valida_manifest(lavoro)
    skills = sorted(p for p in (lavoro / "skills").glob("*/") if p.is_dir())
    agenti = sorted((lavoro / "agents").glob("*.md")) if (lavoro / "agents").is_dir() else []
    if not skills:
        avviso("nessuna skill nel plugin (normale finché i domini non sono pronti)")
    nomi = nomi_agenti(lavoro)
    for s in skills:
        valida_skill(s, nomi)
    for a in agenti:
        valida_agente(a)
    controlla_caratteri_vietati(lavoro)

    for a in avvisi:
        print(f"AVVISO  {a}")
    for e in errori:
        print(f"ERRORE  {e}")

    if tmp is not None:
        shutil.rmtree(tmp, ignore_errors=True)
    if errori:
        print(f"\nBuild fallita: {len(errori)} errori, {len(avvisi)} avvisi.")
        return 1

    if not solo_check:
        comprimi(lavoro, DIST / f"{PLUGIN_NAME}.plugin")
        for s in skills:
            comprimi_skill(s, DIST / "skills" / f"{s.name}.zip")
        print(f"\nBuild riuscita: {len(skills)} skill, {len(agenti)} agenti, {len(avvisi)} avvisi.")
        print(f"  {DIST / (PLUGIN_NAME + '.plugin')}")
    else:
        print(f"\nValidazione riuscita: {len(skills)} skill, {len(agenti)} agenti, {len(avvisi)} avvisi.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
