"""
Python NameError Patterns

This module contains error patterns for Python NameError exceptions.
"""

from app.data.patterns.python import PATTERNS

# NameError: name is not defined
PATTERNS.append({
    "regex": r"NameError: name \'([^\']+)\' is not defined",
    "title": 'Variable "{{$1}}" Not Defined',
    "explanation": 'Python cannot find a variable named "{{$1}}". This usually means you\'re trying to use a variable before creating it, or you might have a typo in the variable name.',
    "solution": 'Make sure you\'ve defined the variable "{{$1}}" before using it. Check for typos in variable names.',
    "code_example": """
# Incorrect:
result = {{$1}} + 10  # Error: {{$1}} doesn't exist yet

# Correct:
{{$1}} = 5
result = {{$1}} + 10  # Now it works!
""",
    "related_errors": ["UnboundLocalError"],
    "difficulty": "beginner",
})

# More patterns can be added here as needed 