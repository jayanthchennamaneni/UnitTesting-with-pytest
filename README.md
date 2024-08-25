# UnitTesting-with-pytest

This is a simple Python project that implements a `ShoppingCart` class. The project includes unit tests written with Pytest to ensure the functionality of the shopping cart.

UnitTesting: Automated tests(usually functions) that we can write and run to check if our source code is working as intended.


## Getting Started

### Prerequisites

- Python 3.7+
- `pip` (Python package installer)
- `virtualenv` (optional, but recommended)

## Project Structure

    UnitTesting-with-pytest/
    ├── src/
    │   └── shopping_cart.py        # Implementation of the ShoppingCart class
    ├── tests/
    │   └── test_shopping_cart.py   # Unit tests for the ShoppingCart class
    ├── .gitignore                  # Git ignore file to exclude unnecessary files from version control
    ├── README.md                   # Project documentation
    └── requirements.txt            # List of Python dependencies


### Setup

1. **Clone the repository**:

   ```bash
   git clone <https://github.com/jayanthchennamaneni/UnitTesting-with-pytest.git>
   cd UnitTesting-with-pytest
   ```

2. **Create a virtual environment**:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Running the Tests**:
To run the unit tests, use the following command:

    ```bash
    pytest tests/
    ```
This command will discover and execute all the test cases in the tests/ directory.