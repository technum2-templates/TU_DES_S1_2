#!/usr/bin/env python3
"""GitHub Actions test wrapper — Séance unique (12 exercices) via S1+S2.

Objectif: permettre un autograding **par exercice** sans multiplier les templates.

Sélection des tests (ordre de priorité):
1) Variable d'env EXO (ex: EXO=03 ou EXO=11)
2) Nom de branche contenant un numéro d'exercice (ex: exo03, exo-11, ex_7, exercice12)
3) Nom de branche contenant seance_1 / seance_2 (-> exécute la séance entière)
4) Sinon: exécute tout (S1 + S2)

Mapping:
- EXO 01..06  -> seance_1 (test_exercice_1..6.py)
- EXO 07..12  -> seance_2 (test_exercice_1..6.py)

Le wrapper:
- lance pytest en mode verbeux (logs visibles dans Actions)
- écrit un petit résumé dans le Job Summary (si disponible)
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional, Tuple


def write_summary(md: str) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    try:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(md + "\n")
    except Exception:
        pass


def parse_exo_from_text(text: str) -> Optional[int]:
    """Extrait un numéro d'exercice (1..12) depuis un texte (branche, etc.)."""
    if not text:
        return None
    t = text.lower()
    m = re.search(r"(?:exo|exercice|ex)[-_\s]*0*(\d{1,2})\b", t)
    if not m:
        return None
    n = int(m.group(1))
    return n if 1 <= n <= 12 else None


def map_exo_to_test(exo: int) -> Tuple[str, str]:
    """Retourne (dossier, fichier_test) pour un exercice 1..12."""
    if 1 <= exo <= 6:
        return ("seance_1", f"test_exercice_{exo}.py")
    # 7..12 -> seance_2, test_exercice_(exo-6).py
    return ("seance_2", f"test_exercice_{exo - 6}.py")


def main() -> int:
    branch = (os.getenv("BRANCH_NAME") or "").strip()
    exo_env = (os.getenv("EXO") or "").strip()

    exo = parse_exo_from_text(exo_env) or parse_exo_from_text(branch)

    cmd = ["pytest", "-vv", "-rA", "--maxfail=1"]
    target_label = "tout (S1+S2)"

    if exo is not None:
        folder, test_file = map_exo_to_test(exo)
        test_path = Path(folder) / test_file
        if not test_path.exists():
            msg = f"❌ Test introuvable pour EXO {exo:02d}: `{test_path}`"
            print(msg, file=sys.stderr)
            write_summary("## Autograding\n\n" + msg)
            return 2
        cmd.append(str(test_path))
        target_label = f"EXO {exo:02d} → `{test_path}`"
    else:
        b = branch.lower()
        if "seance_1" in b or b == "s1" or "seance1" in b:
            cmd.append("seance_1")
            target_label = "`seance_1` (6 exercices)"
        elif "seance_2" in b or b == "s2" or "seance2" in b:
            cmd.append("seance_2")
            target_label = "`seance_2` (6 exercices)"

    # sanity check for folders if we run them
    for maybe in ["seance_1", "seance_2"]:
        if maybe in cmd and not Path(maybe).exists():
            msg = f"❌ Dossier introuvable: `{maybe}`"
            print(msg, file=sys.stderr)
            write_summary("## Autograding\n\n" + msg)
            return 2

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
