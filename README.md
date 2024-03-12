# Mock Pipeline 🪈
### Environment 🌀 and Installation 👩🏽‍🔧👨🏽‍🔧
#### Prerequisite
+ Python 3.11.6 (We will use [pyenv](https://github.com/pyenv/pyenv#simple-python-version-management-pyenv) for Python Version Management but feel free to use any other tool)
+ Virtual environment (We will use the module venv from python but you can use any other tool)


For __MacOs__/__Linux__ users
```bash
# Sets the local Python version to 3.11.6 using pyenv
pyenv local 3.11.6 
# Create a Virtual Environment named .venv using venv
python -m venv .venv
# Activate the Virtual Environment
source .venv/bin/activate
# Install Libraries
pip install -r requirements.txt
```

For __Windows__ users with PowerShell CLI


```bash
# Sets the local Python version to 3.11.6 using pyenv
pyenv local 3.11.6 
# Create a Virtual Environment named .venv using venv
python -m venv .venv
# Activate the Virtual Environment
.venv\Scripts\Activate.ps1
# Install Libraries
pip install -r requirements.txt
```

For __Windows__ users with GIT-BASH CLI


```bash
# Sets the local Python version to 3.11.6 using pyenv
pyenv local 3.11.6 
# Create a Virtual Environment named .venv using venv
python -m venv .venv
# Activate the Virtual Environment
source .venv/Scripts/activate
# Install Libraries
pip install -r requirements.txt
```