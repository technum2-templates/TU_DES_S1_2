# GitHub Classroom Unittest - Mise à jour

Ce projet a été mis à jour pour inclure un système de feedback progressif et une intégration GitHub Actions améliorée.

## 🚀 Nouveautés

1.  **`github_action_wrapper.py`** : Un wrapper Python qui exécute les tests et génère un rapport Markdown détaillé directement dans le résumé de votre exécution GitHub Action (`GITHUB_STEP_SUMMARY`).
2.  **`run_tests.sh`** : Un script shell pour exécuter les tests localement avec le même feedback progressif.
3.  **Workflow GitHub Actions optimisé** : Situé dans `.github/workflows/tests.yml`, il utilise désormais le wrapper pour un affichage clair des résultats.

## 💻 Utilisation Locale

Pour exécuter les tests localement avec feedback :

```bash
# Donner les permissions d'exécution
chmod +x run_tests.sh

# Exécuter tous les tests
./run_tests.sh

# Exécuter les tests d'une séance spécifique
./run_tests.sh seance_1

# Exécuter un exercice spécifique
./run_tests.sh seance_1 1
```

## 🤖 GitHub Actions

Le workflow se déclenche automatiquement à chaque `push`. Vous verrez un résumé détaillé dans l'onglet **Actions** de votre dépôt GitHub, incluant :
- Le nombre de tests réussis/échoués.
- Les messages d'erreur détaillés avec indices progressifs.
- Le rapport de couverture de code.

## ⚠️ Note sur les Imports

Assurez-vous que les noms des fonctions dans vos fichiers d'exercices (ex: `exercice_1_fonction_simple.py`) correspondent exactement à ceux attendus par les tests (ex: `add` et `subtract`). Actuellement, certains fichiers d'exercices utilisent des noms différents (ex: `ajouter` au lieu de `add`), ce qui causera l'échec des tests.

## Autograding par exercice (sans 12 templates)

Pour éviter que GitHub Actions vous parle d'exercices que vous n'avez pas encore faits, **travaillez sur une branche nommée** :

- `exo01`, `exo02`, ..., `exo12` (ou `exo-03`, `ex_7`, `exercice12`, etc.)

👉 La CI détecte automatiquement le numéro dans le nom de la branche et n'exécute **que** le test correspondant.

Exemples :
- branche `exo03` → exécute `seance_1/test_exercice_3.py`
- branche `exo11` → exécute `seance_2/test_exercice_5.py`

Si votre branche s'appelle `seance_1` ou `seance_2`, la CI exécute toute la séance (6 exercices).
Sinon, par défaut, elle exécute tout (S1+S2).
