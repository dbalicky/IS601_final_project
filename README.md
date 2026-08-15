# Final Project Setup

## Creating directory 

### Navigate to projects folder
```bash
cd is601_projects/
```

### Create directory
```bash
mkdir final_project

cd final_project
```

### Open in VSCode
```bash
code .
```


## Initialization

### Set python version to 3.10 via pyenv
```bash
pyenv local 3.10
```

### Create and activate venv
```bash
python -m venv venv

source venv/bin/activate
```

### Initialize repo
```bash
git init
```

### Add remote github repo
```bash
git remote add origin git@github.com:dbalicky/IS601_final_project.git
```


## Docker Repository Setup

### Create docker repo

- Repository: dbal7/is601_final_project

### Create secret tokens and add to github

**In DockerHub:**

- Account Settings -> Personal access tokens

- Generate new token

  - Account token description: final_project

  - Expiration date: none

  - Access permissions: Read & Write

**In GitHub Respository**

- Settings -> Secrets and variables -> Actions

For Username:

- New repository secret

  - Name: DOCKERHUB_USERNAME

  - Secret: dbal7

For Token:

- New repository secret

  - Name: DOCKERHUB_TOKEN

  - Secret: <personal access token from docker>


## Adding directories and files

### Create necessary folders and files from module 14
```bash
touch <folder/file>
```

### Initial commit and push
```bash
git add .

git commit -m 'Initial commit'

git push --set-upstream origin main
```

### Add code to files and commit
```bash
git add <file> # or <folder/file>

git commit -m 'added code to <filename>'

git push
```

### Set tokens in test.yml to match docker repo
```bash
tags: |
    dbal7/is601_final_project:latest
    dbal7/is601_final_project:${{ github.sha }}

cache-from: type=registry,ref=dbal7/is601_final_project:cache
```


## Installing dependencies and testing

### Install dependencies from requirements.txt
```bash
pip install -r requirements.txt
```

### Build docker image and run in background
```bash
docker compose up -d --build
```

### Test with pytest
```bash
pytest
```


## Add Feature: Hypotense Calculation

### Add code to calculation.py in app/models

**Import near the top for square root function**
```bash
import math
```

**Create the Operation class**
```bash
class Hypotenuse(Calculation):
    """
    Hypotenuse calculation subclass.
    
    Finds the hypotenuse of a right triangle with two positive 
    side lengths rounded to nearest hundredths.

    Examples:
        [3, 4] -> sqrt(3^2 + 4^2) = 5
        [2, 6] -> sqrt(2^2 + 6^2) = 6.32
    """
    __mapper_args__ = {"polymorphic_identity": "hypotenuse"}

    def get_result(self) -> float:
        """
        Calculate the hypotenuse of a right triangle
        
        Returns:
            float: The hypotenuse length
            
        Raises:
            ValueError: If inputs are not a list, if there are not exactly
                        two inputs, or if either input is zero or negative
        """
        if not isinstance(self.inputs, list):
            raise ValueError("Inputs must be a list of numbers.")
        
        if len(self.inputs) != 2:
            raise ValueError("Exactly two numbers are required to calculate hypotenuse.")

        if any(value <= 0 for value in self.inputs):
            raise ValueError("Side lengths must be greater than zero.")
        
        return round(math.sqrt(self.inputs[0] ** 2 + self.inputs[1] ** 2), 2)
```


**Add opeartion to existing calculation_classes**
```bash
calculation_classes = {
    'addition': Addition,
    'subtraction': Subtraction,
    'multiplication': Multiplication,
    'division': Division,
    'hypotenuse': Hypotenuse,
}
```

### Add code to calculation.py in app/schemas

**Add operation to CalculationType class**
```bash
ADDITION = "addition"
SUBTRACTION = "subtraction"
MULTIPLICATION = "multiplication"
DIVISION = "division"
HYPOTENUSE = "hypotenuse"
```

**Add opeartion to description in CalculationBase class**
```bash
description="Type of calculation (addition, subtraction, multiplication, division, hypotenuse)",
```

**Add code to validate Hypotenuse operation in validate_inputs function for CalculationBase**
```bash
    if self.type == CalculationType.HYPOTENUSE:
        if len(self.inputs) != 2:
            raise ValueError(
                "Exactly two numbers are required to calculate hypotenuse."
            )
        if any(x <= 0 for x in self.inputs):
            raise ValueError("Side lengths must be greater than zero.")

# return statement moved after HYPOTENUSE validation
return self
```

