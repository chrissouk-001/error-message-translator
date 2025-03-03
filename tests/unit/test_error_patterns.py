"""
Unit tests for the error_patterns module.
"""
import re
import pytest
from app.data.error_patterns import (
    PYTHON_PATTERNS,
    JAVASCRIPT_PATTERNS,
    HTML_PATTERNS,
    CSS_PATTERNS,
    GENERAL_PATTERNS
)


def validate_pattern(pattern):
    """Helper function to validate a pattern structure."""
    # Check required fields
    assert 'regex' in pattern, "Pattern missing 'regex' field"
    assert 'title' in pattern, "Pattern missing 'title' field"
    assert 'explanation' in pattern, "Pattern missing 'explanation' field"
    assert 'solution' in pattern, "Pattern missing 'solution' field"
    
    # Check regex compilation
    try:
        compiled_regex = re.compile(pattern['regex'])
    except re.error:
        pytest.fail(f"Invalid regex pattern: {pattern['regex']}")
    
    # Check for placeholder consistency
    placeholders = re.findall(r'\{\{\$(\d+)\}\}', pattern['title'] + pattern['explanation'] + pattern['solution'])
    if placeholders:
        # Get unique placeholder numbers
        placeholder_nums = set(map(int, placeholders))
        # Check that placeholders are sequential starting from 1
        assert min(placeholder_nums) == 1, "Placeholder numbering should start from 1"
        
        # Count the capture groups in the regex
        # We need to count the number of capturing groups in the regex pattern
        num_groups = compiled_regex.groups
        assert max(placeholder_nums) <= num_groups, \
            f"More placeholders than regex capture groups. Found {max(placeholder_nums)} placeholders but only {num_groups} capture groups"


class TestPatternStructure:
    """Tests for the structure of error patterns."""
    
    def test_python_patterns(self, python_patterns):
        """Test that Python patterns are correctly structured."""
        assert len(python_patterns) > 0, "No Python patterns defined"
        for pattern in python_patterns:
            validate_pattern(pattern)
    
    def test_javascript_patterns(self, js_patterns):
        """Test that JavaScript patterns are correctly structured."""
        assert len(js_patterns) > 0, "No JavaScript patterns defined"
        for pattern in js_patterns:
            validate_pattern(pattern)
    
    def test_html_patterns(self, html_patterns):
        """Test that HTML patterns are correctly structured."""
        assert len(html_patterns) > 0, "No HTML patterns defined"
        for pattern in html_patterns:
            validate_pattern(pattern)
    
    def test_css_patterns(self, css_patterns):
        """Test that CSS patterns are correctly structured."""
        assert len(css_patterns) > 0, "No CSS patterns defined"
        for pattern in css_patterns:
            validate_pattern(pattern)


class TestPatternMatching:
    """Tests for matching error patterns against error messages."""
    
    def test_python_name_error_match(self, sample_python_error):
        """Test matching a Python NameError."""
        matched = False
        for pattern in PYTHON_PATTERNS:
            match = re.search(pattern['regex'], sample_python_error)
            if match:
                matched = True
                break
        
        assert matched, "Python NameError pattern should match sample error"
    
    def test_javascript_type_error_match(self, sample_js_error):
        """Test matching a JavaScript TypeError."""
        matched = False
        for pattern in JAVASCRIPT_PATTERNS:
            match = re.search(pattern['regex'], sample_js_error)
            if match:
                matched = True
                break
        
        assert matched, "JavaScript TypeError pattern should match sample error"
    
    def test_html_unclosed_tag_match(self, sample_html_error):
        """Test matching an HTML unclosed tag error."""
        matched = False
        for pattern in HTML_PATTERNS:
            match = re.search(pattern['regex'], sample_html_error)
            if match:
                matched = True
                break
        
        assert matched, "HTML unclosed tag pattern should match sample error"
    
    def test_css_unknown_property_match(self, sample_css_error):
        """Test matching a CSS unknown property error."""
        matched = False
        for pattern in CSS_PATTERNS:
            match = re.search(pattern['regex'], sample_css_error)
            if match:
                matched = True
                break
        
        assert matched, "CSS unknown property pattern should match sample error" 