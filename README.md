# Exercices Tests Unitaires - Séances 0, 1 et 2

Bienvenue dans ce dépôt d'exercices sur les **tests unitaires procéduraux** en Python ! Ce dépôt contient des exercices progressifs pour maîtriser les tests unitaires, du niveau débutant au niveau intermédiaire.

---

## 📚 Structure du Dépôt

```
.
├── README.md                          # Ce fichier
├── INSTRUCTIONS.md                    # Instructions générales
├── .github/
│   └── workflows/                     # Tests automatisés (CI/CD)
├── seance_0/                          # Culture Générale des Tests
│   ├── README.md
│   ├── exercice_1_pourquoi_tester.py
│   ├── exercice_2_types_tests.py
│   ├── exercice_3_assertions.py
│   ├── exercice_4_couverture.py
│   └── exercice_5_bonnes_pratiques.py
├── seance_1/                          # Introduction Tests Unitaires
│   ├── README.md
│   ├── exercice_1_fonction_simple.py
│   ├── exercice_2_fonction_conditions.py
│   ├── exercice_3_fonction_exceptions.py
│   ├── exercice_4_fonction_listes.py
│   ├── exercice_5_fonction_dictionnaires.py
│   └── exercice_6_fonction_complexe.py
└── seance_2/                          # Tests Unitaires Avancés
    ├── README.md
    ├── exercice_1_setup_teardown.py
    ├── exercice_2_fixtures.py
    ├── exercice_3_parametrize.py
    ├── exercice_4_couverture_code.py
    ├── exercice_5_tdd_simple.py
    └── exercice_6_tdd_complexe.py
```

---

## 🎯 Objectifs

### Séance 0 : Culture Générale des Tests
Comprendre les fondamentaux des tests et pourquoi ils sont essentiels :
- Pourquoi tester ?
- Types de tests (unitaires, intégration, etc.)
- Assertions et vérifications
- Couverture de code
- Bonnes pratiques

### Séance 1 : Introduction aux Tests Unitaires
Apprendre à écrire des tests unitaires simples en Python :
- Structure d'un test unitaire
- Assertions de base
- Tests de fonctions simples
- Gestion des exceptions
- Tests avec collections

### Séance 2 : Tests Unitaires Avancés
Maîtriser les techniques avancées des tests :
- Setup et teardown
- Fixtures pytest
- Paramétrisation des tests
- Couverture de code
- Test-Driven Development (TDD)

---

## 🚀 Comment Utiliser ce Dépôt

### 1. Cloner le Dépôt
```bash
git clone <url-du-depot>
cd github_classroom_unittest
```

### 2. Naviguer vers une Séance
```bash
cd seance_0  # ou seance_1, seance_2
```

### 3. Résoudre les Exercices
Chaque fichier d'exercice contient :
- Une description du problème
- Des fonctions à tester
- Des tests à compléter
- Des assertions à écrire

### 4. Tester votre Code
```bash
python3 -m pytest seance_0/ -v
```

> 🔎 **Note (important)**
>
> - Plusieurs exercices utilisent le style **`unittest.TestCase`** (pour apprendre les bases).
> - La correction automatique (GitHub Classroom / CI) exécute tout via **`pytest`**.
>   `pytest` sait découvrir et lancer les tests écrits avec `unittest`, ce qui permet
>   d'évoluer progressivement vers les fonctionnalités avancées de `pytest` (fixtures, parametrize, etc.).

### 5. Valider avec les Tests
```bash
python3 -m pytest -v
```

---

## 📋 Exercices Séance 0 (Culture Générale)

| # | Exercice | Concepts Clés |
|---|----------|---------------|
| 1 | Pourquoi Tester ? | Bénéfices, ROI, qualité |
| 2 | Types de Tests | Unitaires, intégration, E2E |
| 3 | Assertions | assert, vérifications |
| 4 | Couverture de Code | Mesure, objectifs |
| 5 | Bonnes Pratiques | AAA, noms, organisation |

---

## 📋 Exercices Séance 1 (Introduction)

| # | Exercice | Concepts Clés |
|---|----------|---------------|
| 1 | Fonction Simple | Structure de base |
| 2 | Conditions | Branches, cas limites |
| 3 | Exceptions | Gestion d'erreurs |
| 4 | Listes | Collections, itération |
| 5 | Dictionnaires | Clés, valeurs, accès |
| 6 | Fonction Complexe | Intégration multiple |

---

## 📋 Exercices Séance 2 (Avancé)

| # | Exercice | Concepts Clés |
|---|----------|---------------|
| 1 | Setup/Teardown | Préparation, nettoyage |
| 2 | Fixtures | Réutilisabilité, isolation |
| 3 | Paramétrisation | Cas multiples, efficacité |
| 4 | Couverture Code | Mesure, amélioration |
| 5 | TDD Simple | Red-Green-Refactor |
| 6 | TDD Complexe | Conception par les tests |

---

## 💡 Conseils pour Réussir

1. **Commencez par Séance 0** : Comprenez la philosophie avant la pratique.

2. **Progressez graduellement** : Séance 1 avant Séance 2.

3. **Écrivez des tests clairs** : Noms explicites, une assertion par test.

4. **Testez les cas limites** : Pas seulement le cas heureux.

5. **Utilisez AAA** : Arrange, Act, Assert.

6. **Consultez les corrigés** : Pour comprendre les approches.

---

## 📚 Ressources Supplémentaires

- **Documentation unittest** : https://docs.python.org/3/library/unittest.html
- **Documentation pytest** : https://docs.pytest.org/
- **Guide Complet Tests Unitaires** : Voir `GUIDE_COMPLET_UNITTEST_BEGINNER.md`
- **Guide Avancé Tests** : Voir `GUIDE_AVANCE_TESTS_UNITAIRES.md`
- **Corrigés Détaillés** : Voir `CORRIGES_UNITTEST_SEANCES_*.md`

---

## 🧪 Tests Automatisés

Ce dépôt inclut des tests automatisés qui s'exécutent à chaque commit. Vous pouvez voir l'état des tests dans l'onglet "Actions" de GitHub.

Pour exécuter les tests localement :
```bash
python3 -m pytest -v
```

---

## 📝 Soumettre votre Travail

1. Créez une branche pour votre travail :
   ```bash
   git checkout -b solution/seance-0
   ```

2. Complétez les exercices et committez :
   ```bash
   git add .
   git commit -m "Complétez les exercices Séance 0"
   ```

3. Poussez votre branche :
   ```bash
   git push origin solution/seance-0
   ```

4. Créez une Pull Request sur GitHub

---

## ✅ Critères d'Évaluation

- **Fonctionnalité** : Vos tests valident correctement le code
- **Couverture** : Vous testez les cas principaux et limites
- **Qualité** : Vos tests sont clairs et bien organisés
- **Tests Passants** : Tous les tests automatisés passent
- **Documentation** : Vos tests sont commentés et explicites

---

## 🤝 Contribution

Si vous trouvez une erreur ou avez une suggestion :
1. Ouvrez une issue
2. Proposez une pull request
3. Contactez votre professeur

---

## 📞 Support

Pour toute question ou problème :
- Consultez les fichiers README dans chaque dossier de séance
- Lisez les corrigés détaillés
- Demandez à votre professeur

---

**Bon courage ! 🚀** Maîtriser les tests unitaires est une compétence essentielle en programmation.
