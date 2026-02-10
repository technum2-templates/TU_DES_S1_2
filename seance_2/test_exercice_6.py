"""Tests de validation pour exercice 6 - TDD Complexe"""
import unittest
from exercice_6_tdd_complexe import ShoppingCart

class TestExercice6(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
    
    def test_add_item(self):
        self.cart.add_item("apple", 1.5)
        self.assertEqual(len(self.cart.items), 1)
    
    def test_total_price(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("banana", 0.5)
        self.assertEqual(self.cart.total(), 2.0)

if __name__ == "__main__":
    unittest.main()
