# How to Contribute

> **Research Notice**: This project is for research purposes to evaluate how Large Language Models (LLMs) perform on software development projects. Everyone is welcome to contribute to this repository as part of this research test.

This is a research project testing how LLMs work with code. We welcome all kinds of contributions!

## Quick Start

1. Fork the repo
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/error-message-translator.git`
3. Create a branch for your changes: `git checkout -b your-feature`
4. Make changes
5. Test if possible: `./run_tests.sh`
6. Push your branch: `git push origin your-feature`
7. Open a Pull Request

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
git clone https://github.com/YOUR_USERNAME/error-message-translator.git
cd error-message-translator

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements-test.txt

# Run the app
python app.py
```

## Running Tests
```bash
./run_tests.sh
```

Thanks for contributing to this research project! 