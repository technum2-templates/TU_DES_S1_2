"""Tests de validation pour exercice 6 - Fonction Complexe"""
import unittest
from exercice_6_fonction_complexe import fibonacci, factorial

class TestExercice6(unittest.TestCase):
    def test_fibonacci_function_exists(self):
        self.assertTrue(callable(fibonacci))
    
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
    
    def test_factorial_function_exists(self):
        self.assertTrue(callable(factorial))
    
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

if __name__ == "__main__":
    unittest.main()
