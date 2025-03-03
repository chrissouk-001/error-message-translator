"""
Unit tests for the translator module.
"""
import pytest
from app.translator import detect_language, translate_error


class TestLanguageDetection:
    """Tests for the detect_language function."""
    
    def test_python_detection(self, sample_python_error):
        """Test that Python errors are correctly detected."""
        assert detect_language(sample_python_error) == 'python'
    
    def test_javascript_detection(self, sample_js_error):
        """Test that JavaScript errors are correctly detected."""
        assert detect_language(sample_js_error) == 'javascript'
    
    def test_html_detection(self, sample_html_error):
        """Test that HTML errors are correctly detected."""
        assert detect_language(sample_html_error) == 'html'
    
    def test_css_detection(self, sample_css_error):
        """Test that CSS errors are correctly detected."""
        assert detect_language(sample_css_error) == 'css'
    
    def test_general_detection(self):
        """Test that unknown errors default to general."""
        assert detect_language("Some unknown error message") == 'general'


class TestErrorTranslation:
    """Tests for the translate_error function."""
    
    def test_empty_error_message(self):
        """Test handling of empty error messages."""
        result = translate_error("")
        assert result['language'] == 'unknown'
        assert result['title'] == 'No error message provided'
    
    def test_python_name_error_translation(self):
        """Test translation of a Python NameError."""
        error = "NameError: name 'undefined_variable' is not defined"
        result = translate_error(error)
        
        assert result['language'] == 'python'
        assert 'undefined_variable' in result['title']
        assert 'explanation' in result
        assert 'solution' in result
    
    def test_javascript_reference_error_translation(self):
        """Test translation of a JavaScript ReferenceError."""
        error = "ReferenceError: someVar is not defined"
        result = translate_error(error)
        
        assert result['language'] == 'javascript'
        assert 'someVar' in result['title']
        assert 'explanation' in result
        assert 'solution' in result
    
    def test_html_unclosed_tag_translation(self):
        """Test translation of an HTML unclosed tag error."""
        error = "Unclosed tag 'div'"
        result = translate_error(error)
        
        assert result['language'] == 'html'
        assert 'div' in result['title']
        assert 'explanation' in result
        assert 'solution' in result
    
    def test_css_unknown_property_translation(self):
        """Test translation of a CSS unknown property error."""
        error = "Unknown property: 'backgrond'"
        result = translate_error(error)
        
        assert result['language'] == 'css'
        assert 'backgrond' in result['title']
        assert 'explanation' in result
        assert 'solution' in result
    
    def test_unknown_error_translation(self):
        """Test translation of an unknown error."""
        error = "This is an error that doesn't match any pattern"
        result = translate_error(error)
        
        assert result['language'] == 'general'
        assert result['title'] == 'Unknown Error'
        assert 'explanation' in result
        assert 'solution' in result
    
    def test_specified_language(self):
        """Test translation with a specified language."""
        error = "This could be any error"
        result = translate_error(error, language='python')
        
        assert result['language'] == 'python'
        # Even though it won't match a pattern, the language should be respected
    
    def test_code_example_presence(self):
        """Test that code examples are included when available."""
        error = "NameError: name 'undefined_variable' is not defined"
        result = translate_error(error)
        
        assert 'code_example' in result
        assert result['code_example'] != ''  # Should not be empty for this error 