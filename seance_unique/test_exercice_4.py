"""Tests de validation pour exercice 4 - Fonction Listes"""
import unittest
from exercice_4_fonction_listes import sum_list, find_max

class TestExercice4(unittest.TestCase):
    def test_sum_list_function_exists(self):
        self.assertTrue(callable(sum_list))
    
    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3]), 6)
        self.assertEqual(sum_list([10, 20]), 30)
    
    def test_find_max_function_exists(self):
        self.assertTrue(callable(find_max))
    
    def test_find_max(self):
        self.assertEqual(find_max([1, 5, 3]), 5)

if __name__ == "__main__":
    unittest.main()
