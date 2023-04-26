import pytest

def add_numbers(a, b):
    return a + b

def test_add_numbers():
    assert add_numbers(1, 2) == 3
