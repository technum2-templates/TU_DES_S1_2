# Instructions - Exercices Tests Unitaires Séances 0, 1 et 2

---

## 🎯 Objectif Global

Vous devez compléter les exercices des Séances 0, 1 et 2 en écrivant des tests unitaires appropriés. Chaque exercice teste votre compréhension des concepts clés des tests en Python.

---

## 🧩 Installation (local)

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📝 Format des Fichiers d'Exercice

Chaque fichier d'exercice suit ce format :

> ✅ Les exercices utilisent souvent le style `unittest.TestCase`.
> La correction automatique les exécute via `pytest`, qui sait détecter et lancer
> les tests écrits avec `unittest`.

```python
"""
EXERCICE N : [Titre de l'exercice]

Contexte : [Description du problème réel]

Tâche : [Ce que vous devez faire]

Fonctions à tester : [Les fonctions fournies]

Cas de test : [Les cas à couvrir]
"""

import unittest

class TestFonction(unittest.TestCase):
    """Tests pour la fonction"""
    
    def setUp(self):
        """Préparation avant chaque test"""
        pass
    
    def test_cas_1(self):
        """Test du cas 1"""
        # TODO: Complétez ce test
        pass
    
    def test_cas_2(self):
        """Test du cas 2"""
        # TODO: Complétez ce test
        pass


if __name__ == "__main__":
    unittest.main()
```

---

## 🔧 Comment Compléter un Exercice

### Étape 1 : Lire le Contexte
Comprenez le problème réel que vous testez. Cela vous aidera à écrire des tests pertinents.

### Étape 2 : Analyser la Fonction
Regardez la fonction à tester et identifiez :
- Les entrées possibles
- Les sorties attendues
- Les cas limites
- Les exceptions possibles

### Étape 3 : Écrire les Tests
Écrivez des tests qui couvrent :
- Le cas heureux (happy path)
- Les cas limites
- Les erreurs et exceptions
- Les conditions spéciales

### Étape 4 : Tester Localement
Exécutez les tests pour voir s'ils passent :
```bash
python3 exercice_1_*.py
```

### Étape 5 : Affiner et Déboguer
Si les tests échouent, revoyez votre logique de test.

### Étape 6 : Valider
Une fois satisfait, committez votre solution :
```bash
git add seance_0/exercice_1_*.py
git commit -m "Complétez exercice 1 Séance 0"
```

---

## 🧪 Exécuter les Tests

### Test d'un Exercice Spécifique
```bash
python3 seance_0/exercice_1_pourquoi_tester.py
```

### Test de Tous les Exercices d'une Séance
```bash
python3 -m pytest seance_0/ -v
```

### Test de Tous les Exercices
```bash
python3 -m pytest -v
```

### Avec Rapport de Couverture
```bash
python3 -m pytest --cov=. --cov-report=html
```

---

## 💡 Conseils de Débogage

### Utiliser des Assertions Explicites
```python
# ❌ Mauvais : peu informatif
self.assertTrue(result)

# ✅ Correct : explicite et informatif
self.assertEqual(result, 42, "La fonction devrait retourner 42")
```

### Tester les Cas Limites
```python
# ✅ Bon : tester les limites
def test_liste_vide(self):
    result = ma_fonction([])
    self.assertEqual(result, 0)

def test_liste_un_element(self):
    result = ma_fonction([1])
    self.assertEqual(result, 1)
```

### Tester les Exceptions
```python
# ✅ Bon : vérifier les exceptions
def test_division_par_zero(self):
    with self.assertRaises(ValueError):
        diviser(10, 0)
```

### Utiliser setUp et tearDown
```python
def setUp(self):
    """Appelé avant chaque test"""
    self.data = [1, 2, 3]

def tearDown(self):
    """Appelé après chaque test"""
    self.data = None
```

---

## 📊 Progression Recommandée

### Semaine 1 : Séance 0 (Culture Générale)
1. Lisez les 5 exercices
2. Répondez aux questions conceptuelles
3. Comprenez la philosophie des tests

### Semaine 2 : Séance 1 (Introduction)
1. Complétez les exercices 1-3 (fonctions simples)
2. Progressez avec les exercices 4-6 (collections)
3. Consultez les corrigés pour vérifier votre approche

### Semaine 3 : Séance 2 (Avancé)
1. Commencez par les exercices 1-2 (setup/teardown, fixtures)
2. Progressez avec les exercices 3-4 (paramétrisation, couverture)
3. Terminez avec les exercices 5-6 (TDD)

---

## 🚨 Erreurs Courantes à Éviter

