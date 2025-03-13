"""
Error Patterns

This module contains error patterns for various programming languages.
"""

# List to store all error patterns
ALL_PATTERNS = []

# Import patterns from language-specific modules
try:
    from app.data.patterns import python
    ALL_PATTERNS.extend(python.PATTERNS)
except ImportError as e:
    print(f"Warning: Could not import Python error patterns: {e}")

try:
    from app.data.patterns import javascript
    ALL_PATTERNS.extend(javascript.PATTERNS)
except ImportError as e:
    print(f"Warning: Could not import JavaScript error patterns: {e}")

try:
    from app.data.patterns import java
    ALL_PATTERNS.extend(java.PATTERNS)
except ImportError as e:
    print(f"Warning: Could not import Java error patterns: {e}")

try:
    from app.data.patterns import ruby
    ALL_PATTERNS.extend(ruby.PATTERNS)
except ImportError as e:
    print(f"Warning: Could not import Ruby error patterns: {e}")

try:
    from app.data.patterns import html
    ALL_PATTERNS.extend(html.PATTERNS)
except ImportError as e:
    print(f"Warning: Could not import HTML error patterns: {e}")

try:
    from app.data.patterns import css
    ALL_PATTERNS.extend(css.PATTERNS)
except ImportError as e:
    print(f"Warning: Could not import CSS error patterns: {e}")

try:
    from app.data.patterns import general
    ALL_PATTERNS.extend(general.PATTERNS)
except ImportError as e:
    print(f"Warning: Could not import general error patterns: {e}")

print(f"Loaded {len(ALL_PATTERNS)} error patterns in total.") 