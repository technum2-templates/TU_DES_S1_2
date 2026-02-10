import os
import subprocess
import json
import sys

def run_command(command):
    """Exécute une commande shell et retourne la sortie."""
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        text=True,
        env=os.environ.copy()
    )
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr

def generate_markdown_report(pytest_report_path):
    """Génère un rapport Markdown à partir du rapport JSON de pytest."""
    if not os.path.exists(pytest_report_path):
        return "### ❌ Erreur: Rapport de test non généré."
    
    with open(pytest_report_path, 'r') as f:
        data = json.load(f)
    
    summary = data.get('summary', {})
    total = summary.get('total', 0)
    passed = summary.get('passed', 0)
    failed = summary.get('failed', 0)
    skipped = summary.get('skipped', 0)
    duration = data.get('duration', 0)
    
    report = f"## 📊 Résumé des Tests\n\n"
    report += f"- **Total**: {total}\n"
    report += f"- **Réussis**: ✅ {passed}\n"
    report += f"- **Échecs**: ❌ {failed}\n"
    report += f"- **Ignorés**: ⏭️ {skipped}\n"
    report += f"- **Durée**: {duration:.2f}s\n\n"
    
    if failed > 0:
        report += "### 🔍 Détails des Échecs\n\n"
        for test in data.get('tests', []):
            if test.get('outcome') == 'failed':
                nodeid = test.get('nodeid')
                call = test.get('call', {})
                longrepr = call.get('longrepr', 'Aucun détail disponible.')
                report += f"<details>\n<summary>❌ {nodeid}</summary>\n\n```python\n{longrepr}\n```\n</details>\n\n"
    
    return report

def main():
    print("🚀 Démarrage du wrapper GitHub Action...")
    
    # 1. Configurer l'environnement
    os.environ['PYTHONPATH'] = os.environ.get('PYTHONPATH', '') + ":" + os.getcwd()
    
    # 2. Exécuter les tests avec pytest-json-report + couverture (un seul run)
    print("🧪 Exécution des tests...")
    rc, stdout, stderr = run_command(
        "python3 -m pytest -vv -rA "
        "--json-report --json-report-file=report.json "
        "--tb=short "
        "--cov=. --cov-report=term-missing"
    )
    
    # 3. Générer le rapport Markdown
    markdown_report = generate_markdown_report("report.json")
    
    # 4. Écrire dans le résumé de l'action GitHub si disponible
    github_step_summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if github_step_summary:
        with open(github_step_summary, 'a') as f:
            f.write(markdown_report)
            # Ajouter aussi la sortie de couverture (et tout stdout) pour un feedback complet
            if stdout.strip():
                f.write("\n\n---\n\n## 🧾 Sortie pytest / couverture\n\n")
                f.write("```text\n")
                f.write(stdout)
                f.write("\n```\n")
            if stderr.strip():
                f.write("\n\n## ⚠️ Erreurs / stderr\n\n")
                f.write("```text\n")
                f.write(stderr)
                f.write("\n```\n")
        print("📝 Rapport Markdown ajouté au résumé GitHub Action.")
        # Afficher aussi la sortie dans les logs Actions (utile pour debug)
        if stdout.strip():
            print("\n--- SORTIE PYTEST / COUVERTURE ---\n")
            print(stdout)
        if stderr.strip():
            print("\n--- STDERR ---\n")
            print(stderr, file=sys.stderr)

    else:
        print("\n--- RAPPORT DE TEST ---\n")
        print(markdown_report)
        if stdout.strip():
            print("\n--- SORTIE PYTEST / COUVERTURE ---\n")
            print(stdout)
        if stderr.strip():
            print("\n--- STDERR ---\n")
            print(stderr)
    
    # 5. Sortir avec le code de retour approprié
    sys.exit(rc)

if __name__ == "__main__":
    main()
