"""
EXERCICE 2 : Fonction avec Conditions

Contexte :
Vous devez tester une fonction qui contient des conditions.

Tâche :
Écrivez des tests pour couvrir tous les chemins (branches).
"""

import unittest

def is_even(n):
    """Retourne True si n est pair, False sinon."""
    return n % 2 == 0

def is_positive(n):
    """Retourne True si n est strictement positif, False sinon."""
    return n > 0

class TestFonctionsConditions(unittest.TestCase):
    """Tests pour les fonctions avec conditions"""
    
    def test_is_even_nombre_pair(self):
        """TODO: Tester avec un nombre pair"""
        pass
    
    def test_is_even_nombre_impair(self):
        """TODO: Tester avec un nombre impair"""
        pass
    
    def test_is_positive_positif(self):
        """TODO: Tester avec un nombre positif"""
        pass
    
    def test_is_positive_negatif(self):
        """TODO: Tester avec un nombre négatif"""
        pass


if __name__ == "__main__":
    unittest.main()
