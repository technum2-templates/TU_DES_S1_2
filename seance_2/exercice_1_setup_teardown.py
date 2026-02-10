"""
EXERCICE 1 : Setup et Teardown

Contexte :
Vous devez tester une classe qui gère une liste de tâches.
Les tests ont besoin d'une liste vierge avant chaque test.

Tâche :
Écrivez les tests avec setUp() et tearDown().
"""

import unittest

class Calculator:
    """Calculatrice simple pour les tests"""
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b

class TodoList:
    """Gère une liste de tâches"""
    
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        """Ajoute une tâche"""
        self.tasks.append(task)
    
    def remove_task(self, task):
        """Supprime une tâche"""
        if task in self.tasks:
            self.tasks.remove(task)
    
    def get_tasks(self):
        """Retourne toutes les tâches"""
        return self.tasks.copy()
    
    def clear(self):
        """Vide la liste"""
        self.tasks = []

class TestTodoList(unittest.TestCase):
    """Tests pour TodoList avec setUp/tearDown"""
    
    def setUp(self):
        """TODO: Initialiser une TodoList avant chaque test"""
        pass
    
    def tearDown(self):
        """TODO: Nettoyer après chaque test"""
        pass
    
    def test_add_task(self):
        """TODO: Tester l'ajout d'une tâche"""
        pass
    
    def test_remove_task(self):
        """TODO: Tester la suppression d'une tâche"""
        pass
    
    def test_get_tasks(self):
        """TODO: Tester la récupération des tâches"""
        pass
    
    def test_clear(self):
        """TODO: Tester le vidage de la liste"""
        pass
    
    def test_multiple_tasks(self):
        """TODO: Tester avec plusieurs tâches"""
        pass


if __name__ == "__main__":
    unittest.main()
