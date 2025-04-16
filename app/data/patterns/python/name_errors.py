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

PATTERNS.append({
    "regex": r"AttributeError: '([^']+)' object has no attribute '([^']+)'",
    "title": "Missing Attribute: {{$2}} on {{$1}} Object",
    "explanation": "You're trying to access an attribute or method named '{{$2}}' on an object of type '{{$1}}', but that object doesn't have such an attribute.",
    "solution": "Check for typos in the attribute name '{{$2}}'. Verify that the object is of the expected type '{{$1}}' and that it actually has the attribute you're trying to access. Use dir(object) to see available attributes.",
    "code_example": """
# Incorrect:
my_list = [1, 2, 3]
my_list.lenght  # AttributeError: 'list' object has no attribute 'lenght' (typo)

# Correct:
my_list = [1, 2, 3]
my_list.length  # Correct attribute name

# Another example:
my_string = "hello"
my_string.append(" world") # AttributeError: 'str' object has no attribute 'append'

# Correct (strings are immutable):
my_string = "hello"
my_string = my_string + " world" # Use concatenation
""",
    "related_errors": ["NameError", "TypeError: object is not callable"],
    "difficulty": "beginner",
}) 