"""
EXERCICE 4 : Couverture de Code

Contexte :
Vous devez tester une fonction complexe et atteindre 100% de couverture.

Tâche :
Écrivez les tests pour couvrir tous les chemins du code.
"""

import unittest

def classify_number(n):
    """Classifie un nombre en positif, négatif ou zéro."""
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

def valider_utilisateur(donnees):
    """
    Valide les données utilisateur.
    Retourne (True, message) si valide, (False, message) sinon.
    """
    if not donnees:
        return (False, "Données vides")
    
    if "nom" not in donnees or not donnees["nom"]:
        return (False, "Nom manquant")
    
    if "email" not in donnees or not donnees["email"]:
        return (False, "Email manquant")
    
    if "@" not in donnees["email"]:
        return (False, "Email invalide")
    
    if "age" not in donnees:
        return (False, "Age manquant")
    
    try:
        age = int(donnees["age"])
        if age < 0 or age > 150:
            return (False, "Age invalide")
    except (ValueError, TypeError):
        return (False, "Age doit être un nombre")
    
    return (True, "Utilisateur valide")

class TestCouvertureCode(unittest.TestCase):
    """Tests pour atteindre 100% de couverture"""
    
    def test_donnees_vides(self):
        """TODO: Tester avec données vides"""
        pass
    
    def test_nom_manquant(self):
        """TODO: Tester avec nom manquant"""
        pass
    
    def test_email_manquant(self):
        """TODO: Tester avec email manquant"""
        pass
    
    def test_email_invalide(self):
        """TODO: Tester avec email invalide"""
        pass
    
    def test_age_manquant(self):
        """TODO: Tester avec age manquant"""
        pass
    
    def test_age_invalide_negatif(self):
        """TODO: Tester avec age négatif"""
        pass
    
    def test_age_invalide_trop_grand(self):
        """TODO: Tester avec age > 150"""
        pass
    
    def test_age_non_nombre(self):
        """TODO: Tester avec age non numérique"""
        pass
    
    def test_utilisateur_valide(self):
        """TODO: Tester avec données valides"""
        pass


if __name__ == "__main__":
    unittest.main()
