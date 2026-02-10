"""Tests optimisés pour exercice 2 - Conditions"""
import unittest
import sys
sys.path.insert(0, '..')
from test_utils import OptimizedTestCase

class TestExercice2(OptimizedTestCase):
    def setUp(self):
        try:
            from exercice_2_fonction_conditions import is_even, is_positive
            self.is_even = is_even
            self.is_positive = is_positive
        except ImportError as e:
            self.fail(f"❌ Impossible d'importer les fonctions: {e}")
    
    def test_is_even(self):
        test_cases = [(4, True), (5, False), (0, True), (-2, True)]
        print(f"\n{self.INFO} Test de is_even():")
        for num, expected in test_cases:
            result = self.is_even(num)
            if result == expected:
                print(f"  {self.PASS} is_even({num}) = {result}")
            else:
                self.fail(
                    f"{self.FAIL} is_even({num})\n"
                    f"  Obtenu: {result}, Attendu: {expected}\n"
                    f"{self.HINT} Indice: Utilisez num % 2 == 0"
                )
    
    def test_is_positive(self):
        test_cases = [(5, True), (-5, False), (0, False)]
        print(f"\n{self.INFO} Test de is_positive():")
        for num, expected in test_cases:
            result = self.is_positive(num)
            if result == expected:
                print(f"  {self.PASS} is_positive({num}) = {result}")
            else:
                self.fail(f"{self.FAIL} is_positive({num}) = {result}, attendu {expected}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
