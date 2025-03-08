"""
Integration tests for the Flask application.
"""
import pytest
import sys
import os

# Add parent directory to path to allow imports when running tests directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

try:
    from app import app
except ImportError as e:
    print(f"Import error: {e}")
    print("Current path:", sys.path)
    raise

def test_home_page(client):
    """Test home page loads properly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data
    assert b'Error Message Translator' in response.data

def test_not_found(client):
    """Test 404 handling."""
    response = client.get('/nonexistent-route')
    assert response.status_code == 404

if __name__ == "__main__":
    pytest.main() 