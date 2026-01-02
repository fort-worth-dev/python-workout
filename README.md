# Python Workout - Exercise Solutions Portfolio

> Professional implementations of exercises from "Python Workout" by Reuven M. Lerner

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## About This Project

This repository contains my solutions to exercises from the book ["Python Workout"](https://www.manning.com/books/python-workout) by Reuven M. Lerner. Each exercise is implemented with:

- Clean, well-documented code following PEP 8
- Comprehensive test coverage using pytest
- Type hints for better code clarity
- Professional project structure

## Project Structure

```
src/python_workout/      # Source code organized by chapter
tests/                   # Test suite mirroring source structure
docs/                    # Additional documentation
```

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/python-workout.git
cd python-workout

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```

### Running Exercises

```bash
# Run a specific exercise
python -m python_workout.ch01_numeric_types.ex01_number_guessing_game

# Run with Python's -i flag for interactive exploration
python -i -m python_workout.ch02_strings.ex05_pig_latin
```

### Running Tests

```bash
# Run all tests
pytest

# Run tests for a specific chapter
pytest tests/ch01_numeric_types/

# Run tests with coverage
pytest --cov=python_workout --cov-report=html

# Run tests in parallel (faster)
pytest -n auto
```

### Code Quality

```bash
# Format code
ruff format .

# Lint code
ruff check .

# Type check
mypy src/
```

## Chapters

| Chapter | Topic | Exercises | Status |
|---------|-------|-----------|--------|
| 1 | [Numeric Types](docs/chapters/01_numeric_types.md) | TBD | 📝 Planned |
| 2 | [Strings](docs/chapters/02_strings.md) | TBD | 📝 Planned |
| 3 | [Lists and Tuples](docs/chapters/03_lists_tuples.md) | TBD | 📝 Planned |
| 4 | [Dictionaries and Sets](docs/chapters/04_dicts_sets.md) | TBD | 📝 Planned |
| 5 | [Files](docs/chapters/05_files.md) | TBD | 📝 Planned |
| 6 | [Functions](docs/chapters/06_functions.md) | TBD | 📝 Planned |
| 7 | [Functional Programming](docs/chapters/07_functional.md) | TBD | 📝 Planned |
| 8 | [Modules and Packages](docs/chapters/08_modules_packages.md) | TBD | 📝 Planned |
| 9 | [Objects](docs/chapters/09_objects.md) | TBD | 📝 Planned |
| 10 | [Iterators and Generators](docs/chapters/10_iterators_generators.md) | TBD | 📝 Planned |

## Development Workflow

1. **Create exercise file** in appropriate chapter directory
2. **Write docstring** with problem description and learning objectives
3. **Implement solution** with type hints and comments
4. **Write tests** achieving >90% coverage
5. **Run quality checks** (tests, linting, type checking)
6. **Document** in chapter README

## Technologies Used

- **Python 3.9+**: Modern Python features
- **pytest**: Testing framework with fixtures and parameterization
- **ruff**: Fast, modern linting and formatting
- **mypy**: Static type checking
- **GitHub Actions**: CI/CD pipeline

## Learning Highlights

- Clean code principles and PEP 8 compliance
- Test-driven development practices
- Type hints and static analysis
- Modern Python packaging (src-layout, pyproject.toml)
- CI/CD with GitHub Actions

## About the Book

"Python Workout" by Reuven M. Lerner presents 50 carefully selected exercises covering key Python concepts. Each exercise includes solutions and additional challenges to deepen understanding.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Reuven M. Lerner for the excellent "Python Workout" book
- The Python community for maintaining excellent documentation and tools

## Contact

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

---

*This is a portfolio project showcasing Python development skills, testing practices, and professional project organization.*
