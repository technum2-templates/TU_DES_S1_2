# 🎓 Exercices de Programmation Python - Séance Unique

Bienvenue dans ce dépôt d'exercices. L'objectif est de compléter une série de **12 exercices** couvrant les bases de Python et les tests unitaires.

## 📋 Structure du dépôt

- `seance_unique/` : Contient les 12 exercices (`exercice_X.py`) et leurs tests associés (`test_exercice_X.py`).
- `run_tests.sh` : Script pour vérifier votre travail localement.
- `check_exercises.py` : Utilitaire de vérification de structure.

## 🚀 Comment travailler ?

1. **Ouvrez un exercice** dans le dossier `seance_unique/` (ex: `exercice_1_fonction_simple.py`).
2. **Complétez le code** selon les instructions en commentaire.
3. **Vérifiez votre travail** en lançant le script de test :
   ```bash
   ./run_tests.sh
   ```
4. **Soumettez votre travail** en faisant un `git commit` et `git push`.

## 🛠 Liste des exercices

| N° | Thème |
| :--- | :--- |
| 1 | Fonctions simples |
| 2 | Conditions et logique |
| 3 | Gestion des exceptions |
| 4 | Manipulation de listes |
| 5 | Dictionnaires |
| 6 | Algorithmique complexe |
| 7 | Setup & Teardown (Unittest) |
| 8 | Fixtures (Pytest) |
| 9 | Paramétrage des tests |
| 10 | Couverture de code |
| 11 | TDD - Développement dirigé par les tests (Simple) |
| 12 | TDD - Développement dirigé par les tests (Complexe) |

---
*Note : Toutes les références aux anciennes séances S0, S1 et S2 ont été supprimées pour simplifier votre parcours.*

## Autograding par exercice (recommandé)

Pour éviter que GitHub Actions exécute des tests d'exercices que vous n'avez pas encore faits :

1) Créez une branche nommée **`exoX`** (exemples : `exo1`, `exo2`, ..., `exo12`)
2) Travaillez et *push* sur cette branche.

➡️ La CI détecte automatiquement `exoX` et n'exécute **que** le test correspondant.

Exemples :
- branche `exo3` → exécute `seance_unique/test_exercice_3.py`
- branche `exo11` → exécute `seance_unique/test_exercice_11.py`

Si vous restez sur `main`, la CI peut exécuter l'ensemble des tests.
