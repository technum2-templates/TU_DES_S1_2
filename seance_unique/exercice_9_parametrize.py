"""
EXERCICE 3 : Paramétrisation

Contexte :
Vous devez tester une fonction avec plusieurs cas différents.

Tâche :
Utilisez @pytest.mark.parametrize pour tester plusieurs cas.
"""

import pytest

def multiply(a, b):
    """Multiplie deux nombres"""
    return a * b

def double(n):
    """Retourne le double du nombre"""
    return n * 2

def est_positif(n):
    """Retourne True si positif"""
    return n > 0

def classer_nombre(n):
    """Classe un nombre: négatif, zéro, positif"""
    if n < 0:
        return "négatif"
    elif n == 0:
        return "zéro"
    else:
        return "positif"

# TODO: Paramétriser les tests pour double
@pytest.mark.parametrize("input,expected", [
    # TODO: Ajouter les cas de test
])
def test_double(input, expected):
    """TODO: Tester double avec paramétrisation"""
    pass

# TODO: Paramétriser les tests pour est_positif
@pytest.mark.parametrize("input,expected", [
    # TODO: Ajouter les cas de test
])
def test_est_positif(input, expected):
    """TODO: Tester est_positif avec paramétrisation"""
    pass

# TODO: Paramétriser les tests pour classer_nombre
@pytest.mark.parametrize("input,expected", [
    # TODO: Ajouter les cas de test
])
def test_classer_nombre(input, expected):
    """TODO: Tester classer_nombre avec paramétrisation"""
    pass
