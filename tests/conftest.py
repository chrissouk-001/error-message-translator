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

# Silence deprecation warnings during testing
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=PendingDeprecationWarning)


@pytest.fixture(scope="session")
def app():
    """Create a Flask app instance for testing."""
    # Import inside function to avoid import issues
    from app import app

    # Configure the app for testing
    app.config.update(
        {
            "TESTING": True,
            "SERVER_NAME": "localhost.localdomain",
            "DEBUG": False,
            "WTF_CSRF_ENABLED": False,
        }
    )

    # Create app context for testing
    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        client.environ_base["HTTP_ACCEPT"] = "text/html"
        yield client


@pytest.fixture
def runner(app):
    """Create a CLI test runner for the Flask app."""
    return app.test_cli_runner()
