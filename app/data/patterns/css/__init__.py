"""
CSS Error Patterns

This module contains error patterns for CSS styling.
"""

# List to store all CSS error patterns
PATTERNS = []

# Import patterns from pattern files
try:
    from app.data.patterns.css import validation_errors
    # Import additional pattern modules as they're created:
    # etc.
except ImportError as e:
    print(f"Warning: Could not import some CSS error patterns: {e}") 