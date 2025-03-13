"""
Java Error Patterns

This module contains error patterns for Java programming language.
"""

# List to store all Java error patterns
PATTERNS = []

# Import patterns from pattern files
try:
    from app.data.patterns.java import compilation_errors
    from app.data.patterns.java import runtime_exceptions
    # Import additional pattern modules as they're created:
    # etc.
except ImportError as e:
    print(f"Warning: Could not import some Java error patterns: {e}")

# Example pattern addition:
# PATTERNS.append({
#     "regex": r"cannot find symbol\s+symbol:\s+([a-zA-Z0-9_]+)\s+([a-zA-Z0-9_]+)",
#     "title": 'Cannot Find Symbol "{{$2}}"',
#     "explanation": 'Java cannot find a symbol (variable, method, or class) named "{{$2}}". This usually means it hasn\'t been declared, or it\'s out of scope where you\'re trying to use it.',
#     "solution": 'Check if you have declared "{{$2}}" before using it. Verify the spelling and make sure it\'s accessible in the current scope.',
#     "code_example": """
# // Incorrect:
# public class Example {
#     public static void main(String[] args) {
#         System.out.println({{$2}});  // Error: cannot find symbol {{$2}}
#     }
# }
#
# // Correct:
# public class Example {
#     public static void main(String[] args) {
#         String {{$2}} = "Hello";
#         System.out.println({{$2}});  // Now it works!
#     }
# }
# """,
#     "related_errors": ["ClassNotFoundException"],
#     "difficulty": "beginner",
# }) 