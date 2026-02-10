#!/usr/bin/env python3
"""GitHub Actions test wrapper - Séance Unique (12 exercices).

- Exécute pytest sur tous les exercices.
- Génère un résumé Markdown pour GitHub Actions.
- Fournit des retours constructifs en cas d'échec.
"""

import os
import subprocess
import sys
from pathlib import Path

def write_summary(md: str) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        print("\n--- RÉSUMÉ DES TESTS ---\n")
        print(md)
        return
    try:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(md + "\n")
    except Exception:
        pass

def main() -> int:
    target = "seance_unique"
    
    if not Path(target).exists():
        msg = f"❌ Dossier '{target}' introuvable. Assurez-vous que la structure du dépôt est correcte."
        print(msg, file=sys.stderr)
        write_summary("## Autograding\n\n" + msg)
        return 2

    # Exécution de pytest
    # -vv: très verbeux
    # -rA: affiche le résumé de tous les tests (passés et échoués)
    # --tb=short: trace d'erreur courte pour plus de clarté
    cmd = ["pytest", "-vv", "-rA", "--tb=short", target]
    print(f"Exécution des tests dans: {target}")
    
    proc = subprocess.run(cmd, capture_output=True, text=True)
    rc = proc.returncode
    stdout = proc.stdout
    stderr = proc.stderr

    # Affichage de la sortie pour les logs GitHub
    print(stdout)
    if stderr:
        print(stderr, file=sys.stderr)

    # Construction du résumé
    status = "✅ Tous les exercices sont réussis !" if rc == 0 else "❌ Certains exercices nécessitent encore du travail."
    
    summary = [
        "## 🎓 Rapport d'Autograding",
        f"**Résultat global**: {status}",
        "\n### Détails des exercices\n",
        "| Exercice | Statut |",
        "| :--- | :--- |"
    ]

    # Analyse rapide des résultats pour le tableau
    for i in range(1, 13):
        if f"test_exercice_{i}.py" in stdout:
            # On cherche si le test spécifique a échoué
            # Pytest affiche "FAILED seance_unique/test_exercice_X.py"
            if f"FAILED seance_unique/test_exercice_{i}.py" in stdout:
                summary.append(f"| Exercice {i} | ❌ Échec |")
            else:
                summary.append(f"| Exercice {i} | ✅ Réussi |")
        else:
            summary.append(f"| Exercice {i} | ❓ Non exécuté |")

    if rc != 0:
        summary.append("\n### 💡 Conseils pour corriger")
        summary.append("1. Lisez attentivement le message d'erreur ci-dessus.")
        summary.append("2. Vérifiez que vos fonctions portent exactement le nom demandé.")
        summary.append("3. Assurez-vous de ne pas avoir modifié la structure des fichiers de test.")
        summary.append("4. Vous pouvez lancer les tests localement avec la commande `pytest`.")

    write_summary("\n".join(summary))
    return rc

if __name__ == "__main__":
    sys.exit(main())
