"""
Python TypeError Patterns

This module contains error patterns for Python TypeError exceptions.
"""

from app.data.patterns.python import PATTERNS

# TypeError: unsupported operand type(s)
PATTERNS.append({
    "regex": r"TypeError: unsupported operand type\(s\) for ([^:]+): '([^']+)' and '([^']+)'",
    "title": "Incompatible Types for {{$1}} Operation",
    "explanation": "You're trying to use the {{$1}} operator between a {{$2}} and a {{$3}}, but these types can't be combined this way in Python.",
    "solution": "Make sure both values are of compatible types before using the {{$1}} operator. You might need to convert one value to match the type of the other.",
    "code_example": """
# Incorrect:
result = "hello" + 42  # TypeError: unsupported operand type(s) for +: 'str' and 'int'

# Correct:
result = "hello" + str(42)  # Convert the int to str
# or
result = "hello" + "42"  # Use a string literal
""",
    "related_errors": ["ValueError"],
    "difficulty": "beginner",
})

# TypeError: object is not subscriptable
PATTERNS.append({
    "regex": r"TypeError: '([^']+)' object is not subscriptable",
    "title": "Cannot Use Index on {{$1}} Type",
    "explanation": "You're trying to use square brackets [] to access an item in a {{$1}} object, but this type doesn't support indexing.",
    "solution": "Check that your variable is actually a collection type like list, tuple, dict, or str before trying to use indexing. Make sure you're not trying to index an integer, float, or None.",
    "code_example": """
# Incorrect:
number = 42
digit = number[0]  # TypeError: 'int' object is not subscriptable

# Correct:
number_str = str(42)
digit = number_str[0]  # Works! '4'

# Or use a proper collection:
numbers = [42, 43, 44]
first = numbers[0]  # Works! 42
""",
    "related_errors": ["IndexError", "KeyError"],
    "difficulty": "beginner",
})

# TypeError: object is not callable
PATTERNS.append({
    "regex": r"TypeError: '([^']+)' object is not callable",
    "title": "Cannot Call {{$1}} Type as a Function",
    "explanation": "You're trying to call a {{$1}} object as if it were a function by using parentheses () after it, but this type doesn't support being called.",
    "solution": "Check if you've accidentally overwritten a function name with a different type, or if you're trying to call something that isn't a function.",
    "code_example": """
# Incorrect:
print = "Hello World"
print()  # TypeError: 'str' object is not callable

# Correct:
# Don't overwrite built-in functions, use different variable names:
message = "Hello World"
print(message)  # Works!
""",
    "related_errors": ["NameError"],
    "difficulty": "beginner",
})

# TypeError: function takes x positional arguments but y were given
PATTERNS.append({
    "regex": r"TypeError: ([^\(]+)\(\) takes (\d+) positional arguments? but (\d+) (?:were|was) given",
    "title": "Wrong Number of Arguments for {{$1}}()",
    "explanation": "You're calling the function {{$1}}() with {{$3}} arguments, but it expects {{$2}} arguments.",
    "solution": "Check the function definition for {{$1}} and make sure you're providing the correct number of arguments.",
    "code_example": """
# Incorrect:
def greet(name):
    return f"Hello, {name}!"
    
result = greet("Alice", "Johnson")  # TypeError: greet() takes 1 positional argument but 2 were given

# Correct:
result = greet("Alice")  # Works!

# If you need to pass more arguments, update the function:
def greet_full(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"
    
result = greet_full("Alice", "Johnson")  # Works!
""",
    "related_errors": ["SyntaxError"],
    "difficulty": "beginner",
})

# TypeError: cannot unpack non-iterable type
PATTERNS.append({
    "regex": r"TypeError: cannot unpack non-iterable ([^']+) object",
    "title": "Cannot Unpack a {{$1}} Object",
    "explanation": "You're trying to use unpacking (assigning multiple variables at once) with a {{$1}} object, but this type can't be unpacked because it's not iterable.",
    "solution": "Make sure you're unpacking an iterable (like a list, tuple, or string) and not a single value like an integer or None.",
    "code_example": """
# Incorrect:
number = 42
a, b = number  # TypeError: cannot unpack non-iterable int object

# Correct:
number_pair = (42, 73)
a, b = number_pair  # Works! a = 42, b = 73

# Or with a list:
number_list = [42, 73]
a, b = number_list  # Works! a = 42, b = 73
""",
    "related_errors": ["ValueError: too many values to unpack"],
    "difficulty": "intermediate",
}) 