# Quick-Calc: Simple Calculator Application

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![pytest](https://img.shields.io/badge/tested%20with-pytest-green.svg)](https://pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Project Description

Quick-Calc is a lightweight command-line calculator application demonstrating professional software engineering practices. It implements the four basic arithmetic operations (addition, subtraction, multiplication, and division) with robust error handling, comprehensive testing, and clean, maintainable code.

The application is designed to showcase:
- **Clean Code Architecture**: Separation of concerns between calculator logic and user interface
- **Professional Testing**: Multi-layered testing strategy with unit and integration tests
- **Error Handling**: Graceful handling of edge cases (e.g., division by zero)
- **Version Control**: Meaningful commit history demonstrating realistic development workflow
- **Documentation**: Complete technical documentation and testing strategy

## Features

- ✅ **Addition**: Correctly adds two numbers
- ✅ **Subtraction**: Correctly subtracts two numbers
- ✅ **Multiplication**: Correctly multiplies two numbers
- ✅ **Division**: Correctly divides two numbers with zero-division error handling
- ✅ **Clear Function**: Resets calculator state to zero
- ✅ **Comprehensive Testing**: 19 tests covering all operations and edge cases

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/lepembejeremie/swe-testing-assignment.git
cd swe-testing-assignment
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install pytest pytest-cov
```

### Step 4: Run the Application

```bash
python app.py
```

Follow the interactive menu to perform calculations.

## How to Run Tests

### Run All Tests

```bash
pytest test_calculator.py -v
```

### Run with Coverage Report

```bash
pytest test_calculator.py --cov=calculator --cov-report=html
```

This generates an HTML coverage report in the `htmlcov/` directory.

### Run Specific Test Class

```bash
pytest test_calculator.py::TestAddition -v
```

### Run with Detailed Output

```bash
pytest test_calculator.py -vv --tb=short
```

## Testing Framework Research

### Comparison: pytest vs unittest

#### **pytest**

**Pros:**
- **Simpler syntax**: Tests are plain Python functions with `assert` statements, making code more readable
- **Better fixture system**: Pytest fixtures are more flexible and composable than unittest's setUp/tearDown methods
- **Parametrization**: Built-in `@pytest.mark.parametrize` allows running the same test with different inputs
- **Powerful plugins ecosystem**: Rich ecosystem with plugins for coverage, parallel execution, HTML reports, etc.
- **Less boilerplate**: No need for test classes inheriting from `TestCase`; tests can be functions or methods
- **Better error messages**: Assertion introspection provides detailed failure information automatically
- **Easier mocking**: Integrates seamlessly with `unittest.mock` and pytest-mock plugins

**Cons:**
- Slightly steeper learning curve for advanced features
- Requires separate package installation (not in Python standard library)
- Configuration file (pytest.ini or pyproject.toml) may be needed for complex setups

#### **unittest** (Python Standard Library)

**Pros:**
- **Built-in**: No external dependencies required, comes with Python
- **Familiar to Java developers**: Similar structure to JUnit framework
- **Well-established**: Mature framework with extensive documentation
- **Standard approach**: Consistent with enterprise Java testing patterns

**Cons:**
- **Verbose syntax**: Tests require classes inheriting from `TestCase` with verbose `self.assertEqual()` calls
- **Poor error messages**: Assertion failures don't provide as much context
- **Setup/teardown complexity**: `setUp()` and `tearDown()` methods are less flexible than pytest fixtures
- **No parametrization support**: Difficult to run same test with multiple inputs
- **More boilerplate**: Requires more code to write equivalent tests
- **Limited plugin ecosystem**: Fewer third-party extensions compared to pytest

### Decision: Why pytest Was Chosen

For this project, **pytest** was selected as the testing framework for the following reasons:

1. **Code Clarity**: Pytest's simpler assertion syntax (`assert result == 8`) is more readable than unittest's verbose syntax (`self.assertEqual(result, 8)`)

2. **Test Coverage**: The `pytest-cov` plugin makes generating coverage reports straightforward, supporting the requirement to demonstrate testing comprehensiveness

3. **Scalability**: As the test suite grows, pytest's fixture system and parametrization features provide better maintainability

4. **Industry Standard**: Pytest is the de facto standard in modern Python development, reflected in its adoption across popular projects and frameworks

5. **Rich Output**: Pytest provides detailed failure information and works seamlessly with CI/CD pipelines

6. **Learning Value**: Using pytest demonstrates awareness of modern Python testing practices, aligning with the advanced software engineering curriculum

## Project Structure

```
swe-testing-assignment/
├── calculator.py          # Core Calculator class and logic
├── app.py                 # Command-line interface
├── test_calculator.py     # Unit and integration tests
├── TESTING.md            # Testing strategy documentation
├── README.md             # This file
└── .gitignore            # Git ignore rules for Python projects
```

## Test Results

All 19 tests pass successfully. See [TESTING.md](TESTING.md) for detailed testing strategy and results summary.

```
========================= 19 passed in 0.25s ==========================
```

## Commit History

The development process is documented through meaningful commits:

1. `feat: initialize project with gitignore and basic structure`
2. `feat: implement Calculator class with four operations`
3. `feat: add comprehensive unit tests for all operations`
4. `feat: add integration tests for complete workflows`
5. `feat: implement CLI application and add documentation`

See full commit history with `git log --oneline`.

## Release

**Version 1.0.0** - Released on [Date]

Initial production-ready release of Quick-Calc with complete functionality, comprehensive testing, and professional documentation.

## Author

Developed as part of Advanced Software Engineering Course - Assignment 3

## License

MIT License - See LICENSE file for details

## References

- [pytest Official Documentation](https://docs.pytest.org/)
- [Python unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Semantic Versioning](https://semver.org/)
