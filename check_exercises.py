import os
import sys
import importlib.util

def check_imports():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, base_dir)
    
    session_dir = os.path.join(base_dir, 'seance_unique')
    issues = []
    
    if not os.path.exists(session_dir):
        return ["Dossier 'seance_unique' manquant."]
            
    test_files = sorted([f for f in os.listdir(session_dir) if f.startswith('test_exercice_')], 
                       key=lambda x: int(x.split('_')[-1].split('.')[0]))
    
    for test_file in test_files:
        test_path = os.path.join(session_dir, test_file)
        with open(test_path, 'r') as f:
            content = f.read()
            
        import_lines = [line for line in content.split('\n') if 'from exercice_' in line and 'import' in line]
        for line in import_lines:
            try:
                parts = line.split('import')
                module_part = parts[0].replace('from', '').strip()
                functions_part = parts[1].strip()
                functions = [f.strip() for f in functions_part.split(',')]
                
                module_path = os.path.join(session_dir, f"{module_part}.py")
                if not os.path.exists(module_path):
                    issues.append(f"Fichier manquant: {module_part}.py (requis par {test_file})")
                    continue
                    
                spec = importlib.util.spec_from_file_location(module_part, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                for func in functions:
                    if not hasattr(module, func):
                        issues.append(f"Fonction '{func}' manquante dans {module_part}.py")
            except Exception as e:
                issues.append(f"Erreur dans {test_file}: {str(e)}")
                
    return issues

if __name__ == "__main__":
    problems = check_imports()
    if problems:
        print("❌ Problèmes détectés :")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    else:
        print("✅ Structure des exercices valide (12/12).")
        sys.exit(0)
