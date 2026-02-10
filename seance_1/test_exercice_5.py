"""Tests de validation pour exercice 5 - Fonction Dictionnaires"""
import unittest
from exercice_5_fonction_dictionnaires import get_value, has_key

class TestExercice5(unittest.TestCase):
    def test_get_value_function_exists(self):
        self.assertTrue(callable(get_value))
    
    def test_get_value(self):
        d = {"name": "John", "age": 30}
        self.assertEqual(get_value(d, "name"), "John")
    
    def test_has_key_function_exists(self):
        self.assertTrue(callable(has_key))
    
    def test_has_key(self):
        d = {"name": "John"}
        self.assertTrue(has_key(d, "name"))

if __name__ == "__main__":
    unittest.main()
