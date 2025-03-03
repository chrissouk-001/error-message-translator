"""
Test configuration file for the Error Message Translator.

This file contains fixtures and configuration for pytest.
"""
import os
import sys
import pytest
from flask import Flask

# Add the parent directory to sys.path to make app imports work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import translator
from app.data import error_patterns


@pytest.fixture
def flask_app():
    """Create a Flask app for testing."""
    # Import the app directly from app.py rather than the package
    import sys
    import importlib.util
    
    # Path to the app.py file
    app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app.py'))
    
    # Import the module dynamically
    spec = importlib.util.spec_from_file_location("app_module", app_path)
    app_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app_module)
    
    # Get the app object
    app = app_module.app
    
    # Configure the app for testing
    app.config.update({
        'TESTING': True,
        'DEBUG': True,
    })
    
    yield app


@pytest.fixture
def client(flask_app):
    """Create a test client for the app."""
    return flask_app.test_client()


@pytest.fixture
def live_server(flask_app):
    """Create a live Flask server for Selenium tests."""
    import multiprocessing
    import socket
    import time
    from werkzeug.serving import make_server
    
    # Find an available port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    
    # Configure the app
    flask_app.config.update({
        'TESTING': True,
        'LIVESERVER_PORT': port
    })
    
    # Start the server
    server = make_server('localhost', port, flask_app)
    server_process = multiprocessing.Process(target=server.serve_forever)
    server_process.start()
    
    # Give the server a moment to ensure it's started
    time.sleep(1)
    
    # Create a live server object with methods needed by our tests
    class LiveServer:
        def url(self, path=''):
            return f'http://localhost:{port}{path}'
        
        def start(self):
            pass  # Already started
            
    yield LiveServer()
    
    # Cleanup
    server_process.terminate()
    server_process.join()


@pytest.fixture
def selenium(pytestconfig):
    """Selenium WebDriver fixture for browser tests."""
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    
    # Set up Chrome options for headless testing
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    
    # Create WebDriver
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    
    yield driver
    
    # Teardown
    driver.quit()


@pytest.fixture
def sample_python_error():
    """Sample Python error message for testing."""
    return "NameError: name 'undefined_variable' is not defined"


@pytest.fixture
def sample_js_error():
    """Sample JavaScript error message for testing."""
    return "Uncaught TypeError: Cannot read property 'length' of undefined"


@pytest.fixture
def sample_html_error():
    """Sample HTML error message for testing."""
    return "Unclosed tag 'div'"


@pytest.fixture
def sample_css_error():
    """Sample CSS error message for testing."""
    return "Unknown property: 'backgrond'"


@pytest.fixture
def python_patterns():
    """Access to Python error patterns for testing."""
    return error_patterns.PYTHON_PATTERNS


@pytest.fixture
def js_patterns():
    """Access to JavaScript error patterns for testing."""
    return error_patterns.JAVASCRIPT_PATTERNS


@pytest.fixture
def html_patterns():
    """Access to HTML error patterns for testing."""
    return error_patterns.HTML_PATTERNS


@pytest.fixture
def css_patterns():
    """Access to CSS error patterns for testing."""
    return error_patterns.CSS_PATTERNS 