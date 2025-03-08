"""
Unit tests for the translator module.
"""
import pytest

# No need for manual import path manipulation - that's handled in conftest.py
from app.translator import translate_error, detect_language


@pytest.mark.unit
def test_detect_language_python():
    """Test detection of Python errors."""
    error_msg = "SyntaxError: invalid syntax"
    assert detect_language(error_msg) == "python"


@pytest.mark.unit
def test_detect_language_javascript():
    """Test detection of JavaScript errors."""
    error_msg = "Uncaught ReferenceError: foo is not defined"
    assert detect_language(error_msg) == "javascript"


@pytest.mark.unit
def test_detect_language_html():
    """Test detection of HTML errors."""
    error_msg = "Unclosed tag 'div'"
    assert detect_language(error_msg) == "html"


@pytest.mark.unit
def test_detect_language_css():
    """Test detection of CSS errors."""
    error_msg = "Unknown property: 'colour'"
    assert detect_language(error_msg) == "css"


@pytest.mark.unit
def test_detect_language_general():
    """Test fallback to general for unknown errors."""
    error_msg = "Something went wrong"
    assert detect_language(error_msg) == "general"


@pytest.mark.unit
def test_translate_error_syntax():
    """Test translation of syntax errors."""
    error_msg = "SyntaxError: invalid syntax"
    result = translate_error(error_msg, "python")
    assert "title" in result
    assert "explanation" in result
    assert "solution" in result
    assert result["language"] == "python"


@pytest.mark.unit
def test_translate_error_empty():
    """Test translation of empty error message."""
    error_msg = ""
    result = translate_error(error_msg)
    assert result["title"] == "No error message provided"


if __name__ == "__main__":
    pytest.main()
