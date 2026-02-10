"""
EXERCICE 2 : Fixtures pytest

Contexte :
Vous devez tester une classe Calculatrice avec des fixtures pytest.

Tâche :
Écrivez les tests en utilisant des fixtures pytest.
"""

import pytest

class Database:
    """Simule une base de données pour les tests"""
    def __init__(self):
        self.connected = False
        self.data = {}
    def connect(self):
        self.connected = True
    def disconnect(self):
        self.connected = False
    def save(self, key, value):
        if not self.connected: raise ConnectionError("Non connecté")
        self.data[key] = value
    def get(self, key):
        if not self.connected: raise ConnectionError("Non connecté")
        return self.data.get(key)

class Calculatrice:
    """Une calculatrice simple"""
    
    def __init__(self):
        self.history = []
    
    def ajouter(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def soustraire(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiplier(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def get_history(self):
        return self.history.copy()
    
    def clear_history(self):
        self.history = []

# TODO: Créer une fixture pour Calculatrice
@pytest.fixture
def calculatrice():
    """TODO: Retourner une instance de Calculatrice"""
    pass

def test_ajouter(calculatrice):
    """TODO: Tester l'addition avec la fixture"""
    pass

def test_soustraire(calculatrice):
    """TODO: Tester la soustraction avec la fixture"""
    pass

def test_multiplier(calculatrice):
    """TODO: Tester la multiplication avec la fixture"""
    pass

def test_history(calculatrice):
    """TODO: Tester l'historique avec la fixture"""
    pass

def test_clear_history(calculatrice):
    """TODO: Tester le vidage de l'historique"""
    pass
