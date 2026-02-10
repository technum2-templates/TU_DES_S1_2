"""
EXERCICE 3 : Fonction avec Exceptions

Contexte :
Vous devez tester une fonction qui lève des exceptions.

Tâche :
Écrivez des tests pour vérifier que les exceptions sont levées correctement.
"""

import unittest

def divide(a, b):
    """Divise a par b. Lève ValueError si b est zéro."""
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b

def parse_int(s):
    """Convertit une chaîne en entier. Lève ValueError si invalide."""
    try:
        return int(s)
    except ValueError:
        raise ValueError(f"Impossible de convertir '{s}' en entier")

class TestFonctionsExceptions(unittest.TestCase):
    """Tests pour les fonctions avec exceptions"""
    
    def test_divide_normal(self):
        """TODO: Tester une division normale"""
        pass
    
    def test_divide_by_zero(self):
        """TODO: Tester la division par zéro (doit lever ValueError)"""
        pass
    
    def test_parse_int_valide(self):
        """TODO: Tester avec une chaîne valide"""
        pass
    
    def test_parse_int_invalide(self):
        """TODO: Tester avec une chaîne invalide (doit lever ValueError)"""
        pass


if __name__ == "__main__":
    unittest.main()
