"""
Ruby SyntaxError Patterns

This module contains error patterns for Ruby SyntaxError exceptions.
"""

from app.data.patterns.ruby import PATTERNS

# SyntaxError: unexpected token
PATTERNS.append({
    "regex": r"SyntaxError: (?:.*?)unexpected ([^,]+)(?:,|$)",
    "title": "Unexpected Token: {{$1}}",
    "explanation": "Ruby encountered a token '{{$1}}' that it wasn't expecting. This usually happens when you have mismatched brackets, missing keywords, or other syntax issues.",
    "solution": "Look at the line indicated in the error message to find mismatched brackets or quotes. Check for missing keywords like 'end', 'do', or comma/period placement.",
    "code_example": """
# Incorrect:
def hello
  puts "Hello, world!"
# SyntaxError: unexpected end-of-input, expecting keyword_end

# Correct:
def hello
  puts "Hello, world!"
end  # Added the missing 'end' keyword

# Another example:
# Incorrect:
if x > 5
  puts "x is greater than 5"
  else  # Incorrect indentation
  puts "x is not greater than 5"
end

# Correct:
if x > 5
  puts "x is greater than 5"
else  # Proper indentation
  puts "x is not greater than 5"
end
""",
    "related_errors": ["unexpected end-of-input", "unterminated string literal"],
    "difficulty": "beginner",
})

# SyntaxError: unterminated string
PATTERNS.append({
    "regex": r"SyntaxError: (?:.*?)unterminated ([a-z_]+)",
    "title": "Unterminated {{$1}}",
    "explanation": "Ruby found an opening quote for a {{$1}} but couldn't find the matching closing quote. This often happens with strings, regular expressions, or other paired delimiters.",
    "solution": "Make sure all your string literals have matching opening and closing quotes. Check for multi-line strings that might be missing the closing quote.",
    "code_example": """
# Incorrect:
message = "Hello, world  # SyntaxError: unterminated string

# Correct:
message = "Hello, world"  # Added the closing quote

# Another example:
# Incorrect:
regex = /[a-z]+/i  # Missing closing slash for regex
puts "Match found" if text =~ regex

# Correct:
regex = /[a-z]+/i  # Added the closing slash
puts "Match found" if text =~ regex
""",
    "related_errors": ["unexpected $end", "SyntaxError: unexpected tSTRING_END"],
    "difficulty": "beginner",
})

# SyntaxError: unexpected end-of-input, expecting keyword_end
PATTERNS.append({
    "regex": r"SyntaxError: (?:.*?)unexpected end-of-input(?:.*?)expecting\s+([^\s,]+)",
    "title": "Missing {{$1}} Keyword",
    "explanation": "Ruby reached the end of your code but was still expecting the keyword '{{$1}}'. This typically happens when you have unclosed blocks or missing 'end' statements.",
    "solution": "Count your opening and closing keywords (like 'do'/'end', 'def'/'end', 'if'/'end') to make sure they balance. Add the missing {{$1}} keyword.",
    "code_example": """
# Incorrect:
class User
  def initialize(name)
    @name = name
  # Missing 'end' for the method
# Missing 'end' for the class

# Correct:
class User
  def initialize(name)
    @name = name
  end  # Added missing 'end' for the method
end  # Added missing 'end' for the class

# Tip: Use proper indentation to help identify missing 'end' statements
""",
    "related_errors": ["SyntaxError: unexpected keyword_end", "SyntaxError: unexpected tIDENTIFIER"],
    "difficulty": "beginner",
})

# SyntaxError: unexpected ')', expecting end-of-input
PATTERNS.append({
    "regex": r"SyntaxError: (?:.*?)unexpected '([^']+)', expecting ([^,]+)",
    "title": "Unexpected '{{$1}}', Expecting {{$2}}",
    "explanation": "Ruby found '{{$1}}' but was expecting '{{$2}}'. This typically happens when you have extra or misplaced parentheses, brackets, or other syntax elements.",
    "solution": "Look at the line indicated in the error message. Check for mismatched parentheses, brackets, or blocks. Ruby expected to see '{{$2}}' but found '{{$1}}' instead.",
    "code_example": """
# Incorrect:
def calculate(x, y))  # Extra closing parenthesis
  x + y
end
# SyntaxError: unexpected ')', expecting end-of-input

# Correct:
def calculate(x, y)  # Removed the extra parenthesis
  x + y
end

# Another example:
# Incorrect:
if (x > 5))  # Extra closing parenthesis
  puts "x is greater than 5"
end

# Correct:
if (x > 5)  # Proper parentheses
  puts "x is greater than 5"
end
""",
    "related_errors": ["SyntaxError: unexpected keyword_end", "SyntaxError: unexpected tIDENTIFIER"],
    "difficulty": "beginner",
}) 