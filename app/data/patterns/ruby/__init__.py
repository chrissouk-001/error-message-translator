"""
Ruby Error Patterns

This module contains error patterns for Ruby programming language.
"""

# List to store all Ruby error patterns
PATTERNS = []

# Import patterns from pattern files
try:
    from app.data.patterns.ruby import name_errors
    from app.data.patterns.ruby import syntax_errors
    # Import additional pattern modules as they're created:
    # etc.
except ImportError as e:
    print(f"Warning: Could not import some Ruby error patterns: {e}")

# Example pattern addition:
# PATTERNS.append({
#     "regex": r"NameError: undefined local variable or method `([^']+)'",
#     "title": 'Undefined Variable or Method "{{$1}}"',
#     "explanation": 'Ruby cannot find a variable or method named "{{$1}}". This usually means you\'re trying to use it before defining it, or it might be out of scope.',
#     "solution": 'Check if you have defined "{{$1}}" before using it. Verify the spelling and scope of your variables and methods.',
#     "code_example": """
# # Incorrect:
# puts {{$1}}  # Error: undefined local variable or method '{{$1}}'
#
# # Correct:
# {{$1}} = "Hello"
# puts {{$1}}  # Now it works!
# """,
#     "related_errors": ["NoMethodError"],
#     "difficulty": "beginner",
# }) 