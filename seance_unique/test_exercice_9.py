"""Tests de validation pour exercice 9 - Parametrize"""
import pytest
from exercice_9_parametrize import multiply

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (5, 4, 20),
    (0, 10, 0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
