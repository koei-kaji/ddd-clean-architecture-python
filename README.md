# ddd-clean-architecture-python

DDD example with Clean Architechture in Python.  

## Getting Started

### Prerequisites

- [pyenv]: Python Version Management
- [poetry]: Dependency Management for Python
- make: Build tool

### Installing

```bash
# install python 3.10.5 with pyenv
$ pyenv install 3.10.5

# install dependencies
$ poetry install

# [Optional] activate virtual environment
$ source .venv/bin/activate
```

## How to run

```bash
$ make run
# Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Built With

- [pydantic]: Data validation and settings management using Python type hints
- [injector]: Python dependency injection framework
- [fastapi]: A modern, fast (high-performance), web framework for building APIs with Python

### Development only

- [pytest]
- [mypy]
- [isort]
- [black]
- [pytest-cov]
- [pylint]
- [coverage-badge]

[pyenv]: https://github.com/pyenv/pyenv
[poetry]: https://github.com/python-poetry/poetry
[pydantic]: https://github.com/samuelcolvin/pydantic
[injector]: https://github.com/alecthomas/injector
[fastapi]: https://github.com/tiangolo/fastapi
[pytest]: https://github.com/pytest-dev/pytest
[mypy]: https://github.com/python/mypy
[isort]: https://github.com/PyCQA/isort
[black]: https://github.com/psf/black
[pytest-cov]: https://github.com/pytest-dev/pytest-cov
[pylint]: https://github.com/PyCQA/pylint
[coverage-badge]: https://github.com/dbrgn/coverage-badge
