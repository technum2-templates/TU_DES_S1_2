#!/usr/bin/env python3
"""GitHub Actions test wrapper (S1+S2 only).

- Runs pytest with verbose output.
- Writes a short markdown summary to the GitHub Actions job summary (if available).
- If BRANCH_NAME contains 'seance_1' or 'seance_2', it will only run that folder.
  Otherwise it runs both seance_1 and seance_2.
"""

import os
import subprocess
import sys
from pathlib import Path


def write_summary(md: str) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    try:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(md + "\n")
    except Exception:
        # If summary writing fails, don't fail the whole job.
        pass


def main() -> int:
    branch = (os.getenv("BRANCH_NAME") or "").lower()

    targets = []
    if "seance_1" in branch or branch == "s1":
        targets = ["seance_1"]
    elif "seance_2" in branch or branch == "s2":
        targets = ["seance_2"]
    else:
        targets = ["seance_1", "seance_2"]

    # Ensure folders exist (avoid confusing errors)
    missing = [t for t in targets if not Path(t).exists()]
    if missing:
        msg = f"❌ Dossier(s) introuvable(s): {', '.join(missing)}"
        print(msg, file=sys.stderr)
        write_summary("## Autograding\n\n" + msg)
        return 2

    cmd = ["pytest", "-vv", "-rA", "--maxfail=1", *targets]
    print("Running:", " ".join(cmd))

    proc = subprocess.run(cmd, text=True)
    rc = proc.returncode

    status = "✅ Succès" if rc == 0 else f"❌ Échec (code {rc})"
    write_summary(f"## Autograding\n\n**Cible**: `{', '.join(targets)}`\n\n**Résultat**: {status}\n")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
