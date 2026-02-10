"""Tests de validation pour exercice 1 - Setup/Teardown"""
import unittest
from exercice_7_setup_teardown import Calculator

class TestExercice7(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_calculator_exists(self):
        self.assertIsNotNone(self.calc)
    
    def test_add_method_exists(self):
        self.assertTrue(hasattr(self.calc, 'add'))
    
    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()