### 1. Tester l'Implémentation au lieu du Comportement
```python
# ❌ Mauvais : teste l'implémentation
def test_implementation(self):
    result = ma_fonction(5)
    self.assertEqual(result, 5 * 2)  # Teste la formule, pas le résultat

# ✅ Correct : teste le comportement
def test_comportement(self):
    result = ma_fonction(5)
    self.assertEqual(result, 10)  # Teste le résultat attendu
```

### 2. Oublier les Cas Limites
```python
# ❌ Mauvais : ne teste que le cas heureux
def test_fonction(self):
    self.assertEqual(ma_fonction([1, 2, 3]), 6)

# ✅ Correct : teste les cas limites aussi
def test_liste_vide(self):
    self.assertEqual(ma_fonction([]), 0)

def test_nombres_negatifs(self):
    self.assertEqual(ma_fonction([-1, -2, -3]), -6)
```

### 3. Plusieurs Assertions par Test
```python
# ❌ Mauvais : plusieurs assertions
def test_fonction(self):
    result = ma_fonction(5)
    self.assertEqual(result, 10)
    self.assertGreater(result, 0)
    self.assertIsNotNone(result)

# ✅ Correct : une assertion par test
def test_fonction_retourne_10(self):
    self.assertEqual(ma_fonction(5), 10)

def test_fonction_retourne_positif(self):
    self.assertGreater(ma_fonction(5), 0)

def test_fonction_retourne_non_none(self):
    self.assertIsNotNone(ma_fonction(5))
```

### 4. Oublier le setUp/tearDown
```python
# ❌ Mauvais : duplication de code
def test_1(self):
    data = [1, 2, 3]
    # ...

def test_2(self):
    data = [1, 2, 3]
    # ...

# ✅ Correct : utiliser setUp
def setUp(self):
    self.data = [1, 2, 3]
```

---

## 📚 Ressources Utiles

### Assertions unittest
| Assertion | Utilisation |
|-----------|-------------|
| `assertEqual(a, b)` | a == b |
| `assertNotEqual(a, b)` | a != b |
| `assertTrue(x)` | x est True |
| `assertFalse(x)` | x est False |
| `assertIsNone(x)` | x est None |
| `assertIsNotNone(x)` | x n'est pas None |
| `assertIn(a, b)` | a in b |
| `assertNotIn(a, b)` | a not in b |
| `assertRaises(exc, func)` | func() lève exc |
| `assertGreater(a, b)` | a > b |
| `assertLess(a, b)` | a < b |

### Méthodes Utiles
```python
def setUp(self):
    """Appelé avant chaque test"""
    pass

def tearDown(self):
    """Appelé après chaque test"""
    pass

@classmethod
def setUpClass(cls):
    """Appelé une fois avant tous les tests de la classe"""
    pass

@classmethod
def tearDownClass(cls):
    """Appelé une fois après tous les tests de la classe"""
    pass
```

### Documentation
- **unittest** : https://docs.python.org/3/library/unittest.html
- **pytest** : https://docs.pytest.org/
- **Assertions** : https://docs.python.org/3/library/unittest.html#test-cases

---

## ✅ Checklist de Soumission

Avant de soumettre votre travail :

- [ ] Tous les exercices sont complétés
- [ ] Les tests passent localement (`pytest -v`)
- [ ] Votre code est bien formaté et commenté
- [ ] Vous avez committés vos changements
- [ ] Vous avez poussé votre branche
- [ ] Vous avez créé une Pull Request

---

## 🎓 Critères d'Évaluation

Votre travail sera évalué sur :

1. **Correctness (40%)** : Vos tests valident correctement le code
2. **Coverage (30%)** : Vous couvrez les cas principaux et limites
3. **Quality (20%)** : Vos tests sont clairs et bien organisés
4. **Best Practices (10%)** : Vous suivez les bonnes pratiques

---

## 🤔 FAQ

**Q: Dois-je tester toutes les fonctions ?**
A: Oui, chaque exercice fournit des fonctions à tester. Testez-les toutes.

**Q: Combien de tests par fonction ?**
A: Au minimum 3-5 : cas heureux, cas limites, erreurs.

**Q: Puis-je modifier les fonctions fournies ?**
A: Non, testez-les telles qu'elles sont. Votre travail est d'écrire les tests.

**Q: Que faire si je suis bloqué ?**
A: 
1. Relisez le contexte et les fonctions
2. Consultez les corrigés (mais essayez d'abord !)
3. Demandez à votre professeur

**Q: Dois-je compléter Séance 0 avant Séance 1 ?**
A: Oui, les concepts de Séance 0 sont fondamentaux pour les autres séances.

---

## 📞 Support

Pour toute question :
1. Consultez ce fichier INSTRUCTIONS.md
2. Lisez les commentaires dans les fichiers d'exercice
3. Consultez les corrigés détaillés
4. Contactez votre professeur

---

**Bonne chance ! 🚀**
