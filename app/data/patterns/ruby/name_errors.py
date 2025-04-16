"""
Ruby NameError Patterns

This module contains error patterns for Ruby NameError exceptions.
"""

from app.data.patterns.ruby import PATTERNS

# NameError: undefined local variable or method
PATTERNS.append({
    "regex": r"NameError: undefined local variable or method [`']([^'`]+)'",
    "title": "Undefined Variable or Method: {{$1}}",
    "explanation": "Ruby can't find a variable or method named '{{$1}}'. This usually means you're trying to use a variable before it's defined, or you've mistyped a method name.",
    "solution": "Check for typos in '{{$1}}'. Make sure you've defined the variable before using it, or that you're calling the correct method name.",
    "code_example": """
# Incorrect:
puts message  # NameError: undefined local variable or method 'message'

# Correct:
message = "Hello, World!"
puts message  # Works!

# Or for a method:
def greet
  puts "Hello!"
end

greet  # Works!
""",
    "related_errors": ["NoMethodError", "uninitialized constant"],
    "difficulty": "beginner",
})

# NameError: uninitialized constant
PATTERNS.append({
    "regex": r"NameError: uninitialized constant ([^:]+)(?:::([^:]+))?",
    "title": "Uninitialized Constant: {{$1}}",
    "explanation": "Ruby can't find a constant (class or module) named '{{$1}}'. This usually means you're trying to use a class that doesn't exist or that hasn't been required/imported.",
    "solution": "Check if you've defined the class or module '{{$1}}'. Make sure you've required any necessary files and check for typos in the class or module name.",
    "code_example": """
# Incorrect:
user = User.new  # NameError: uninitialized constant User

# Correct:
# Option 1: Define the class before using it
class User
  attr_accessor :name
end

user = User.new  # Works!

# Option 2: Require a file that defines the class
require 'user'  # Loads user.rb which defines User class
user = User.new  # Works!

# Option 3: Use the correct namespace
user = MyApp::User.new  # If User is defined within the MyApp module
""",
    "related_errors": ["LoadError", "NameError: undefined local variable"],
    "difficulty": "beginner",
})

# NoMethodError: undefined method
PATTERNS.append({
    "regex": r"NoMethodError: undefined method [`']([^'`]+)' for ([^:]+)",
    "title": "Undefined Method: {{$1}} for {{$2}}",
    "explanation": "Ruby can't find a method named '{{$1}}' for the object '{{$2}}'. This means either the method doesn't exist for this type of object, or you've misspelled the method name.",
    "solution": "Check if '{{$1}}' is a valid method for the type of object '{{$2}}'. Look for typos in the method name, or make sure you're calling the method on the correct object.",
    "code_example": """
# Incorrect:
number = 42
number.length  # NoMethodError: undefined method 'length' for 42:Integer

# Correct:
# Option 1: Use methods that exist for the object type
number = 42
number.to_s.length  # Convert to string first, then get length

# Option 2: Check the object type and use appropriate methods
if number.is_a?(String)
  puts number.length
else
  puts number.to_s.length
end

# Option 3: Use respond_to? to check if a method exists
number = 42
if number.respond_to?(:length)
  puts number.length
else
  puts "Can't call length on #{number.class}"
end
""",
    "related_errors": ["NameError", "TypeError"],
    "difficulty": "beginner",
})

# LoadError: cannot load such file
PATTERNS.append({
    "regex": r"LoadError: cannot load such file -- (.+)",
    "title": "Cannot Load File: {{$1}}",
    "explanation": "Ruby failed to load the file '{{$1}}'. This happens when you try to 'require' or 'load' a file that Ruby can't find in its load path.",
    "solution": "Make sure the file '{{$1}}' exists and is correctly spelled. Check if the file is in a directory included in Ruby's $LOAD_PATH. If it's a gem, ensure the gem is installed. If it's a relative path, use 'require_relative' instead.",
    "code_example": """
# Incorrect:
require 'my_missing_library'  # LoadError: cannot load such file -- my_missing_library

# Correct:
# Option 1: Ensure the file exists in $LOAD_PATH or install the gem
# gem install my_library
# require 'my_library'

# Option 2: Use require_relative for local files
# Assuming 'my_local_file.rb' is in the same directory
require_relative 'my_local_file'
""",
    "related_errors": ["NameError: uninitialized constant"],
    "difficulty": "intermediate",
}) 