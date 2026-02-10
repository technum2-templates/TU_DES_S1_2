"""
EXERCICE 1 : Fonction Simple

Contexte :
Vous devez tester une fonction simple qui effectue une opération mathématique.

Tâche :
Écrivez des tests pour la fonction fournie.
"""

import unittest

def add(a, b):
    """Ajoute deux nombres et retourne le résultat."""
    return a + b

def subtract(a, b):
    """Soustrait b de a et retourne le résultat."""
  
    return a - b

class TestFonctionsSimples(unittest.TestCase):
    """Tests pour les fonctions simples"""
    
    def test_ajouter_positifs(self):
        """TODO: Tester l'addition de deux nombres positifs"""
        pass
    
    def test_ajouter_negatifs(self):
        """TODO: Tester l'addition avec des nombres négatifs"""
        pass
    
    def test_ajouter_zero(self):
        """TODO: Tester l'addition avec zéro"""
        pass
    
    def test_soustraire_negatifs(self):
        """TODO: Tester la multiplication de deux nombres positifs"""
        pass
    
    def test_soustraire_positifs(self):
        """TODO: Tester la multiplication par zéro"""
        pass
    
    def test_soustraire_zero(self):
        """TODO: Tester la multiplication avec des nombres négatifs"""
        pass


if __name__ == "__main__":
    unittest.main()
