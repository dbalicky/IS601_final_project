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