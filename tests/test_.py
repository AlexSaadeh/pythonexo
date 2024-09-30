import pytest
from python import identity_function, mult_two, rectangle_perimeter, is_even, determine_sign, find_remainder

def test_identity_function():
    assert identity_function(3) == 3
    assert identity_function("string") == "string"
    assert identity_function(True) is True

def test_mult_two():
    assert mult_two(3, 2) == 6
    assert mult_two(0, 1) == 0

def test_rectangle_perimeter():
    assert rectangle_perimeter(2, 4) == 12
    assert rectangle_perimeter(3, 5) == 16
    assert rectangle_perimeter(10, 20) == 60

def test_is_even():
    assert is_even(2) is True
    assert is_even(5) is False
    assert is_even(0) is True

def test_determine_sign():
    assert determine_sign(5) == "positive"
    assert determine_sign(0) == "zero"
    assert determine_sign(-10) == "negative"

def test_find_remainder():
    assert find_remainder(10, 3) == 1
    assert find_remainder(14, 4) == 2
