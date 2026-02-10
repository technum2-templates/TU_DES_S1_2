"""Tests de validation pour exercice 5 - TDD Simple"""
import unittest
from exercice_11_tdd_simple import BankAccount

class TestExercice5(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)
    
    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)
    
    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
    
    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

if __name__ == "__main__":
    unittest.main()
