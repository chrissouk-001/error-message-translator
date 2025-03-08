.PHONY: help setup test lint format clean run

# Default target executed when no arguments are given to make.
help:
	@echo "Available commands:"
	@echo "  setup    - Install dependencies"
	@echo "  test     - Run tests"
	@echo "  lint     - Run linting checks"
	@echo "  format   - Format code with Black"
	@echo "  clean    - Remove Python cache files"
	@echo "  run      - Run the Flask application"

setup:
	pip install -r requirements.txt

test:
	pytest

lint:
	flake8 app tests
	black --check app tests

format:
	black app tests

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +

run:
	python app.py 