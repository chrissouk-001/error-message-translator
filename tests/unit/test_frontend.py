"""
Unit tests for frontend functionality.
"""

import os
import sys
from app.static.js.main import getPrismLanguageClass, createShareButton, shareTranslation, copyShareLinkToClipboard

def test_html_structure():
    """Test that the HTML file has the required structure."""
    from pathlib import Path
    html_path = Path("app/templates/index.html")
    
    content = html_path.read_text()
    
    # Check for important elements
    elements = [
        '<div class="container">',
        '<header>',
        '<textarea id="error-input"',
        '<select id="language-select">',
        'id="translate-btn"',
        'class="translation-section" id="translation-result"',
        'id="error-title"',
        'class="language-badge" id="language-badge"'
    ]
    
    for element in elements:
        assert element in content, f"{element} missing from HTML"

def test_css_structure():
    """Test that CSS file has the required sections."""
    from pathlib import Path
    css_path = Path("app/static/css/styles.css")
    
    content = css_path.read_text()
    
    sections = [
        ".input-section",
        ".translation-section", 
        ".language-badge",
        ".original-error",
        ".code-container"
    ]
    
    for section in sections:
        assert section in content, f"{section} styles missing"


def test_css_styles_exist():
    """Test that required CSS classes exist in the styles.css file."""
    from pathlib import Path
    css_path = Path("app/static/css/styles.css")
    
    css_content = css_path.read_text()
    
    # Check for important class definitions
    assert ".input-section" in css_content
    assert ".translation-section" in css_content
    assert ".share-btn" in css_content
    
    # These class names might be different in the actual CSS
    # Let's check for elements that should definitely exist
    assert "header" in css_content
    assert "footer" in css_content
    assert "button" in css_content


def test_prism_language_mapping():
    """Test that the Prism language class mapping function works correctly."""
    assert getPrismLanguageClass('python') == 'language-python'
    assert getPrismLanguageClass('javascript') == 'language-javascript'
    assert getPrismLanguageClass('html') == 'language-markup'
    assert getPrismLanguageClass('css') == 'language-css'
    assert getPrismLanguageClass('unknown') == 'language-none'


def test_share_button_creation():
    """Test that the share button creation function works correctly."""
    # Mock DOM elements
    class MockElement:
        def __init__(self):
            self.children = []
            self.className = ""
            self.style = {}
            self.innerHTML = ""
            self.title = ""
            self.events = {}
        
        def appendChild(self, child):
            self.children.append(child)
            return child
        
        def insertBefore(self, new_child, ref_child):
            self.children.insert(self.children.index(ref_child) if ref_child in self.children else 0, new_child)
            return new_child
        
        def addEventListener(self, event, handler):
            self.events[event] = handler
    
    # Mock document.createElement and document.querySelector
    class MockDocument:
        def createElement(self, tag):
            return MockElement()
        
        def querySelector(self, selector):
            if selector == '.translation-header':
                header = MockElement()
                badge = MockElement()
                header.children.append(badge)
                return header
            return None
    
    # Mock document.getElementById
    def getElementById(id):
        if id == 'language-badge':
            badge = MockElement()
            return badge
        return None
    
    # Setup mock environment
    document = MockDocument()
    document.getElementById = getElementById
    
    # Call function with mock
    header = document.querySelector('.translation-header')
    createShareButton(document, header)
    
    # Assertions
    assert len(header.children) >= 1
    share_container = [child for child in header.children if isinstance(child, MockElement) and child.className == 'share-container']
    assert len(share_container) == 1
    
    share_container = share_container[0]
    assert share_container.style.get('marginLeft') == 'auto'
    
    share_buttons = [child for child in share_container.children if isinstance(child, MockElement) and child.className == 'share-btn']
    assert len(share_buttons) == 1
    
    share_button = share_buttons[0]
    assert '<i class="fas fa-share-alt"></i> Share' in share_button.innerHTML
    assert share_button.title == 'Share this error translation'
    assert 'click' in share_button.events


def test_share_url_generation():
    """Test that the share URL is generated correctly."""
    # Mock window.location and URL
    class MockLocation:
        href = 'http://localhost:5000/'
    
    class MockURL:
        def __init__(self, url):
            self.url = url
            self.params = {}
        
        def toString(self):
            base = self.url.split('?')[0]
            if not self.params:
                return base
            query = '&'.join([f"{k}={v}" for k, v in self.params.items()])
            return f"{base}?{query}"
        
        @property
        def searchParams(self):
            return self
        
        def set(self, key, value):
            self.params[key] = value
            return self
        
        def delete(self, key):
            if key in self.params:
                del self.params[key]
            return self
    
    # Mock elements and values
    class MockElement:
        def __init__(self):
            self.value = ""
    
    errorInput = MockElement()
    errorInput.value = "TypeError: Cannot read property 'length' of undefined"
    
    languageSelect = MockElement()
    languageSelect.value = "javascript"
    
    window = type('obj', (object,), {
        'location': MockLocation()
    })
    
    # Test URL generation for specific language
    url = shareTranslation(errorInput, languageSelect, window, MockURL)
    assert "error=TypeError" in url
    assert "lang=javascript" in url
    
    # Test URL generation for auto-detect
    languageSelect.value = "auto"
    url = shareTranslation(errorInput, languageSelect, window, MockURL)
    assert "error=TypeError" in url
    assert "lang=" not in url 