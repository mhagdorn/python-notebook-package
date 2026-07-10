# Python Notebook and Package Demonstration
This project demonstrates how you can develop a Python package
together with Jupyter Notebooks. This is a typical application for a
research project where the problem is initally explored in a
notebook. Reusable functions of the notebook are subsequently moved to
a Python package.

This skeleton package contains a simple package computing Fibonacci
numbers, associated tests, a notebook that can be rendered using
quarto and sphinx documentation.

[![DOI](https://zenodo.org/badge/1296427036.svg)](https://doi.org/10.5281/zenodo.21297691)

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

## Running the Tests
```bash
python3 -m pytest
```

## Producing the Sphinx Documentation
```bash
sphinx-build -b html doc public
```

## Rendering the Document
If you have [quarto](https://quarto.org/) installed you can render the
notebook to pdf and html using
```bash
quarto render notebooks/demo.ipynb --to html,pdf --output-dir ../public
```
The output files will be stored in the `public` directory.
