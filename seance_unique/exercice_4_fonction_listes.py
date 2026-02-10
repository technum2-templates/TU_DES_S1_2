"""
EXERCICE 4 : Fonction avec Listes

Contexte :
Vous devez tester une fonction qui manipule des listes.

Tâche :
Écrivez des tests pour couvrir tous les cas avec les collections.
"""

import unittest

def sum_list(lst):
    """Retourne la somme de tous les éléments de la liste."""
    return sum(lst)

def find_max(lst):
    if not lst:
        raise ValueError("Liste vide")
    return max(lst)

def filtrer_positifs(lst):
    """Retourne une nouvelle liste avec seulement les nombres positifs."""
    return [x for x in lst if x > 0]

def compter_occurrences(lst, element):
    """Compte le nombre d'occurrences d'un élément dans la liste."""
    return lst.count(element)

class TestFonctionsListes(unittest.TestCase):
    """Tests pour les fonctions avec listes"""
    
    def test_somme_liste_normale(self):
        """TODO: Tester la somme d'une liste normale"""
        pass
    
    def test_somme_liste_vide(self):
        """TODO: Tester la somme d'une liste vide"""
        pass
    
    def test_somme_liste_negatifs(self):
        """TODO: Tester la somme avec des nombres négatifs"""
        pass
    
    def test_filtrer_positifs_mixte(self):
        """TODO: Tester le filtrage avec une liste mixte"""
        pass
    
    def test_filtrer_positifs_tous_negatifs(self):
        """TODO: Tester le filtrage avec tous négatifs"""
        pass
    
    def test_filtrer_positifs_vide(self):
        """TODO: Tester le filtrage d'une liste vide"""
        pass
    
    def test_compter_occurrences_present(self):
        """TODO: Tester le comptage d'un élément présent"""
        pass
    
    def test_compter_occurrences_absent(self):
        """TODO: Tester le comptage d'un élément absent"""
        pass
    
    def test_compter_occurrences_multiple(self):
        """TODO: Tester le comptage avec plusieurs occurrences"""
        pass


if __name__ == "__main__":
    unittest.main()
