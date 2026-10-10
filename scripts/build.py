#!/usr/bin/env python3
"""Assembla, valida e impacchetta il plugin cima-scrittura.

Uso:
    python3 scripts/build.py           # build completa in dist/
    python3 scripts/build.py --check   # solo validazione, nessun file scritto

Passaggi:
1. copia plugin/ in dist/cima-scrittura/
2. inietta nucleo/*.md in ogni skill, in references/nucleo/
3. valida manifest, frontmatter, nomi, riferimenti, trattino em
4. crea dist/cima-scrittura.plugin (Cowork) e dist/skills/<nome>.zip (chat)
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NUCLEO = ROOT / "nucleo"
SRC = ROOT / "plugin"
DIST = ROOT / "dist"
PLUGIN_NAME = "cima-scrittura"

PREFISSI = ("generale-", "paper-", "proposte-", "progetti-")
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
EM_DASH = "—"
# File in cui il trattino em compare solo per nominarlo come vietato.
EM_DASH_ESENTI = {"anti-pattern-ai.md"}
MAX_DESCRIZIONE = 1024
COLORI_AGENTE = {"blue", "cyan", "green", "yellow", "magenta", "red"}
MODELLI_AGENTE = {"inherit", "sonnet", "opus", "haiku"}

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
        if f.name not in EM_DASH_ESENTI and EM_DASH in f.read_text(encoding="utf-8"):
            errore(f"trattino em in nucleo/{f.name}")


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
    if not re.match(r"^\d+\.\d+\.\d+$", str(dati.get("version", ""))):
        errore("plugin.json: version deve essere semver (es. 0.1.0)")


def valida_skill(skill_dir: Path) -> None:
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
        avviso(f"{rel}/SKILL.md: description senza clausola 'Non usare per…' (vedi BRIEF §6)")
    if "<" in desc or ">" in desc:
        errore(f"{rel}/SKILL.md: description con parentesi angolari")

    corpo = sk.read_text(encoding="utf-8")
    parole = len(corpo.split())
    if parole > 3000:
        avviso(f"{rel}/SKILL.md: {parole} parole (consigliato < 3000)")
    if "references/nucleo/vincoli.md" not in corpo:
        avviso(f"{rel}/SKILL.md: non richiama references/nucleo/vincoli.md")

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


def controlla_em_dash(base: Path) -> None:
    for f in base.rglob("*.md"):
        if f.name in EM_DASH_ESENTI:
            continue
        for n, riga in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if EM_DASH in riga:
                errore(f"{f.relative_to(base)}:{n}: trattino em")


def assembla(dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(SRC, dest, ignore=shutil.ignore_patterns(".DS_Store", ".gitkeep", "README-dominio.md"))
    for skill_dir in sorted((dest / "skills").glob("*/")):
        target = skill_dir / "references" / "nucleo"
        if target.exists():
            errore(f"skills/{skill_dir.name}: il sorgente non deve contenere references/nucleo/")
            shutil.rmtree(target)
        target.mkdir(parents=True)
        for f in sorted(NUCLEO.glob("*.md")):
            shutil.copy2(f, target / f.name)


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

    lavoro = DIST / PLUGIN_NAME
    if solo_check:
        lavoro = DIST / ".check" / PLUGIN_NAME
    assembla(lavoro)

    valida_manifest(lavoro)
    skills = sorted(p for p in (lavoro / "skills").glob("*/") if p.is_dir())
    agenti = sorted((lavoro / "agents").glob("*.md")) if (lavoro / "agents").is_dir() else []
    if not skills:
        avviso("nessuna skill nel plugin (normale finché i domini non sono pronti)")
    for s in skills:
        valida_skill(s)
    for a in agenti:
        valida_agente(a)
    controlla_em_dash(lavoro)

    for a in avvisi:
        print(f"AVVISO  {a}")
    for e in errori:
        print(f"ERRORE  {e}")

    if solo_check:
        shutil.rmtree(DIST / ".check", ignore_errors=True)
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
