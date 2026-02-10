"""Tests de validation pour exercice 3 - Paramétrize"""
import unittest
from parameterized import parameterized
from exercice_3_parametrize import multiply

class TestExercice3(unittest.TestCase):
    @parameterized.expand([
        (2, 3, 6),
        (5, 4, 20),
        (0, 10, 0),
    ])
    def test_multiply(self, a, b, expected):
        self.assertEqual(multiply(a, b), expected)

if __name__ == "__main__":
    unittest.main()
