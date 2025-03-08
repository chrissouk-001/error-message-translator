"""
Integration tests for the Flask application.
"""
import pytest

# No need for manual import path manipulation - that's handled in conftest.py

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