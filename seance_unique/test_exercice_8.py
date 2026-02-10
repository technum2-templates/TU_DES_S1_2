"""Tests de validation pour exercice 8 - Fixtures"""
import unittest
from exercice_8_fixtures import Database

class TestExercice8(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = Database()
    
    def test_database_exists(self):
        self.assertIsNotNone(self.db)
    
    def test_save_method_exists(self):
        # Dans exercice_8_fixtures.py, la méthode s'appelle 'save' et non 'insert'
        self.assertTrue(hasattr(self.db, 'save'), "La méthode 'save' est manquante dans la classe Database")

if __name__ == "__main__":
    unittest.main()
