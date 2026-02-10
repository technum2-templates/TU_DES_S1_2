#!/usr/bin/env python3
"""GitHub Classroom autograding wrapper (séance unique).

Objectif: exécuter les tests **par exercice** sans créer 12 templates.

✅ Convention de branche recommandée :
- `exo1`, `exo2`, ..., `exo12`

Sélection des tests (ordre de priorité) :
1) Variable d'env EXO (ex: EXO=3)
2) Nom de branche contenant `exoX`
3) Sinon : exécute tout

Ce wrapper :
- lance pytest en mode verbeux (logs visibles dans Actions)
- écrit un petit résumé dans le Job Summary (si disponible)
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional


SEANCE_DIR = Path("seance_unique")


def write_summary(md: str) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    try:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(md + "\n")
    except Exception:
        # Ne pas faire échouer la CI juste pour ça.
        pass


def parse_exo(value: str) -> Optional[int]:
    if not value:
        return None
    v = value.strip().lower()
    # accepte "3", "03", "exo3", "exo03"
    m = re.search(r"(?:^|\b)(?:exo)?\s*0*(\d{1,2})(?:\b|$)", v)
    if not m:
        return None
    n = int(m.group(1))
    return n if 1 <= n <= 12 else None


def parse_exo_from_branch(branch: str) -> Optional[int]:
    if not branch:
        return None
    b = branch.lower()
    m = re.search(r"(?:^|/|\b)exo\s*0*(\d{1,2})(?:\b|$)", b)
    if not m:
        return None
    n = int(m.group(1))
    return n if 1 <= n <= 12 else None


def main() -> int:
    branch = (os.getenv("BRANCH_NAME") or "").strip()
    exo = parse_exo(os.getenv("EXO") or "") or parse_exo_from_branch(branch)

    if not SEANCE_DIR.exists():
        msg = f"❌ Dossier introuvable: `{SEANCE_DIR}`"
        print(msg, file=sys.stderr)
        write_summary("## Autograding\n\n" + msg)
        return 2

    cmd = ["pytest", "-vv", "-rA", "--maxfail=1"]
    target_label = "tous les exercices"

    if exo is not None:
        # On suppose que les tests suivent la convention : test_exercice_<n>.py
        test_path = SEANCE_DIR / f"test_exercice_{exo}.py"
        if not test_path.exists():
            # fallback si tests rangés dans sous-dossier tests/
            alt = SEANCE_DIR / "tests" / f"test_exercice_{exo}.py"
            if alt.exists():
                test_path = alt
            else:
                msg = f"❌ Test introuvable pour exo {exo}: `{test_path}`"
                print(msg, file=sys.stderr)
                write_summary("## Autograding\n\n" + msg)
                return 2

        cmd.append(str(test_path))
        target_label = f"exo{exo} → `{test_path}`"
    else:
        cmd.append(str(SEANCE_DIR))

    print("Running:", " ".join(cmd))
    proc = subprocess.run(cmd, text=True)
    rc = proc.returncode

    status = "✅ Succès" if rc == 0 else f"❌ Échec (code {rc})"
    write_summary(
        "## Autograding\n\n"
        f"**Branche**: `{branch or 'n/a'}`\n\n"
        f"**Cible**: {target_label}\n\n"
        f"**Résultat**: {status}\n"
    )
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
