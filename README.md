# Modern Python Template

A production-ready Python CLI template with modern packaging and development practices.

## Features

- Poetry-based dependency management
- Click CLI framework
- pytest test suite
- Type checking with mypy
- Code formatting with Black
- Linting with flake8
- pipx installable
- Unix-style man page help system

## Installation

```bash
pipx install modern-python-template
```

For development installation:
```bash
git clone https://github.com/yourusername/modern-python-template.git
cd modern-python-template
poetry install
```

## Usage

```bash
modern-python-template --help
modern-python-template process input.txt --output output.csv
modern-python-template config
```

## Development Commands

Run tests:
```bash
poetry run pytest
```

Format code:
```bash
poetry run black .
```

Check types:
```bash
poetry run mypy .
```

## Packaging

Build package:
```bash
poetry build
```

Install locally with pipx:
```bash
pipx install dist/modern_python_template-*.whl