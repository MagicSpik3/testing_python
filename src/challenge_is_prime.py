# python -m doctest -v .\challenge_is_prime.py
import pytest
import math
import time
import random
 
 
def is_prime(n):
    return()
           
def tests_main():
    # don't touch this function...
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False

 

    items = [
        (3, True),
        (5, True),
        (6, False),
        (9, False),
        (102241, True),
        (102243, False),
        (15485863, True),
    ]

    for item, answer in items:
        assert is_prime(item) is answer

 
def test_exception():
    # don't touch this function...
    with pytest.raises(ValueError):
        is_prime(0)
    with pytest.raises(ValueError):
        is_prime(1)
    with pytest.raises(ValueError):
        is_prime(-1)