import pytest
from src.module1 import return_true

def test_return_true():
    assert return_true() == True