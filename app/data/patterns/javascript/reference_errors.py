"""
JavaScript ReferenceError Patterns

This module contains error patterns for JavaScript ReferenceError exceptions.
"""

from app.data.patterns.javascript import PATTERNS

# ReferenceError: variable is not defined
PATTERNS.append({
    "regex": r"ReferenceError: ([^']+) is not defined",
    "title": 'Variable "{{$1}}" Not Defined',
    "explanation": 'JavaScript cannot find a variable or function named "{{$1}}". This usually means you\'re trying to use it before declaring it, or you might have a typo in the name.',
    "solution": 'Check if you have declared the variable "{{$1}}" before using it. Look for typos and ensure proper scoping.',
    "code_example": """
// Incorrect:
console.log({{$1}});  // Error: {{$1}} is not defined

// Correct:
const {{$1}} = 5;
console.log({{$1}});  // Now it works!
""",
    "related_errors": ["TypeError"],
    "difficulty": "beginner",
})

# More patterns can be added here as needed 