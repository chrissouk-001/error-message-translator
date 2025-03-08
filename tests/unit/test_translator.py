"""
Unit tests for the translator module.
"""
import pytest
import sys
import os

# Add parent directory to path to allow imports when running tests directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

try:
    from app.translator import translate_error, detect_language
except ImportError as e:
    print(f"Import error: {e}")
    print("Current path:", sys.path)
    raise

def test_detect_language_python():
    """Test detection of Python errors."""
    error_msg = "SyntaxError: invalid syntax"
    assert detect_language(error_msg) == "python"

def test_detect_language_javascript():
    """Test detection of JavaScript errors."""
    error_msg = "Uncaught ReferenceError: foo is not defined"
    assert detect_language(error_msg) == "javascript"

def test_detect_language_html():
    """Test detection of HTML errors."""
    error_msg = "Unclosed tag 'div'"
    assert detect_language(error_msg) == "html"

def test_detect_language_css():
    """Test detection of CSS errors."""
    error_msg = "Unknown property: 'colour'"
    assert detect_language(error_msg) == "css"

def test_detect_language_general():
    """Test fallback to general for unknown errors."""
    error_msg = "Something went wrong"
    assert detect_language(error_msg) == "general"

def test_translate_error_syntax():
    """Test translation of syntax errors."""
    error_msg = "SyntaxError: invalid syntax"
    result = translate_error(error_msg, "python")
    assert "title" in result
    assert "explanation" in result
    assert "solution" in result
    assert result["language"] == "python"

def test_translate_error_empty():
    """Test translation of empty error message."""
    error_msg = ""
    result = translate_error(error_msg)
    assert result["title"] == "No error message provided"

if __name__ == "__main__":
    pytest.main() 