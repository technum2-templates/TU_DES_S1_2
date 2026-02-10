"""
Configuration pytest pour les exercices Tests Unitaires
"""

import pytest


def pytest_configure(config):
    """Configuration initiale de pytest"""
    config.addinivalue_line(
        "markers", "seance0: marque les tests de la Séance 0"
    )
    config.addinivalue_line(
        "markers", "seance1: marque les tests de la Séance 1"
    )
    config.addinivalue_line(
        "markers", "seance2: marque les tests de la Séance 2"
    )


@pytest.fixture
def sample_list():
    """Fixture fournissant une liste de test"""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_dict():
    """Fixture fournissant un dictionnaire de test"""
    return {"nom": "Alice", "age": 30, "email": "alice@example.com"}
