# tests/test_.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python import func, mult_two, rectangle_perimeter, is_even, determine_sign, find_remainder

def test_func():
    assert func(3) == 3
    assert func("string") == "string"
    assert func(True) == True

def test_mult_two():
    assert mult_two(1, 2) == 2
    assert mult_two(3, 2) == 6
    assert mult_two(0, 1) == 0

def test_rectangle_perimeter():
    assert rectangle_perimeter(2, 4) == 12
    assert rectangle_perimeter(3, 5) == 16

def test_is_even():
    assert is_even(2) == True
    assert is_even(5) == False

def test_determine_sign():
    assert determine_sign(5) == "positive"
    assert determine_sign(0) == "zero"
    assert determine_sign(-10) == "negative"

def test_find_remainder():
    assert find_remainder(10, 3) == 1
    assert find_remainder(14, 4) == 2
