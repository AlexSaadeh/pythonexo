"""This module contains several mathematical functions and operations."""

# Constants
A = 2
B = 5

# Calculate sum and product of constants
ADD = A + B
MULTI = A * B

def identity_function(value):
    """Returns the input value."""
    return value

print("Example:")
print(identity_function(3))

# These "asserts" are used for self-checking
assert identity_function(3) == 3
assert identity_function("string") == "string"
assert identity_function(True) is True

print("The mission is done! Click 'Check Solution' to earn rewards!")

def mult_two(a: int, b: int) -> int:
    """Returns the product of two numbers."""
    return a * b

print("Example:")
print(mult_two(1, 2))

assert mult_two(3, 2) == 6
assert mult_two(0, 1) == 0

print("The first mission is done! Click 'Check' to earn cool rewards!")

def rectangle_perimeter(length: int, width: int) -> int:
    """Returns the perimeter of a rectangle."""
    return 2 * (length + width)

print("Example:")
print(rectangle_perimeter(3, 2))

# These "asserts" are used for self-checking
assert rectangle_perimeter(2, 4) == 12
assert rectangle_perimeter(3, 5) == 16
assert rectangle_perimeter(10, 20) == 60
assert rectangle_perimeter(7, 2) == 18
assert rectangle_perimeter(1, 1) == 4
assert rectangle_perimeter(1, 5) == 12
assert rectangle_perimeter(4, 1) == 10
assert rectangle_perimeter(100, 100) == 400
assert rectangle_perimeter(0.5, 2) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")

def is_even(num: int) -> bool:
    """Determines if a number is even."""
    return num % 2 == 0

print("Example:")
print(is_even(2))

# These "asserts" are used for self-checking
assert is_even(2) is True
assert is_even(5) is False
assert is_even(0) is True

print("The mission is done! Click 'Check Solution' to earn rewards!")

def determine_sign(num: int) -> str:
    """Determines the sign of a number."""
    if num < 0:
        return "negative"
    elif num > 0:
        return "positive"
    else:
        return "zero"

print("Example:")
print(determine_sign(11))

# These "asserts" are used for self-checking
assert determine_sign(5) == "positive"
assert determine_sign(0) == "zero"
assert determine_sign(-10) == "negative"
assert determine_sign(1) == "positive"
assert determine_sign(-1) == "negative"
assert determine_sign(999) == "positive"
assert determine_sign(-1000) == "negative"
assert determine_sign(123456789) == "positive"
assert determine_sign(-987654321) == "negative"
assert determine_sign(2) == "positive"

print("The mission is done! Click 'Check Solution' to earn rewards!")

def find_remainder(dividend: int, divisor: int) -> int:
    """Returns the remainder of the division of dividend by divisor."""
    return dividend % divisor

print("Example:")
print(find_remainder(3, 2))

# These "asserts" are used for self-checking
assert find_remainder(10, 3) == 1
assert find_remainder(14, 4) == 2
assert find_remainder(27, 4) == 3
assert find_remainder(10, 5) == 0
assert find_remainder(10, 1) == 0
assert find_remainder(5, 7) == 5
assert find_remainder(7, 5) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
