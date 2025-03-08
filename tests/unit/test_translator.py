"""
Unit tests for the translator module.
"""
import unittest
from app.translator import translate_error, detect_language


class TestTranslator(unittest.TestCase):
    """Test cases for the translator module."""

    def test_detect_language_python(self):
        """Test detection of Python errors."""
        error_msg = "SyntaxError: invalid syntax"
        self.assertEqual(detect_language(error_msg), "python")

    def test_detect_language_javascript(self):
        """Test detection of JavaScript errors."""
        error_msg = "Uncaught ReferenceError: foo is not defined"
        self.assertEqual(detect_language(error_msg), "javascript")

    def test_detect_language_html(self):
        """Test detection of HTML errors."""
        error_msg = "Unclosed tag 'div'"
        self.assertEqual(detect_language(error_msg), "html")

    def test_detect_language_css(self):
        """Test detection of CSS errors."""
        error_msg = "Unknown property: 'colour'"
        self.assertEqual(detect_language(error_msg), "css")

    def test_detect_language_general(self):
        """Test fallback to general for unknown errors."""
        error_msg = "Something went wrong"
        self.assertEqual(detect_language(error_msg), "general")

    def test_translate_error_syntax(self):
        """Test translation of syntax errors."""
        error_msg = "SyntaxError: invalid syntax"
        result = translate_error(error_msg, "python")
        self.assertIn("title", result)
        self.assertIn("explanation", result)
        self.assertIn("solution", result)
        self.assertEqual(result["language"], "python")

    def test_translate_error_empty(self):
        """Test translation of empty error message."""
        error_msg = ""
        result = translate_error(error_msg)
        self.assertEqual(result["title"], "No error message provided")


if __name__ == "__main__":
    unittest.main() 