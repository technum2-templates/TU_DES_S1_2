import os
import sys
import importlib.util

def check_imports():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, base_dir)
    
    sessions = ['seance_1', 'seance_2']
    issues = []
    
    for session in sessions:
        session_dir = os.path.join(base_dir, session)
        if not os.path.exists(session_dir):
            continue
            
        test_files = [f for f in os.listdir(session_dir) if f.startswith('test_exercice_')]
        for test_file in test_files:
            test_path = os.path.join(session_dir, test_file)
            # Lire le fichier de test pour voir ce qu'il essaie d'importer
            with open(test_path, 'r') as f:
                content = f.read()
                
            # Chercher les imports de type "from exercice_X import ..."
            import_lines = [line for line in content.split('\n') if 'from exercice_' in line and 'import' in line]
            for line in import_lines:
                try:
                    # Extraire le nom du module et les fonctions
                    parts = line.split('import')
                    module_part = parts[0].replace('from', '').strip()
                    functions_part = parts[1].strip()
                    functions = [f.strip() for f in functions_part.split(',')]
                    
                    # Tenter d'importer le module
                    module_path = os.path.join(session_dir, f"{module_part}.py")
                    if not os.path.exists(module_path):
                        issues.append(f"Fichier manquant: {module_path}")
                        continue
                        
                    spec = importlib.util.spec_from_file_location(module_part, module_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    for func in functions:
                        if not hasattr(module, func):
                            issues.append(f"Fonction '{func}' manquante dans {module_part}.py (demandée par {test_file})")
                except Exception as e:
                    issues.append(f"Erreur lors de l'analyse de {test_file}: {str(e)}")
                    
    return issues

if __name__ == "__main__":
    problems = check_imports()
    if problems:
        print("Problèmes détectés :")
        for p in problems:
            print(f"- {p}")
    else:
        print("Aucun problème d'importation majeur détecté entre les tests et les exercices.")
