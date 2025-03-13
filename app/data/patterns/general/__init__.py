"""
General Error Patterns

This module contains error patterns that apply across multiple programming languages.
"""

# List to store all general error patterns
PATTERNS = []

# Import patterns from pattern files
try:
    from app.data.patterns.general import common_errors
    # Import additional pattern modules as they're created:
    # etc.
except ImportError as e:
    print(f"Warning: Could not import some general error patterns: {e}")

# Example pattern addition:
# PATTERNS.append({
#     "regex": r"Permission denied: '([^']+)'",
#     "title": 'Permission Denied for "{{$1}}"',
#     "explanation": 'The program doesn\'t have the necessary permissions to access "{{$1}}". This is a system-level restriction rather than a programming error.',
#     "solution": 'Check the file or directory permissions for "{{$1}}". You may need to change permissions with chmod (Unix/Mac) or file properties (Windows), or run the program with elevated privileges.',
#     "code_example": """
# # Unix/Mac solution
# chmod +r {{$1}}  # For read permission
# chmod +w {{$1}}  # For write permission
# chmod +x {{$1}}  # For execute permission
#
# # Or for all permissions
# chmod 755 {{$1}}  # For directories
# chmod 644 {{$1}}  # For files
# """,
#     "related_errors": ["Access denied", "Operation not permitted"],
#     "difficulty": "intermediate",
# }) 