"""
EXERCICE 6 : Fonction Complexe

Contexte :
Vous devez tester une fonction plus complexe qui combine plusieurs concepts.

Tâche :
Écrivez des tests complets pour couvrir tous les cas.
"""

import unittest

def fibonacci(n):
    """Calcule le n-ième nombre de Fibonacci."""
    if n <= 0: return 0
    elif n == 1: return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def factorial(n):
    """Calcule la factorielle de n."""
    if n < 0: raise ValueError("n doit être positif")
    if n == 0: return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calculer_moyenne(notes):
    """Calcule la moyenne des notes. Lève ValueError si liste vide."""
    if not notes:
        raise ValueError("Liste vide")
    return sum(notes) / len(notes)

def valider_email(email):
    """Valide un email simple. Retourne True si valide."""
    if "@" not in email or "." not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    return len(parts[0]) > 0 and len(parts[1]) > 0

def traiter_donnees(donnees):
    """Traite un dictionnaire de données. Lève KeyError si clés manquantes."""
    required_keys = ["nom", "age", "email"]
    for key in required_keys:
        if key not in donnees:
            raise KeyError(f"Clé manquante: {key}")
    
    return {
        "nom": donnees["nom"].upper(),
        "age": int(donnees["age"]),
        "email": donnees["email"].lower(),
        "valide": donnees["age"] >= 18
    }

class TestFonctionsComplexes(unittest.TestCase):
    """Tests pour les fonctions complexes"""
    
    def test_calculer_moyenne_normal(self):
        """TODO: Tester le calcul de moyenne normal"""
        pass
    
    def test_calculer_moyenne_vide(self):
        """TODO: Tester avec une liste vide (doit lever ValueError)"""
        pass
    
    def test_calculer_moyenne_un_element(self):
        """TODO: Tester avec un seul élément"""
        pass
    
    def test_valider_email_valide(self):
        """TODO: Tester un email valide"""
        pass
    
    def test_valider_email_sans_arobase(self):
        """TODO: Tester un email sans @"""
        pass
    
    def test_valider_email_sans_point(self):
        """TODO: Tester un email sans point"""
        pass
    
    def test_traiter_donnees_valides(self):
        """TODO: Tester le traitement de données valides"""
        pass
    
    def test_traiter_donnees_manquantes(self):
        """TODO: Tester avec des données manquantes (doit lever KeyError)"""
        pass
    
    def test_traiter_donnees_transformation(self):
        """TODO: Tester que les données sont transformées correctement"""
        pass


if __name__ == "__main__":
    unittest.main()
