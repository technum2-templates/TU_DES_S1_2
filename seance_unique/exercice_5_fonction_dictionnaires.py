"""
EXERCICE 5 : Fonction avec Dictionnaires

Contexte :
Vous devez tester une fonction qui manipule des dictionnaires.

Tâche :
Écrivez des tests pour couvrir tous les cas avec les dictionnaires.
"""

import unittest

def get_value(dico, cle, defaut=None):
    """Obtient la valeur d'une clé, retourne defaut si absent."""
    return dico.get(cle, defaut)

def fusionner_dicos(dico1, dico2):
    """Fusionne deux dictionnaires. dico2 écrase dico1."""
    result = dico1.copy()
    result.update(dico2)
    return result

def has_key(dico, cle):
    """Vérifie si une clé existe dans le dictionnaire."""
    return cle in dico

def inverser_dico(dico):
    """Inverse les clés et valeurs du dictionnaire."""
    return {v: k for k, v in dico.items()}

class TestFonctionsDictionnaires(unittest.TestCase):
    """Tests pour les fonctions avec dictionnaires"""
    
    def test_obtenir_valeur_presente(self):
        """TODO: Tester l'obtention d'une valeur présente"""
        pass
    
    def test_obtenir_valeur_absente(self):
        """TODO: Tester l'obtention d'une valeur absente"""
        pass
    
    def test_obtenir_valeur_avec_defaut(self):
        """TODO: Tester avec une valeur par défaut"""
        pass
    
    def test_fusionner_dicos_normal(self):
        """TODO: Tester la fusion normale"""
        pass
    
    def test_fusionner_dicos_vide(self):
        """TODO: Tester la fusion avec un dico vide"""
        pass
    
    def test_fusionner_dicos_ecrasement(self):
        """TODO: Tester que dico2 écrase dico1"""
        pass
    
    def test_inverser_dico_normal(self):
        """TODO: Tester l'inversion normale"""
        pass
    
    def test_inverser_dico_vide(self):
        """TODO: Tester l'inversion d'un dico vide"""
        pass


if __name__ == "__main__":
    unittest.main()
