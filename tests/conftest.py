"""
Pytest configuration file.

This file contains fixtures and configuration for pytest.
"""
import sys
import os
import pytest
from pathlib import Path

# Add the project root to the Python path
project_root = str(Path(__file__).parent.parent.absolute())
if project_root not in sys.path:
    sys.path.insert(0, project_root)

@pytest.fixture
def app():
    """Create a Flask app instance for testing."""
    from app import app
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    """Create a test client for the Flask app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create a CLI test runner for the Flask app."""
    return app.test_cli_runner() 