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

# Add f-string syntax error
PATTERNS.append({
    "regex": r"SyntaxError: f-string: expecting '}'",
    "title": "Unmatched Curly Brace in f-string",
    "explanation": "You have an f-string with an opening curly brace '{' but no matching closing brace '}'.",
    "solution": "Make sure all opening curly braces in f-strings have matching closing braces. Remember that to include a literal curly brace in an f-string, you need to double it ({{ or }}).",
    "code_example": """
# Incorrect:
message = f"Hello, {name"  # SyntaxError: f-string: expecting '}'

# Correct:
message = f"Hello, {name}"

# If you want to include literal curly braces:
message = f"{{ Hello, {name} }}"  # { Hello, John }
""",
    "related_errors": ["SyntaxError: EOL while scanning string literal"],
    "difficulty": "beginner",
})

# Add walrus operator syntax error
PATTERNS.append({
    "regex": r"SyntaxError: assignment expression cannot be used in a comprehension iterable",
    "title": "Invalid Walrus Operator Usage",
    "explanation": "You're trying to use the walrus operator (:=) in the iterable part of a comprehension, which is not allowed.",
    "solution": "The walrus operator can only be used in the condition or output expression of a comprehension, not in the iterable expression.",
    "code_example": """
# Incorrect:
data = [1, 2, 3, 4, 5]
result = [x for x in (y := data) if x > 2]  # SyntaxError: assignment expression cannot be used in a comprehension iterable

# Correct:
data = [1, 2, 3, 4, 5]
y = data
result = [x for x in y if x > 2]

# Valid walrus operator usage:
result = [x for x in data if (x := x + 1) > 3]
""",
    "related_errors": ["SyntaxError: invalid syntax"],
    "difficulty": "intermediate",
})

# Add multiple context manager syntax error
PATTERNS.append({
    "regex": r"SyntaxError: too many nested blocks",
    "title": "Too Many Nested Blocks",
    "explanation": "Your code has too many nested blocks (like loops or if statements) which exceeds Python's limit for nested blocks.",
    "solution": "Refactor your code to reduce nesting. Extract nested blocks into separate functions or use list comprehensions instead of deeply nested loops.",
    "code_example": """
# Problematic:
def deeply_nested_function():
    for i in range(20):
        for j in range(20):
            for k in range(20):
                # Many more nested loops/blocks...
                # Eventually: SyntaxError: too many nested blocks

# Better:
def process_element(i, j, k):
    # Process a single element
    pass

def improved_function():
    for i in range(20):
        for j in range(20):
            for k in range(20):
                process_element(i, j, k)
""",
    "related_errors": ["RecursionError: maximum recursion depth exceeded"],
    "difficulty": "intermediate",
})

# Add invalid decorator syntax error
PATTERNS.append({
    "regex": r"SyntaxError: invalid syntax",
    "title": "Invalid Python Syntax",
    "explanation": "Your code contains syntax that Python cannot understand. This could be due to mismatched brackets, incorrect indentation, using Python 3 features in Python 2, or many other issues.",
    "solution": "Check for common syntax errors: missing parentheses, incorrect indentation, missing colons after if/for/while statements, or using newer Python features on older Python versions.",
    "code_example": """
# Examples of invalid syntax:

# Missing colon:
if x > 5
    print(x)  # SyntaxError: invalid syntax

# Correct:
if x > 5:
    print(x)

# Misplaced decorator:
def my_function():
    @decorator  # SyntaxError: invalid syntax
    x = 10

# Correct:
@decorator
def my_function():
    x = 10
""",
    "related_errors": ["IndentationError: unexpected indent", "SyntaxError: unexpected EOF while parsing"],
    "difficulty": "beginner",
})

# Add 'continue' outside loop syntax error
PATTERNS.append({
    "regex": r"SyntaxError: 'continue' not properly in loop",
    "title": "'continue' Statement Outside Loop",
    "explanation": "You've used a 'continue' statement outside of a loop. The 'continue' statement can only be used inside loops (for, while).",
    "solution": "Make sure 'continue' statements are only used inside loop bodies. If you're trying to skip to the next iteration in a function, consider using a return statement instead.",
    "code_example": """
# Incorrect:
def process_item(item):
    if item is None:
        continue  # SyntaxError: 'continue' not properly in loop
    return item * 2

# Correct:
def process_item(item):
    if item is None:
        return  # Skip this item by returning early
    return item * 2

# Correct usage in a loop:
for item in items:
    if item is None:
        continue  # Skip to next iteration
    process_item(item)
""",
    "related_errors": ["SyntaxError: 'break' outside loop"],
    "difficulty": "beginner",
}) 