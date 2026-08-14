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