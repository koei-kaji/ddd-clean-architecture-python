# ddd-clean-architecture-python

Domain Driven Design (DDD) example with Clean Architecture in Python.
The subject is a simple TODO application.

## Code Details

- [Directory Structure](./docs/directory_structure.md)
- [Sequence Diagrams](./docs/sequence_diagrams.md)
- [Domain Models](./docs/domain_models.md)
- [IoC Container](./docs/ioc_container.md)
- CQRS

## Getting Started

### Prerequisites

- [rye]: An Experimental Package Management Solution for Python
- make: Build tool

### Installation

```bash
# install
$ rye sync

# activate virtual environment
$ . .venv/bin/activate
```

## How to run

```bash
$ make run
# Uvicorn running on http://127.0.0.1:8000/docs (Press CTRL+C to quit)
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

[rye]: https://rye-up.com/
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
