# Python Notebook and Package Demonstration
This project demonstrates how you can develop a Python package
together with Jupyter Notebooks. This is a typical application for a
research project where the problem is initally explored in a
notebook. Reusable functions of the notebook are subsequently moved to
a Python package.


## Installation
1. Create a virtual environment and activate it: 
```bash
python3 -m venv venv
. venv/bin/activate
```
2. Install the requirements 
```bash
python3 -m pip install -r requirements.txt
```
3. Install the package
```bash
python3 -m pip install -e .
```
