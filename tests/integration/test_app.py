"""
Integration tests for the Flask application.
"""
import unittest
import json
from app import app


class TestApp(unittest.TestCase):
    """Test cases for the Flask application."""

    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        """Test home page loads properly."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)
        self.assertIn(b'Error Message Translator', response.data)

    def test_not_found(self):
        """Test 404 handling."""
        response = self.app.get('/nonexistent-route')
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main() 