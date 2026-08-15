# tests/unit/test_calculator.py

import pytest  # Import the pytest framework for writing and running tests
from typing import Union  # Import Union for type hinting multiple possible types
from app.operations import add, subtract, multiply, divide, hypotenuse  # Import the calculator functions from the operations module

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]


# ---------------------------------------------
# Unit Tests for the 'add' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),           # Test adding two positive integers
        (-2, -3, -5),        # Test adding two negative integers
        (2.5, 3.5, 6.0),     # Test adding two positive floats
        (-2.5, 3.5, 1.0),    # Test adding a negative float and a positive float
        (0, 0, 0),            # Test adding zeros
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_two_positive_floats",
        "add_negative_and_positive_float",
        "add_zeros",
    ]
)
def test_add(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'add' function with various combinations of integers and floats.

    This parameterized test verifies that the 'add' function correctly adds two numbers,
    whether they are positive, negative, integers, or floats. By using parameterization,
    we can efficiently test multiple scenarios without redundant code.

    Parameters:
    - a (Number): The first number to add.
    - b (Number): The second number to add.
    - expected (Number): The expected result of the addition.

    Steps:
    1. Call the 'add' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_add(2, 3, 5)
    >>> test_add(-2, -3, -5)
    """
    # Call the 'add' function with the provided arguments
    result = add(a, b)
    
    # Assert that the result of add(a, b) matches the expected value
    assert result == expected, f"Expected add({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'subtract' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),           # Test subtracting a smaller positive integer from a larger one
        (-5, -3, -2),        # Test subtracting a negative integer from another negative integer
        (5.5, 2.5, 3.0),     # Test subtracting two positive floats
        (-5.5, -2.5, -3.0),  # Test subtracting two negative floats
        (0, 0, 0),            # Test subtracting zeros
    ],
    ids=[
        "subtract_two_positive_integers",
        "subtract_two_negative_integers",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_zeros",
    ]
)
def test_subtract(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'subtract' function with various combinations of integers and floats.

    This parameterized test verifies that the 'subtract' function correctly subtracts the
    second number from the first, handling both positive and negative values, as well as
    integers and floats. Parameterization allows for comprehensive testing of multiple cases.

    Parameters:
    - a (Number): The number from which to subtract.
    - b (Number): The number to subtract.
    - expected (Number): The expected result of the subtraction.

    Steps:
    1. Call the 'subtract' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_subtract(5, 3, 2)
    >>> test_subtract(-5, -3, -2)
    """
    # Call the 'subtract' function with the provided arguments
    result = subtract(a, b)
    
    # Assert that the result of subtract(a, b) matches the expected value
    assert result == expected, f"Expected subtract({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'multiply' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),           # Test multiplying two positive integers
        (-2, 3, -6),         # Test multiplying a negative integer with a positive integer
        (2.5, 4.0, 10.0),    # Test multiplying two positive floats
        (-2.5, 4.0, -10.0),  # Test multiplying a negative float with a positive float
        (0, 5, 0),            # Test multiplying zero with a positive integer
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_negative_and_positive_integer",
        "multiply_two_positive_floats",
        "multiply_negative_float_and_positive_float",
        "multiply_zero_and_positive_integer",
    ]
)
def test_multiply(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'multiply' function with various combinations of integers and floats.

    This parameterized test verifies that the 'multiply' function correctly multiplies two numbers,
    handling both positive and negative values, as well as integers and floats. Parameterization
    enables efficient testing of multiple scenarios in a concise manner.

    Parameters:
    - a (Number): The first number to multiply.
    - b (Number): The second number to multiply.
    - expected (Number): The expected result of the multiplication.

    Steps:
    1. Call the 'multiply' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_multiply(2, 3, 6)
    >>> test_multiply(-2, 3, -6)
    """
    # Call the 'multiply' function with the provided arguments
    result = multiply(a, b)
    
    # Assert that the result of multiply(a, b) matches the expected value
    assert result == expected, f"Expected multiply({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'divide' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           # Test dividing two positive integers
        (-6, 3, -2.0),         # Test dividing a negative integer by a positive integer
        (6.0, 3.0, 2.0),       # Test dividing two positive floats
        (-6.0, 3.0, -2.0),     # Test dividing a negative float by a positive float
        (0, 5, 0.0),            # Test dividing zero by a positive integer
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_negative_integer_by_positive_integer",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
    ]
)
def test_divide(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'divide' function with various combinations of integers and floats.

    This parameterized test verifies that the 'divide' function correctly divides the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.

    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (float): The expected result of the division.

    Steps:
    1. Call the 'divide' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_divide(6, 3, 2.0)
    >>> test_divide(-6, 3, -2.0)
    """
    # Call the 'divide' function with the provided arguments
    result = divide(a, b)
    
    # Assert that the result of divide(a, b) matches the expected value
    assert result == expected, f"Expected divide({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Negative Test Case: Division by Zero
# ---------------------------------------------

def test_divide_by_zero() -> None:
    """
    Test the 'divide' function with division by zero.

    This negative test case verifies that attempting to divide by zero raises a ValueError
    with the appropriate error message. It ensures that the application correctly handles
    invalid operations and provides meaningful feedback to the user.

    Steps:
    1. Attempt to call the 'divide' function with arguments 6 and 0, which should raise a ValueError.
    2. Use pytest's 'raises' context manager to catch the expected exception.
    3. Assert that the error message contains "Cannot divide by zero!".

    Example:
    >>> test_divide_by_zero()
    """
    # Use pytest's context manager to check for a ValueError when dividing by zero
    with pytest.raises(ValueError) as excinfo:
        # Attempt to divide 6 by 0, which should raise a ValueError
        divide(6, 0)
    
    # Assert that the exception message contains the expected error message
    assert "Cannot divide by zero!" in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero!', but got '{excinfo.value}'"


# ---------------------------------------------
# Unit Tests for the 'hypotenuse' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 5),           # Test hypotenuse with two integers
        (2, 6, 6.32),           # Test hypotenuse with two integers reulsting with float
        (3.5, 5.2, 6.27),    # Test hypotenuse with two floats
        (4, 6.7, 7.8),       # Test hypotenuse with one integer and one float
    ],
    ids=[
        "hypotenuse_two_integers",
        "hypotenuse_two_integers_result_float",
        "hypotenuse_two_floats",
        "hypotenuse_one_integer_one_float",
    ]
)
def test_hypotenuse(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'hypotenuse' operation with different combinations of integers and floats.

    This parameterized test verifies that the 'hypotenuse' function correctly finds the
    hypotenuse of a right triangle based on the two side lengths provided. It handles
    positive integers and floats. Parameterization allows for efficient and comprehensive 
    testing across multiple cases.

    Parameters:
    - a (Number): First side.
    - b (Number): Second side.
    - expected (float): The expected hypotenuse.

    Steps:
    1. Call the 'hypotenuse' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_hypotenuse(2, 6, 6.32)
    >>> test_hypotenuse(4, 6.7, 7.8)
    """
    # Call the 'hypotenuse' function with the provided arguments
    result = hypotenuse(a, b)
    
    # Assert that the result of hypotenuse(a, b) matches the expected value
    assert result == expected, f"Expected hypotenuse({a}, {b}) to be {expected}, but got {result}"

# ---------------------------------------------
# Invalid Test Case: Incorrect number of inputs
# ---------------------------------------------

@pytest.mark.parametrize(
    "numbers",
    [
        (3,),
        (3, 4, 5),
    ],
    ids=[
        "hypotenuse_too_few_numbers",
        "hypotenuse_too_many_numbers",
    ]
)
def test_hypotenuse_invalid_number_of_inputs(numbers) -> None:
    """
    Test the 'hypotenuse' function with more than two numbers

    This test case verifies that inputs with an incorrect number of inputs
    raises a ValueError. It ensures that the application correctly handles
    invalid operations and provides meaningful feedback to the user.

    Steps:
    1. Attempt to call the 'hypotenuse' function with with an incorrect number of inputs, which should raise a ValueError.
    2. Use pytest's 'raises' context manager to catch the expected exception.
    3. Assert that the error message contains "Exactly two numbers are required to calculate hypotenuse.".

    Example:
    >>> test_hypotenuse_invalid_number_of_inputs()
    """
    # Use pytest's context manager to check for a ValueError when given an incorrect number of inputs
    with pytest.raises(ValueError) as excinfo:
        # Attempt to calculate hypotenuse with an incorrect number of inputs, which should raise ValueError
        hypotenuse(*numbers)
    
    # Assert that the exception message contains the expected error message
    assert "Exactly two numbers are required to calculate hypotenuse." in str(excinfo.value), \
        f"Expected error message 'Exactly two numbers are required to calculate hypotenuse.', but got '{excinfo.value}'"

# ---------------------------------------------
# Invalid Test Case: Number less than or equal to 0
# ---------------------------------------------
@pytest.mark.parametrize(
    "a, b",
    [
        (0, 4),
        (4, 0),
        (-3, 4),
        (3, -4),
        (-3, -4),
        (0, 0),
    ],
    ids=[
        "hypotenuse_zero_first_side",
        "hypotenuse_zero_second_side",
        "hypotenuse_negative_first_side",
        "hypotenuse_negative_second_side",
        "hypotenuse_both_negative",
        "hypotenuse_both_zero",
    ]
)
def test_hypotenuse_equal_or_less_than_zero(a: Number, b: Number) -> None:
    """
    Test the 'hypotenuse' function with a number less than one.

    This test case verifies that an input with any number less than or equal to zero raises a ValueError
    with the appropriate error message. It ensures that the application correctly handles
    invalid operations and provides meaningful feedback to the user.

    Steps:
    1. Attempt to call the 'hypotenuse' function with arguments 0 and 4, which should raise a ValueError.
    2. Use pytest's 'raises' context manager to catch the expected exception.
    3. Assert that the error message contains "Side lengths must be greater than zero.".

    Example:
    >>> test_hypotenuse_equal_or_less_than_zero()
    """
    # Use pytest's context manager to check for a ValueError when given a number equal to or less than 0
    with pytest.raises(ValueError) as excinfo:
        # Attempt to calculate hypotenuse with 0 and 4, which should raise ValueError
        hypotenuse(a, b)
    
    # Assert that the exception message contains the expected error message
    assert "Side lengths must be greater than zero." in str(excinfo.value), \
        f"Expected error message 'Side lengths must be greater than zero.', but got '{excinfo.value}'"