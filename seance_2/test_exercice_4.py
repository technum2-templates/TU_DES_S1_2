"""Tests de validation pour exercice 4 - Couverture Code"""
import unittest
from exercice_4_couverture_code import classify_number

class TestExercice4(unittest.TestCase):
    def test_classify_positive(self):
        self.assertEqual(classify_number(5), "positive")
    
    def test_classify_negative(self):
        self.assertEqual(classify_number(-5), "negative")
    
    def test_classify_zero(self):
        self.assertEqual(classify_number(0), "zero")

if __name__ == "__main__":
    unittest.main()
