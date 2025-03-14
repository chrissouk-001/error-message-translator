# How to Contribute

> **Research Notice**: This project is for research purposes to evaluate how Large Language Models (LLMs) perform on software development projects. Everyone is welcome to contribute to this repository as part of this research test.

This is a research project testing how LLMs work with code. We welcome all kinds of contributions!

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/chrissouk-001/error-message-translator.git
   ```
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b your-feature
   ```
3. Implement your changes.
4. Run tests to ensure everything works:
   ```bash
   pytest
   ```
5. Submit a pull request with a clear description of your changes.

## What Can You Contribute?

* Code fixes or improvements
* New error patterns in `app/data/error_patterns.py`
* UI improvements
* Documentation updates
* Bug reports
* Feature ideas

## Setting Up Locally

```bash
# Clone and set up
git clone https://github.com/chrissouk-001/error-message-translator.git
cd error-message-translator

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e ".[dev]"  # For development dependencies

# Run the app
python app.py
```

## Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app
```

Thanks for contributing to this research project! 