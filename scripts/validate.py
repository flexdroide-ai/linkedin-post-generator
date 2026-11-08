"""
validate.py — Valida la cartella skill prima del build.

Controlla:
  - SKILL.md esiste alla radice della cartella skill
  - il frontmatter YAML ha 'name' e 'description'
  - 'name' rispetta le regole (lowercase/numeri/trattini, <=64 chars,
    == nome cartella, no parola riservata 'claude', no trattini consecutivi,
    no inizio/fine con trattino)
  - 'description' <= 200 caratteri (limite Claude.ai; agentskills.io consente 1024)
  - nessun file __MACOSX, .DS_Store o ._* nella cartella skill
  - i file referenziati con backtick in SKILL.md esistono

Uso:
    python3 scripts/validate.py

Exit code: 0 se tutto OK, 1 se ci sono errori.
"""

import sys
import os
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_FOLDER_NAME = "linkedin-post-generator"
SKILL_DIR = os.path.join(REPO_ROOT, SKILL_FOLDER_NAME)
MAX_DESCRIPTION_LEN = 200   # Claude.ai constraint (agentskills.io allows up to 1024)
MAX_NAME_LEN = 64


def parse_frontmatter(path):
    """Parse YAML frontmatter (simple key:value pairs). Returns (dict, error_msg)."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return None, "il file deve iniziare con --- (frontmatter YAML mancante)"
    end = content.find("\n---", 3)
    if end == -1:
        return None, "frontmatter non chiuso (manca --- di chiusura)"
    result = {}
    for line in content[3:end].strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            result[key.strip()] = val.strip()
    return result, None


def validate_name(name, folder_name):
    errors = []
    if not name:
        errors.append("campo 'name' mancante o vuoto")
        return errors
    if len(name) > MAX_NAME_LEN:
        errors.append(f"'name' supera {MAX_NAME_LEN} caratteri ({len(name)})")
    if not re.match(r'^[a-z0-9]([a-z0-9-]*[a-z0-9])?$', name) and len(name) != 1:
        errors.append(
            "'name' non valido: solo minuscole (a-z), numeri (0-9) e trattini; "
            "non può iniziare o finire con trattino"
        )
    elif len(name) == 1 and not re.match(r'^[a-z0-9]$', name):
        errors.append("'name' non valido: deve essere un carattere alfanumerico minuscolo")
    if "--" in name:
        errors.append("'name' contiene trattini consecutivi ('--') — non consentiti")
    if "claude" in name:
        errors.append("'name' contiene la parola riservata 'claude'")
    if name != folder_name:
        errors.append(
            f"'name' ({name!r}) non coincide col nome della cartella ({folder_name!r})"
        )
    return errors


def find_garbage(skill_dir):
    """Return list of __MACOSX dirs, .DS_Store and ._* files found inside skill_dir."""
    bad = []
    for root, dirs, files in os.walk(skill_dir):
        if "__MACOSX" in dirs:
            bad.append(os.path.join(root, "__MACOSX"))
        for f in files:
            if f == ".DS_Store" or f.startswith("._"):
                bad.append(os.path.join(root, f))
    return bad


def find_missing_references(skill_md_path, skill_dir):
    """Find backtick-wrapped .md paths in SKILL.md that don't exist on disk."""
    with open(skill_md_path, "r", encoding="utf-8") as f:
        content = f.read()
    missing = []
    for path in re.findall(r'`([^`\n]+\.md)`', content):
        if path.startswith("http"):
            continue
        if not os.path.exists(os.path.join(skill_dir, path)):
            missing.append(path)
    return missing


def main():
    errors = []
    print(f"Validazione: {SKILL_DIR}\n")

    if not os.path.isdir(SKILL_DIR):
        print(f"ERRORE CRITICO: cartella '{SKILL_FOLDER_NAME}/' non trovata.")
        sys.exit(1)

    skill_md = os.path.join(SKILL_DIR, "SKILL.md")
    if not os.path.isfile(skill_md):
        errors.append("SKILL.md mancante alla radice della cartella skill")
    else:
        fm, err = parse_frontmatter(skill_md)
        if err:
            errors.append(f"SKILL.md: {err}")
        else:
            errors.extend(validate_name(fm.get("name", ""), SKILL_FOLDER_NAME))

            desc = fm.get("description", "")
            if not desc:
                errors.append("frontmatter: 'description' mancante o vuoto")
            elif len(desc) > MAX_DESCRIPTION_LEN:
                errors.append(
                    f"frontmatter: 'description' supera {MAX_DESCRIPTION_LEN} caratteri "
                    f"({len(desc)}) — limite Claude.ai"
                )

        for m in find_missing_references(skill_md, SKILL_DIR):
            errors.append(f"file referenziato in SKILL.md non trovato: {m}")

    for g in find_garbage(SKILL_DIR):
        errors.append(f"file da escludere dallo zip: {g}")

    if errors:
        print("ERRORI:")
        for e in errors:
            print(f"  ✗ {e}")
        print(f"\n{len(errors)} errore/i trovato/i. Correggili prima di 'make build'.")
        sys.exit(1)

    print("OK — nessun errore. Pronto per 'make build'.")
    sys.exit(0)


if __name__ == "__main__":
    main()