**Added hypotenuse example to json_schema_extra**
```bash
{"type": "hypotenuse", "inputs": [2, 6]}
```

### Add code to test_calculator.py unit test

**Add operation to import from app.operations**
```bash
from app.operations import add, subtract, multiply, divide, hypotenuse  # Import the calculator functions from the operations module
```

**Add unit test for valid inputs**
```bash
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
```

**Add unit test for invalid number of inputs**
```bash
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
```

**Add unit test for inputs with numbers less than or equal to 0**
```bash
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
```

### Add code to opertions/__init__.py in app directory

**Add hypotenuse function**
```bash
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
```

**Import math near top of code**
```bash
import math               # Import math to use sqrt function for hypotenuse opeartion
```

### Implement hypotenuse operation in dashboard tempalate

**Add Hypotenuse option on line 57**
```bash
<option value="hypotenuse">Hypotenuse</option>
```

**Add Hypotenuse number of input check**

After
```bash
const inputsVal = document.getElementById('calcInputs').value;
const inputs = inputsVal.split(',')
  .map(num => parseFloat(num.trim()))
  .filter(num => !isNaN(num));
```

Add
```bash
const calcType = document.getElementById('calcType').value;
```

After
```bash
if (inputs.length < 2) {
    showError('Please enter at least two valid numbers, separated by commas');
    
    // Highlight the input field with an error state
    const inputField = document.getElementById('calcInputs');
    inputField.classList.add('border-red-500');
    inputField.focus();
    
    // Remove error highlight after 3 seconds or when user types
    setTimeout(() => inputField.classList.remove('border-red-500'), 3000);
    inputField.addEventListener('input', () => inputField.classList.remove('border-red-500'), { once: true });
    
    return;
}
```

Add
```bash
if (calcType === 'hypotenuse') {
    if (inputs.length !== 2) {
        showError('Exactly two numbers are required to calculate hypotenuse.');
        return;
    }

    if (inputs.some(num => num <= 0)) {
        showError('Side lengths must be greater than zero.');
        return;
    }
}
```

**Simplify newCalc type**
```bash
const newCalc = {
    type: calcType,
    inputs
};
```

**Add dynamic placeholder for hypotenuse calculation inside DOMContentLoaded event listener**
```bash
const calcTypeSelect = document.getElementById('calcType');
const calcInputsField = document.getElementById('calcInputs');

calcTypeSelect.addEventListener('change', function() {
if (this.value === 'hypotenuse') {
    calcInputsField.placeholder = 'e.g. 3, 4';
} else {
    calcInputsField.placeholder = 'e.g. 5, 10, 15';
}
});
```

**Change input placeholder back after form reset**
```bash
calcInputsField.placeholder = 'e.g. 5, 10, 15';
```

### Implement hypotenuse operation in edit_calculation template

**Add hypotenuse case to switch statement in calculatePreview function**
```bash
case 'hypotenuse':
    if (inputs.length !== 2) {
        return 'Exactly two numbers required';
    }
    if (inputs.some(value => value <= 0)) {
        return 'Side lengths must be greater than zero';
    }
    result = Math.round(
        Math.sqrt(inputs[0] ** 2 + inputs[1] ** 2) * 100
    ) / 100;
    break;
```

**Add hypotenuse case to operator switch in updatePreview function**
```bash
case 'hypotenuse':
    operator = ',';
    break;
```

**Change input help when Hypotenuse calculation loads**
```bash
if (calc.type === 'hypotenuse') {
  calcInputsInput.placeholder = 'e.g. 3, 4';
  document.getElementById('inputHelp').textContent =
    'Enter exactly two positive side lengths separated by commas.';
}
```

**Add validator for Hypotenuse inputs**
```bash
if (calcTypeInput.value === 'hypotenuse') {
  if (newInputs.length !== 2) {
    showError('Exactly two numbers are required to calculate hypotenuse.');
    return;
  }

  if (newInputs.some(value => value <= 0)) {
    showError('Side lengths must be greater than zero.');
    return;
  }
}
```

### Implement hypotenuse operation in view_calculation template

**Add hypotenuse caste for operator type switch in createCalculationVisual function**
```bash
case 'hypotenuse':
    opreator = ',';
    break;
```

