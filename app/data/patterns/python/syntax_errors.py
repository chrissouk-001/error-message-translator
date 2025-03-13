"""
Python SyntaxError Patterns

This module contains error patterns for Python SyntaxError exceptions.
"""

from app.data.patterns.python import PATTERNS

# SyntaxError: invalid syntax
PATTERNS.append({
    "regex": r"SyntaxError: invalid syntax",
    "title": "Invalid Python Syntax",
    "explanation": "Python couldn't understand your code because it doesn't follow Python's syntax rules. This is often due to typos, missing or extra characters, or using Python syntax incorrectly.",
    "solution": "Check your code carefully for missing colons, brackets, parentheses, quotes, or other punctuation. Look at the line indicated by the error and the line just before it.",
    "code_example": """
# Incorrect:
if x > 5
    print("x is greater than 5")  # SyntaxError: invalid syntax (missing colon)

# Correct:
if x > 5:
    print("x is greater than 5")  # Added the colon
""",
    "related_errors": ["IndentationError", "SyntaxError: unexpected EOF"],
    "difficulty": "beginner",
})

# SyntaxError: EOL while scanning string literal
PATTERNS.append({
    "regex": r"SyntaxError: (EOL|EOF) while scanning string literal",
    "title": "Unclosed String",
    "explanation": "You started a string with a quote but didn't close it with a matching quote. Python reached the end of the line (EOL) or end of file (EOF) while still inside the string.",
    "solution": "Make sure all your strings have matching opening and closing quotes. Check for strings that might be missing a closing quote.",
    "code_example": """
# Incorrect:
message = "Hello, world  # SyntaxError: EOL while scanning string literal

# Correct:
message = "Hello, world"  # Added the closing quote
""",
    "related_errors": ["SyntaxError: unterminated string literal"],
    "difficulty": "beginner",
})

# SyntaxError: unexpected EOF while parsing
PATTERNS.append({
    "regex": r"SyntaxError: unexpected EOF while parsing",
    "title": "Unexpected End of File",
    "explanation": "Python reached the end of the file (EOF) while still expecting more code. This usually means you have unclosed brackets, parentheses, or indentation blocks.",
    "solution": "Check for missing closing brackets (), [], {}, or incomplete control structures like if, for, or while statements. Make sure all opening brackets have matching closing brackets.",
    "code_example": """
# Incorrect:
def calculate_total(items):
    total = 0
    for item in items:
        total += item.price  # SyntaxError: unexpected EOF while parsing (missing closing parenthesis)
    
    return total  # This is never reached

# Correct:
def calculate_total(items):
    total = 0
    for item in items:
        total += item.price
    
    return total
""",
    "related_errors": ["SyntaxError: invalid syntax", "IndentationError"],
    "difficulty": "beginner",
})

# IndentationError: expected an indented block
PATTERNS.append({
    "regex": r"IndentationError: expected an indented block",
    "title": "Missing Indentation Block",
    "explanation": "After a line that should be followed by indented code (like after a colon in if, for, while, def, etc.), Python found no indented code block.",
    "solution": "Add proper indentation (usually 4 spaces or a tab) to the line after statements ending with a colon. Every code block that follows a colon must be indented.",
    "code_example": """
# Incorrect:
if x > 10:
print("x is greater than 10")  # IndentationError: expected an indented block

# Correct:
if x > 10:
    print("x is greater than 10")  # Properly indented
""",
    "related_errors": ["IndentationError: unexpected indent", "SyntaxError: invalid syntax"],
    "difficulty": "beginner",
})

# IndentationError: unexpected indent
PATTERNS.append({
    "regex": r"IndentationError: unexpected indent",
    "title": "Unexpected Indentation",
    "explanation": "Python found indentation where it didn't expect it. This usually means a line is indented when it shouldn't be.",
    "solution": "Check your code's indentation structure and make sure each line has the correct level of indentation. Only indent after statements ending with a colon or to continue a block.",
    "code_example": """
# Incorrect:
x = 10
    y = 20  # IndentationError: unexpected indent

# Correct:
x = 10
y = 20  # No indentation needed here
""",
    "related_errors": ["IndentationError: expected an indented block"],
    "difficulty": "beginner",
}) 