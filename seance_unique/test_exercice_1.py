"""Tests optimisés pour exercice 1 - Fonction Simple"""
import unittest
import sys
sys.path.insert(0, '..')
from test_utils import OptimizedTestCase, TestReporter

class TestExercice1(OptimizedTestCase):
    def setUp(self):
        try:
            from exercice_1_fonction_simple import add, subtract
            self.add = add
            self.subtract = subtract
        except ImportError as e:
            self.fail(f"❌ Impossible d'importer les fonctions: {e}")
    
    def test_add_function_exists(self):
        self.assertTrue(callable(self.add), f"{self.FAIL} 'add' doit être une fonction")
    
    def test_add_positive_numbers(self):
        test_cases = [(2, 3, 5), (10, 20, 30), (0, 5, 5)]
        print(f"\n{self.INFO} Test de la fonction add():")
        for a, b, expected in test_cases:
            result = self.add(a, b)
            if result == expected:
                print(f"  {self.PASS} add({a}, {b}) = {result}")
            else:
                error_msg = (
                    f"\n{self.FAIL} Résultat incorrect\n"
                    f"  add({a}, {b})\n"
                    f"  Résultat obtenu: {result}\n"
                    f"  Résultat attendu: {expected}\n"
                    f"{self.HINT} Indice: Vérifiez la logique de votre fonction add"
                )
                self.fail(error_msg)
    
    def test_subtract_function_exists(self):
        self.assertTrue(callable(self.subtract))
    
    def test_subtract_positive_numbers(self):
        result = self.subtract(10, 3)
        expected = 7
        if result == expected:
            print(f"{self.PASS} subtract(10, 3) = {result}")
        else:
            self.fail(f"{self.FAIL} subtract(10, 3) = {result}, attendu {expected}")

if __name__ == "__main__":
    unittest.main(verbosity=2)
