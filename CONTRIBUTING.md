# Contributing to Error Message Translator

> **⚠️ Research Notice**: This project is for research purposes to evaluate how Large Language Models (LLMs) perform on software development projects. Everyone is welcome to contribute to this repository as part of this research test.

Thank you for considering contributing to Error Message Translator! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md).

## How Can I Contribute?

### Reporting Bugs

Before submitting a bug report:
- Check the existing issues to see if the problem has already been reported
- If you're unable to find an open issue addressing the problem, open a new one

When filing an issue, include as much detail as possible:
- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior vs. actual behavior
- Screenshots if applicable
- Your environment (OS, browser, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:
- Use a clear and descriptive title
- Provide a detailed description of the suggested enhancement
- Explain why this enhancement would be useful

### Adding New Error Patterns

One of the most valuable ways to contribute is by adding new error patterns to our database:

1. Locate the appropriate pattern file in `app/data/error_patterns.py`
2. Follow the existing structure to add a new pattern:
   ```python
   {
       'regex': r'YourRegexPattern',
       'title': 'Error Title',
       'explanation': 'Beginner-friendly explanation',
       'solution': 'How to fix the error',
       'code_example': '''
   # Example code showing the fix
       ''',
       'related_errors': ['Related', 'Errors']
   }
   ```
3. Add tests for your new pattern in the appropriate test file

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the tests to ensure they pass (`./run_tests.sh`)
5. Commit your changes with a descriptive commit message
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

1. Clone your fork of the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements-test.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```

## Testing

- Run all tests: `./run_tests.sh`
- Run unit tests only: `./run_tests.sh --unit`
- Run integration tests only: `./run_tests.sh --integration`
- Run with coverage: `./run_tests.sh --coverage`

## Styleguides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Python Styleguide

- Follow PEP 8
- Use meaningful variable names
- Include docstrings for all functions, classes, and modules
- Write tests for new features

### Documentation Styleguide

- Use Markdown for documentation
- Keep language simple and beginner-friendly
- Include code examples where appropriate

## Additional Notes

### Issue and Pull Request Labels

- `bug`: Bug reports
- `enhancement`: Feature requests
- `documentation`: Documentation improvements
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention is needed

---

Thank you for contributing to Error Message Translator! 