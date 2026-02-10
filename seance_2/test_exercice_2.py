"""Tests de validation pour exercice 2 - Fixtures"""
import unittest
from exercice_2_fixtures import Database

class TestExercice2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = Database()
    
    def test_database_exists(self):
        self.assertIsNotNone(self.db)
    
    def test_insert_method_exists(self):
        self.assertTrue(hasattr(self.db, 'insert'))

if __name__ == "__main__":
    unittest.main()
