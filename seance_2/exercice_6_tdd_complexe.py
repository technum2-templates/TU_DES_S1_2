"""
EXERCICE 6 : TDD Complexe

Contexte :
Vous devez implémenter une classe en utilisant TDD.

Tâche :
1. Écrivez les tests d'abord (décrivez le comportement attendu)
2. Implémentez le code minimal pour passer les tests
3. Refactorisez

Classe à implémenter :
- Panier : Gère un panier d'achat avec articles et prix
"""

import unittest

class ShoppingCart:
    """Panier d'achat simple pour les tests"""
    def __init__(self):
        self.items = []
    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
    def total(self):
        return sum(item["price"] for item in self.items)

# TODO: Implémenter cette classe
class Panier:
    """
    Gère un panier d'achat.
    
    Méthodes attendues:
    - ajouter_article(nom, prix, quantite)
    - retirer_article(nom)
    - get_total()
    - get_articles()
    - appliquer_reduction(pourcentage)
    """
    pass

class TestPanier(unittest.TestCase):
    """Tests pour Panier (TDD complexe)"""
    
    def setUp(self):
        """TODO: Initialiser un panier avant chaque test"""
        pass
    
    def test_panier_vide(self):
        """TODO: Tester un panier vide"""
        pass
    
    def test_ajouter_article(self):
        """TODO: Tester l'ajout d'un article"""
        pass
    
    def test_ajouter_plusieurs_articles(self):
        """TODO: Tester l'ajout de plusieurs articles"""
        pass
    
    def test_retirer_article(self):
        """TODO: Tester la suppression d'un article"""
        pass
    
    def test_get_total(self):
        """TODO: Tester le calcul du total"""
        pass
    
    def test_appliquer_reduction(self):
        """TODO: Tester l'application d'une réduction"""
        pass
    
    def test_reduction_zero(self):
        """TODO: Tester avec réduction de 0%"""
        pass
    
    def test_reduction_100(self):
        """TODO: Tester avec réduction de 100%"""
        pass


if __name__ == "__main__":
    unittest.main()
