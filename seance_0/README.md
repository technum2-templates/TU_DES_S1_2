# Séance 0 : Culture Générale des Tests

---

## 🎯 Objectifs

Dans cette séance, vous comprendrez les **fondamentaux des tests** et pourquoi ils sont essentiels :

- Pourquoi tester ?
- Types de tests (unitaires, intégration, E2E)
- Assertions et vérifications
- Couverture de code
- Bonnes pratiques

---

## 📋 Exercices

| # | Exercice | Concepts Clés |
|---|----------|---------------|
| 1 | Pourquoi Tester ? | Bénéfices, ROI, qualité |
| 2 | Types de Tests | Unitaires, intégration, E2E |
| 3 | Assertions | assert, vérifications |
| 4 | Couverture de Code | Mesure, objectifs |
| 5 | Bonnes Pratiques | AAA, noms, organisation |

---

## 🚀 Démarrage Rapide

### 1. Ouvrir un Exercice
```bash
cat exercice_1_pourquoi_tester.py
```

### 2. Répondre aux Questions
Chaque exercice pose des questions conceptuelles. Répondez-y en détail.

### 3. Valider votre Compréhension
```bash
python3 exercice_1_pourquoi_tester.py
```

### 4. Valider Tous les Exercices
```bash
python3 -m pytest -v
```

---

## 💡 Conseils Progressifs

### Exercice 1 : Pourquoi Tester ?
- **Concept** : Bénéfices et ROI des tests
- **Réfléchissez à** : Qualité, maintenance, confiance
- **Astuce** : Pensez aux bugs en production

### Exercice 2 : Types de Tests
- **Concept** : Différents niveaux de test
- **Réfléchissez à** : Unitaires vs intégration vs E2E
- **Astuce** : Chaque type a un objectif différent

### Exercice 3 : Assertions
- **Concept** : Vérifier les résultats
- **Réfléchissez à** : assertEqual, assertTrue, assertRaises
- **Astuce** : Une assertion = une vérification

### Exercice 4 : Couverture de Code
- **Concept** : Mesurer la qualité des tests
- **Réfléchissez à** : Pourcentage, branches, lignes
- **Astuce** : 100% n'est pas toujours nécessaire

### Exercice 5 : Bonnes Pratiques
- **Concept** : Écrire des tests de qualité
- **Réfléchissez à** : AAA, noms clairs, organisation
- **Astuce** : Un test = une idée

---

## 🔍 Ressources Utiles

### Pourquoi Tester ?
- Détecter les bugs tôt
- Faciliter la maintenance
- Documenter le comportement
- Augmenter la confiance
- Réduire les coûts

### Types de Tests
| Type | Scope | Vitesse | Coût |
|------|-------|---------|------|
| Unitaire | Fonction | Rapide | Bas |
| Intégration | Module | Moyen | Moyen |
| E2E | Système | Lent | Haut |

### Assertions Courantes
```python
self.assertEqual(a, b)      # a == b
self.assertTrue(x)          # x est True
self.assertRaises(exc, fn)  # fn() lève exc
self.assertIn(a, b)         # a in b
```

### Bonnes Pratiques (AAA)
1. **Arrange** : Préparer les données
2. **Act** : Exécuter le code
3. **Assert** : Vérifier les résultats

---

## 🧪 Tester votre Compréhension

### Localement
```bash
python3 exercice_1_pourquoi_tester.py
```

### Avec pytest
```bash
python3 -m pytest seance_0/ -v
```

### En Ligne
Réfléchissez à chaque question et écrivez vos réponses.

---

## 📚 Lectures Recommandées

1. **GUIDE_COMPLET_UNITTEST_BEGINNER.md** : Guide complet avec explications
2. **Documentation unittest** : https://docs.python.org/3/library/unittest.html
3. **Bonnes pratiques** : https://docs.pytest.org/

---

## ✅ Checklist

Avant de passer à Séance 1 :

- [ ] Exercice 1 complété et compris
- [ ] Exercice 2 complété et compris
- [ ] Exercice 3 complété et compris
- [ ] Exercice 4 complété et compris
- [ ] Exercice 5 complété et compris
- [ ] Vous comprenez les bénéfices des tests
- [ ] Vous connaissez les différents types de tests
- [ ] Vous pouvez écrire des assertions

---

**Bon courage ! 🚀** Comprendre la philosophie des tests est essentiel pour écrire de bons tests.
