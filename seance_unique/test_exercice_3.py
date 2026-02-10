"""Tests de validation pour exercice 3 - Fonction Exceptions"""
import unittest
from exercice_3_fonction_exceptions import divide, parse_int

class TestExercice3(unittest.TestCase):
    def test_divide_function_exists(self):
        self.assertTrue(callable(divide))
    
    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == "__main__":
    unittest.main()
