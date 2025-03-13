"""
Python Error Patterns

This module contains error patterns for Python programming language.
"""

# List to store all Python error patterns
PATTERNS = []

# Import patterns from pattern files
try:
    from app.data.patterns.python import name_errors
    from app.data.patterns.python import type_errors
    from app.data.patterns.python import syntax_errors
    # Import additional pattern modules as they're created:
    # etc.
except ImportError as e:
    print(f"Warning: Could not import some Python error patterns: {e}")

# Example pattern addition:
# PATTERNS.append({
#     "regex": r"NameError: name \'([^\']+)\' is not defined",
#     "title": 'Variable "{{$1}}" Not Defined',
#     "explanation": 'Python cannot find a variable named "{{$1}}". This usually means you\'re trying to use a variable before creating it, or you might have a typo in the variable name.',
#     "solution": 'Make sure you\'ve defined the variable "{{$1}}" before using it. Check for typos in variable names.',
#     "code_example": """
# Incorrect:
# result = {{$1}} + 10  # Error: {{$1}} doesn't exist yet
#
# Correct:
# {{$1}} = 5
# result = {{$1}} + 10  # Now it works!
# """,
#     "related_errors": ["UnboundLocalError"],
#     "difficulty": "beginner",
# }) 