# Séance 2 : Tests Unitaires Avancés

---

## 🎯 Objectifs

Maîtriser les **techniques avancées** des tests :

- Setup et teardown
- Fixtures pytest
- Paramétrisation des tests
- Couverture de code
- Test-Driven Development (TDD)

---

## 📋 Exercices

| # | Exercice | Concepts Clés |
|---|----------|---------------|
| 1 | Setup/Teardown | Préparation, nettoyage |
| 2 | Fixtures | Réutilisabilité, isolation |
| 3 | Paramétrisation | Cas multiples, efficacité |
| 4 | Couverture Code | Mesure, amélioration |
| 5 | TDD Simple | Red-Green-Refactor |
| 6 | TDD Complexe | Conception par les tests |

---

## 🚀 Démarrage Rapide

### 1. Ouvrir un Exercice
```bash
cat exercice_1_setup_teardown.py
```

### 2. Écrire les Tests
Complétez les tests avec les techniques avancées.

### 3. Tester Localement
```bash
python3 -m pytest exercice_1_setup_teardown.py -v
```

### 4. Valider Tous les Exercices
```bash
python3 -m pytest seance_2/ -v
```

---

## 💡 Conseils Progressifs

### Exercice 1 : Setup/Teardown
- **Concept** : Préparation et nettoyage
- **À faire** : Initialiser les données avant, nettoyer après
- **Astuce** : Utilisez setUp() et tearDown()

### Exercice 2 : Fixtures
- **Concept** : Réutilisabilité des données
- **À faire** : Créer des fixtures pytest
- **Astuce** : Utilisez @pytest.fixture

### Exercice 3 : Paramétrisation
- **Concept** : Tester plusieurs cas
- **À faire** : Utiliser @pytest.mark.parametrize
- **Astuce** : Réduisez la duplication

### Exercice 4 : Couverture
- **Concept** : Mesurer la qualité
- **À faire** : Atteindre 90%+ de couverture
- **Astuce** : Utilisez pytest-cov

### Exercice 5 : TDD Simple
- **Concept** : Red-Green-Refactor
- **À faire** : Écrire le test d'abord
- **Astuce** : Le test échoue d'abord

### Exercice 6 : TDD Complexe
- **Concept** : Conception par les tests
- **À faire** : Concevoir en testant
- **Astuce** : Pensez à l'interface d'abord

---

## 🔍 Ressources Utiles

### Setup/Teardown
```python
def setUp(self):
    """Appelé avant chaque test"""
    self.data = []

def tearDown(self):
    """Appelé après chaque test"""
    self.data = None
```

### Fixtures pytest
```python
@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_something(sample_data):
    assert len(sample_data) == 3
```

### Paramétrisation
```python
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert double(input) == expected
```

---

## ✅ Checklist

Avant de terminer :

- [ ] Exercice 1 complété
- [ ] Exercice 2 complété
- [ ] Exercice 3 complété
- [ ] Exercice 4 complété
- [ ] Exercice 5 complété
- [ ] Exercice 6 complété
- [ ] Tous les tests passent
- [ ] Couverture > 90%

---

**Félicitations ! 🎉** Vous maîtrisez maintenant les tests unitaires !
