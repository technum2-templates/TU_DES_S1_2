"""
EXERCICE 5 : TDD Simple (Test-Driven Development)

Contexte :
Vous devez implémenter une fonction en utilisant TDD.
Cycle : Red (test échoue) → Green (code minimal) → Refactor

Tâche :
1. Écrivez les tests d'abord
2. Implémentez le code minimal pour passer les tests
3. Refactorisez si nécessaire

Fonction à implémenter :
- est_palindrome(s) : Retourne True si s est un palindrome
"""

import unittest

class BankAccount:
    """Compte bancaire simple pour les tests"""
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Solde insuffisant")
        self.balance -= amount

# TODO: Implémenter cette fonction
def est_palindrome(s):
    """
    Retourne True si la chaîne est un palindrome (ignore les espaces et casse).
    Exemple: "A man a plan a canal Panama" est un palindrome
    """
    pass

class TestEstPalindrome(unittest.TestCase):
    """Tests pour est_palindrome (TDD)"""
    
    def test_palindrome_simple(self):
        """TODO: Tester un palindrome simple"""
        pass
    
    def test_non_palindrome(self):
        """TODO: Tester un non-palindrome"""
        pass
    
    def test_palindrome_avec_espaces(self):
        """TODO: Tester un palindrome avec espaces"""
        pass
    
    def test_palindrome_casse_differente(self):
        """TODO: Tester un palindrome avec casse différente"""
        pass
    
    def test_une_lettre(self):
        """TODO: Tester avec une seule lettre"""
        pass
    
    def test_chaîne_vide(self):
        """TODO: Tester avec une chaîne vide"""
        pass


if __name__ == "__main__":
    unittest.main()
