"""
JavaScript Error Patterns

This module contains error patterns for JavaScript programming language.
"""

# List to store all JavaScript error patterns
PATTERNS = []

# Import patterns from pattern files
try:
    from app.data.patterns.javascript import reference_errors
    from app.data.patterns.javascript import syntax_errors
    from app.data.patterns.javascript import type_errors
    # Import additional pattern modules as they're created:
    # etc.
except ImportError as e:
    print(f"Warning: Could not import some JavaScript error patterns: {e}")

# Example pattern addition:
# PATTERNS.append({
#     "regex": r"ReferenceError: ([^']+) is not defined",
#     "title": 'Variable "{{$1}}" Not Defined',
#     "explanation": 'JavaScript cannot find a variable or function named "{{$1}}". This usually means you\'re trying to use it before declaring it, or you might have a typo in the name.',
#     "solution": 'Check if you have declared the variable "{{$1}}" before using it. Look for typos and ensure proper scoping.',
#     "code_example": """
# // Incorrect:
# console.log({{$1}});  // Error: {{$1}} is not defined
#
# // Correct:
# const {{$1}} = 5;
# console.log({{$1}});  // Now it works!
# """,
#     "related_errors": ["TypeError"],
#     "difficulty": "beginner",
# }) 