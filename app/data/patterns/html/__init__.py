"""
HTML Error Patterns

This module contains error patterns for HTML markup.
"""

# List to store all HTML error patterns
PATTERNS = []

# Import patterns from pattern files
try:
    from app.data.patterns.html import validation_errors
    # Import additional pattern modules as they're created:
    # etc.
except ImportError as e:
    print(f"Warning: Could not import some HTML error patterns: {e}")

# Example pattern addition:
# PATTERNS.append({
#     "regex": r"Unclosed tag ([a-zA-Z0-9_-]+)",
#     "title": 'Unclosed HTML Tag "{{$1}}"',
#     "explanation": 'You have an opening <{{$1}}> tag without a corresponding closing </{{$1}}> tag. HTML requires most tags to be properly closed.',
#     "solution": 'Add the missing closing tag </{{$1}}> at the appropriate position in your HTML document.',
#     "code_example": """
# <!-- Incorrect -->
# <{{$1}}>This text is inside the tag
# 
# <!-- Correct -->
# <{{$1}}>This text is inside the tag</{{$1}}>
# """,
#     "related_errors": ["Stray end tag", "Missing end tag"],
#     "difficulty": "beginner",
# }) 