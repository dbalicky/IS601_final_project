# app/operations.py

"""
Module: operations.py

This module contains basic arithmetic functions that perform addition, subtraction,
multiplication, and division of two numbers. These functions are foundational for
building more complex applications, such as calculators or financial tools.

Functions:
- add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]: Returns the sum of a and b.
- subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]: Returns the difference when b is subtracted from a.
- multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]: Returns the product of a and b.
- divide(a: Union[int, float], b: Union[int, float]) -> float: Returns the quotient when a is divided by b. Raises ValueError if b is zero.

Usage:
These functions can be imported and used in other modules or integrated into APIs
to perform arithmetic operations based on user input.
"""

from typing import Union  # Import Union for type hinting multiple possible types
import math               # Import math to use sqrt function for hypotenuse opeartion

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """
    Add two numbers and return the result.

    Parameters:
    - a (int or float): The first number to add.
    - b (int or float): The second number to add.

    Returns:
    - int or float: The sum of a and b.

    Example:
    >>> add(2, 3)
    5
    >>> add(2.5, 3)
    5.5
    """
    # Perform addition of a and b
    result = a + b
    return result

def subtract(a: Number, b: Number) -> Number:
    """
    Subtract the second number from the first and return the result.

    Parameters:
    - a (int or float): The number from which to subtract.
    - b (int or float): The number to subtract.

    Returns:
    - int or float: The difference between a and b.

    Example:
    >>> subtract(5, 3)
    2
    >>> subtract(5.5, 2)
    3.5
    """
    # Perform subtraction of b from a
    result = a - b
    return result

def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers and return the product.

    Parameters:
    - a (int or float): The first number to multiply.
    - b (int or float): The second number to multiply.

    Returns:
    - int or float: The product of a and b.

    Example:
    >>> multiply(2, 3)
    6
    >>> multiply(2.5, 4)
    10.0
    """
    # Perform multiplication of a and b
    result = a * b
    return result

def divide(a: Number, b: Number) -> float:
    """
    Divide the first number by the second and return the quotient.

    Parameters:
    - a (int or float): The dividend.
    - b (int or float): The divisor.

    Returns:
    - float: The quotient of a divided by b.

    Raises:
    - ValueError: If b is zero, as division by zero is undefined.

    Example:
    >>> divide(6, 3)
    2.0
    >>> divide(5.5, 2)
    2.75
    >>> divide(5, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero!
    """
    # Check if the divisor is zero to prevent division by zero
    if b == 0:
        # Raise a ValueError with a descriptive message
        raise ValueError("Cannot divide by zero!")
    
    # Perform division of a by b and return the result as a float
    result = a / b
    return result

def hypotenuse(*numbers):
    """
    Find the hypotenuse given two sides.
    
    Parameters:
    - *numbers: Exactly two numbers which represent the side lengths.
    
    Returns:
    - float: The hypotenuse rounded to two decimal places.

    Raises:
    - ValueError: If there are not exactly two inputs, or if
                  any input is less than or equal to zero.

    Examples:
    >>> hypotenuse(3, 4)
    5.0
    >>> hypotenuse(2, 6)
    6.32
    >>> hypotenuse(2, 3, 4)
    Traceback (most recent call last):
        ...
    ValueError: Exactly two numbers are required to calculate hypotenuse.
    >>> hypotenuse(0, 5)
        Traceback (most recent call last):
            ...
        ValueError: Side lengths must be greater than zero.
    """
    # Check if there are exactly two inputs
    if len(numbers) != 2:
        raise ValueError(
            "Exactly two numbers are required to calculate hypotenuse."
        )
    # Check if both inputs are greater than zero
    if any(number <= 0 for number in numbers):
        raise ValueError("Side lengths must be greater than zero.")

    # Find the hypotenuse of the two side lenghts
    result = round(
        math.sqrt(numbers[0] ** 2 + numbers[1] ** 2),
        2
    )
    return result