"""
Error Patterns Module

This module contains predefined patterns for recognizing and translating
common error messages from various programming languages.

Each pattern consists of:
- regex: Regular expression to match the error
- title: A concise title summarizing the error
- explanation: Detailed explanation in beginner-friendly terms
- solution: Steps to resolve the issue
- code_example: (Optional) Example code showing the fix
- related_errors: (Optional) List of related errors
- difficulty: Level of difficulty (beginner, intermediate, advanced)

Placeholders in the form {{$N}} can be used to reference captured groups
from the regular expression.
"""

# Python error patterns
PYTHON_PATTERNS = [
    {
        "regex": r"NameError: name \'([^\']+)\' is not defined",
        "title": 'Variable "{{$1}}" Not Defined',
        "explanation": 'Python cannot find a variable named "{{$1}}". This usually means you\'re trying to use a variable before creating it, or you might have a typo in the variable name.',
        "solution": 'Make sure you\'ve defined the variable "{{$1}}" before using it. Check for typos in variable names.',
        "code_example": """
# Incorrect:
result = {{$1}} + 10  # Error: {{$1}} doesn't exist yet

# Correct:
{{$1}} = 5
result = {{$1}} + 10  # Now it works!
""",
        "related_errors": ["UnboundLocalError"],
        "difficulty": "beginner",
    },
    {
        "regex": r"TypeError: \'([^\']+)\' object is not ([^\']+)",
        "title": "Type Error: Can't {{$2}} This Object",
        "explanation": "You're trying to {{$2}} a \"{{$1}}\" object, but that operation isn't allowed for this type of data.",
        "solution": "Check what type of data you're working with and make sure the operation is valid for that type. You might need to convert the data to a different type first.",
        "code_example": """
# Example (if trying to iterate over an integer):
# Incorrect:
number = 42
for digit in number:  # Error: 'int' object is not iterable
    print(digit)

# Correct:
number = 42
for digit in str(number):  # Convert to string first
    print(digit)
""",
        "difficulty": "beginner",
    },
    {
        "regex": r"SyntaxError: invalid syntax",
        "title": "Syntax Error: Invalid Syntax",
        "explanation": "Python encountered invalid syntax. This might be due to a missing punctuation or an extra character.",
        "solution": "Check your code for any syntax mistakes such as missing colons, parentheses, or quotation marks.",
        "code_example": """
# Incorrect:
print("Hello World"

# Correct:
print("Hello World")
""",
        "difficulty": "beginner"
    },
    {
        "regex": r"IndentationError: (unexpected indent|expected an indented block)",
        "title": "Indentation Error",
        "explanation": "There is an indentation issue in your code. Python relies on indentation to define code blocks.",
        "solution": "Ensure that your code follows proper indentation. Each code block should be consistently indented.",
        "code_example": """
# Incorrect:
def foo():
print("Hello World")

# Correct:
def foo():
    print("Hello World")
""",
        "difficulty": "beginner"
    },
    {
        "regex": r"ImportError: No module named ([^\']+)",
        "title": "Module Not Found: {{$1}}",
        "explanation": "Python tried to import the module \"{{$1}}\" but couldn't find it. This usually means the module isn't installed or isn't in your Python path.",
        "solution": "Install the missing module using pip: `pip install {{$1}}`. If it's a local module, make sure the file exists and is in a directory that Python can find.",
        "code_example": """
# Terminal command to install the module:
# pip install {{$1}}

# If it's a local module, make sure it's in the correct path:
import {{$1}}  # This will work once the module is installed or found
""",
        "difficulty": "beginner",
    },
    {
        "regex": r"AttributeError: \'([^\']+)\' object has no attribute \'([^\']+)\'",
        "title": 'Attribute Error: No "{{$2}}" in {{$1}}',
        "explanation": "You're trying to access an attribute or method called \"{{$2}}\" on a {{$1}} object, but {{$1}} doesn't have this attribute or method.",
        "solution": "Check the documentation for the {{$1}} type to see what attributes and methods it has. Check for typos in the attribute name.",
        "code_example": """
# Example (if trying to call a non-existent method on a string):
text = "Hello"
result = text.capitalize()  # This works: "Hello"
result = text.reverse()  # Error: strings don't have a reverse() method

# Correct (for strings):
text = "Hello"
result = text[::-1]  # Use slicing to reverse a string: "olleH"
""",
        "difficulty": "intermediate",
    },
    {
        "regex": r"ZeroDivisionError: division by zero",
        "title": "Division by Zero",
        "explanation": "Your code is trying to divide a number by zero, which is not allowed in mathematics.",
        "solution": "Check for places where you might be dividing by zero and add conditions to handle those cases.",
        "code_example": """
# Incorrect:
x = 10
y = 0
result = x / y  # Error: division by zero

# Correct (using a conditional):
x = 10
y = 0
if y != 0:
    result = x / y
else:
    result = "Cannot divide by zero"
""",
        "difficulty": "beginner",
    },
    {
        "regex": r"RecursionError: maximum recursion depth exceeded",
        "title": "Maximum Recursion Depth Exceeded",
        "explanation": "Your code contains a function that is calling itself too many times. This usually happens when a recursive function doesn't have a proper exit condition, creating an infinite loop of function calls.",
        "solution": "Check your recursive function and make sure it has a proper base case that will eventually be reached. Also consider if the problem could be solved using iteration instead of recursion.",
        "code_example": """
# Incorrect (infinite recursion):
def factorial(n):
    return n * factorial(n-1)  # No base case!

# Correct:
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n-1)
""",
        "related_errors": ["StackOverflowError"],
        "difficulty": "intermediate",
    },
    {
        "regex": r"IndexError: list index out of range",
        "title": "List Index Out of Range",
        "explanation": "You're trying to access an element in a list using an index that is too large (or negative). Python lists are zero-indexed, so a list with n elements has indices from 0 to n-1.",
        "solution": "Make sure your index is within the valid range for the list. Check the length of your list and ensure your index is less than that value.",
        "code_example": """
# Incorrect:
my_list = [1, 2, 3]
print(my_list[3])  # Error: Index 3 is out of range

# Correct:
my_list = [1, 2, 3]
if len(my_list) > 3:
    print(my_list[3])
else:
    print("Index out of range")
    
# Or use a safer approach with try/except:
try:
    print(my_list[3])
except IndexError:
    print("Index out of range")
""",
    },
    {
        "regex": r"KeyError: \'?([^\']+)\'?",
        "title": 'Dictionary Key "{{$1}}" Not Found',
        "explanation": "You're trying to access a key \"{{$1}}\" that doesn't exist in your dictionary.",
        "solution": 'Check that the key exists before trying to access it. Use dictionary.get() method or the "in" operator to safely check for keys.',
        "code_example": """
# Incorrect:
my_dict = {"name": "John", "age": 30}
print(my_dict["email"])  # Error: 'email' key doesn't exist

# Correct (using .get() with default value):
my_dict = {"name": "John", "age": 30}
print(my_dict.get("email", "No email found"))  # Safe, returns default value

# Or check if key exists:
if "email" in my_dict:
    print(my_dict["email"])
else:
    print("No email found")
""",
    },
    {
        "regex": r"ModuleNotFoundError: No module named \'?([^\'\)]+)\'?",
        "title": 'Module "{{$1}}" Not Found',
        "explanation": "Python cannot find the module \"{{$1}}\" that you're trying to import. Either the module isn't installed, or there's a typo in the module name.",
        "solution": 'Try installing the module using pip: "pip install {{$1}}". If that doesn\'t work, check for typos in the module name.',
        "code_example": """
# In your terminal or command prompt:
# pip install {{$1}}

# Or if you're using Python 3:
# python -m pip install {{$1}}
""",
    },
    {
        "regex": r"ValueError: ([^\']+)",
        "title": "Value Error: {{$1}}",
        "explanation": "You're trying to perform an operation with a value that's not appropriate. The specific issue is: {{$1}}",
        "solution": "Check the values you're using in the operation and make sure they're appropriate for what you're trying to do.",
        "code_example": """
# Example (if converting a non-numeric string to int):
# Incorrect:
number = int("hello")  # Error: invalid literal for int()

# Correct (check before converting):
text = "hello"
if text.isdigit():
    number = int(text)
else:
    print("Cannot convert to number")
""",
    },
    {
        "regex": r"FileNotFoundError: \[Errno 2\] No such file or directory: \'?([^\']+)\'?",
        "title": "File Not Found: {{$1}}",
        "explanation": "Python cannot find the file \"{{$1}}\" that you're trying to access. Either the file doesn't exist, or the path is incorrect.",
        "solution": "Check that the file exists at the specified path. Make sure you're using the correct path, which might be relative to the working directory.",
        "code_example": """
# Incorrect (if file doesn't exist):
with open("{{$1}}", "r") as file:
    content = file.read()

# Correct (with error handling):
import os
file_path = "{{$1}}"
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        content = file.read()
else:
    print(f"The file {file_path} does not exist.")
""",
    },
    {
        "regex": r"ModuleNotFoundError: No module named \'([^\']+)\'",
        "title": "Module Not Found: {{$1}}",
        "explanation": 'Python cannot find the module "{{$1}}" that your code is trying to import. This usually means the module is not installed or not in the Python path.',
        "solution": "Install the missing module using pip: `pip install {{$1}}`. If it's a local module, make sure the file exists and is in a directory that Python can find (either in the current directory or in the PYTHONPATH).",
        "code_example": """
# Terminal command to install the missing module
pip install {{$1}}

# If it's a local module, make sure your directory structure is correct
# For example, if trying to import mymodule:

# File structure:
# /project
#   /mypackage
#     __init__.py
#     mymodule.py
#   main.py

# In main.py:
from mypackage import mymodule  # Correct import
""",
    },
    {
        "regex": r"ZeroDivisionError: division by zero",
        "title": "Division by Zero",
        "explanation": "Your code is attempting to divide a number by zero, which is mathematically undefined and raises a ZeroDivisionError in Python.",
        "solution": "Add a condition to check if the divisor is zero before performing the division. You can use an if statement to provide an alternative result or raise a more specific error.",
        "code_example": """
# Problematic code
result = 10 / 0  # This will raise ZeroDivisionError

# Safer approach with condition
divisor = 0
if divisor != 0:
    result = 10 / divisor
else:
    result = "Cannot divide by zero"  # Or some default value

# Using try-except
try:
    result = 10 / divisor
except ZeroDivisionError:
    result = "Cannot divide by zero"
""",
    },
    {
        "regex": r"KeyError: \'([^\']+)\'",
        "title": "Dictionary Key Not Found: {{$1}}",
        "explanation": 'Your code is trying to access a dictionary with the key "{{$1}}", but this key doesn\'t exist in the dictionary.',
        "solution": "Check if the key exists before accessing it using the `in` operator, or use the `.get()` method which allows you to provide a default value if the key doesn't exist.",
        "code_example": """
# Problematic code
my_dict = {"name": "John", "age": 30}
value = my_dict["email"]  # KeyError: 'email'

# Better approach with .get() method
my_dict = {"name": "John", "age": 30}
value = my_dict.get("email", "Not provided")  # Returns "Not provided" instead of raising error

# Or check before accessing
if "email" in my_dict:
    value = my_dict["email"]
else:
    value = "Not provided"
""",
    },
    {
        "regex": r"AttributeError: '([^']+)' object has no attribute '([^']+)'",
        "title": "Attribute Error",
        "explanation": "Python attempted to access an attribute on an object that does not exist. This is often due to a typo or using an unsupported method.",
        "solution": "Check if the attribute exists on the object and correct any typos. Consider using hasattr() to verify attribute existence.",
        "code_example": """
# Incorrect:
obj = None
obj.some_method()

# Correct:
if obj is not None:
    obj.some_method()
""",
        "difficulty": "beginner"
    },
    {
        "regex": r"RecursionError: maximum recursion depth exceeded",
        "title": "Maximum Recursion Depth Exceeded",
        "explanation": "Your code contains a function that is calling itself too many times. This usually happens when a recursive function doesn't have a proper exit condition, creating an infinite loop of function calls.",
        "solution": "Check your recursive function and make sure it has a proper base case that will eventually be reached. Also consider if the problem could be solved using iteration instead of recursion.",
        "code_example": """
# Incorrect (infinite recursion):
def factorial(n):
    return n * factorial(n-1)  # No base case!

# Correct:
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n-1)
""",
        "related_errors": ["StackOverflowError"],
        "difficulty": "intermediate",
    },
    {
        "regex": r"ModuleNotFoundError: No module named '([^']+)'",
        "title": "Module Not Found: {{$1}}",
        "explanation": "Python couldn't find the module '{{$1}}' that your code is trying to import. This could be because the module isn't installed, or there's a typo in the module name.",
        "solution": "Make sure the module '{{$1}}' is installed. You can install it using pip: 'pip install {{$1}}'. Also check for typos in the import statement.",
        "code_example": """
# Installation command:
# pip install {{$1}}

# Then import it:
import {{$1}}
""",
        "related_errors": ["ImportError"],
        "difficulty": "beginner",
    },
    {
        "regex": r"KeyboardInterrupt",
        "title": "Keyboard Interrupt",
        "explanation": "This isn't actually an error, but a signal that the program was deliberately interrupted by the user (usually by pressing Ctrl+C).",
        "solution": "If you intended to stop the program, no action is needed. If this was accidental, simply run the program again. If you want your program to handle interruptions gracefully, you can catch KeyboardInterrupt exceptions.",
        "code_example": """
try:
    # Your long-running code here
    while True:
        process_data()
except KeyboardInterrupt:
    print("Program was interrupted by user")
    # Clean up resources here
    save_progress()
""",
        "difficulty": "beginner",
    },
]

# JavaScript error patterns
JAVASCRIPT_PATTERNS = [
    {
        "regex": r"Uncaught ReferenceError: ([^ ]+) is not defined",
        "title": 'Variable "{{$1}}" Not Defined',
        "explanation": 'JavaScript cannot find a variable named "{{$1}}". This usually means you\'re trying to use a variable before creating it, or you might have a typo in the variable name.',
        "solution": 'Make sure you\'ve defined the variable "{{$1}}" before using it. Check for typos in variable names. Remember that variable names are case-sensitive in JavaScript.',
        "code_example": """
// Incorrect:
console.log(myVariable);  // Error: myVariable is not defined

// Correct:
let myVariable = "Hello World";
console.log(myVariable);  // Now it works!
""",
        "difficulty": "beginner",
    },
    {
        "regex": r"Uncaught TypeError: Cannot read properties? of (null|undefined) \(reading \'([^\']+)\'\)",
        "title": 'Cannot Read Property "{{$2}}" of {{$1}}',
        "explanation": 'Your code is trying to access a property "{{$2}}" on a {{$1}} value. This happens when you try to access properties on variables that are null or undefined.',
        "solution": "Before accessing the property, check if the object exists. You can use optional chaining (?.) in modern JavaScript, the logical AND operator (&&), or a simple if statement.",
        "code_example": """
// Problematic code
const user = null;
console.log(user.name);  // TypeError: Cannot read property 'name' of null

// Solution 1: Use optional chaining (modern JavaScript)
console.log(user?.name);  // Returns undefined instead of throwing an error

// Solution 2: Use logical AND operator
console.log(user && user.name);  // Returns null instead of throwing an error

// Solution 3: Use an if statement
if (user) {
  console.log(user.name);
} else {
  console.log("User not available");
}
""",
        "difficulty": "beginner",
    },
    {
        "regex": r"Uncaught SyntaxError: Unexpected token \)",
        "title": "Unexpected Closing Parenthesis",
        "explanation": 'JavaScript encountered a closing parenthesis ")" that doesn\'t match with an opening parenthesis. This is often caused by mismatched parentheses in your code.',
        "solution": 'Check your code for balanced parentheses, brackets, and braces. Make sure every opening parenthesis "(" has a matching closing parenthesis ")" in the correct order.',
        "code_example": """
// Problematic code
function add(a, b) {
  return (a + b;  // Missing closing parenthesis
}

// Correct code
function add(a, b) {
  return (a + b);  // Balanced parentheses
}

// Common mistake with nested functions or callbacks
document.getElementById("button").addEventListener("click", function() {
  alert("Clicked!");
});  // Make sure to close all parentheses
""",
        "difficulty": "beginner",
    },
    {
        "regex": r"Uncaught RangeError: Maximum call stack size exceeded",
        "title": "Maximum Call Stack Size Exceeded",
        "explanation": "This error occurs when too many function calls are placed on the call stack. It's typically caused by infinite recursion (a function calling itself without a proper exit condition).",
        "solution": "Check for recursive functions and ensure they have a proper termination condition. Look for circular function calls where A calls B, B calls C, and C calls A again. Consider using iteration instead of recursion when appropriate.",
        "code_example": """
// Incorrect (infinite recursion):
function countDown(n) {
  console.log(n);
  countDown(n - 1); // No stopping condition!
}

// Correct:
function countDown(n) {
  console.log(n);
  if (n > 0) { // Base case
    countDown(n - 1);
  }
}
""",
        "related_errors": ["RecursionError", "StackOverflowError"],
        "difficulty": "intermediate",
    },
    {
        "regex": r"Uncaught TypeError: Cannot read propert(?:y|ies) '([^']+)' of (null|undefined)",
        "title": "Cannot Read Property '{{$1}}' of {{$2}}",
        "explanation": "You're trying to access the property '{{$1}}' on a value that is {{$2}}. This means you're trying to use an object that doesn't exist or hasn't been initialized yet.",
        "solution": "Make sure the object exists before trying to access its properties. Add a check to verify the object is not {{$2}} before accessing it.",
        "code_example": """
// Incorrect:
const user = null;
console.log(user.name); // Error: Cannot read property 'name' of null

// Correct:
const user = null;
if (user) {
  console.log(user.name);
} else {
  console.log('User not available');
}

// Modern approach with optional chaining:
console.log(user?.name); // Safely outputs undefined instead of crashing
""",
        "related_errors": ["TypeError"],
        "difficulty": "beginner",
    },
    {
        "regex": r"Uncaught SyntaxError: Unexpected token '([^']+)'",
        "title": "Syntax Error: Unexpected Token '{{$1}}'",
        "explanation": "JavaScript encountered a character '{{$1}}' that it didn't expect at that position. This is often due to missing or mismatched brackets, parentheses, or quotes.",
        "solution": "Check for unbalanced brackets, parentheses, or quotes. Look for missing semicolons or commas. Use a code editor with syntax highlighting to help spot these issues.",
        "code_example": """
// Examples of syntax errors:
// Missing closing parenthesis
if (x === 5 {  // Should be: if (x === 5) {
  doSomething();
}

// Unmatched quotes
const name = 'John;  // Should be: const name = 'John';

// Fix by ensuring all syntax elements are properly matched and closed
""",
        "difficulty": "beginner",
    },
    {
        "regex": r"Uncaught TypeError: Cannot set propert(?:y|ies) \'([^\']+)\' of (null|undefined)",
        "title": 'Cannot Set Property "{{$1}}" of {{$2}}',
        "explanation": "You're trying to set the property \"{{$1}}\" on a {{$2}} value. This happens when you try to modify properties on variables that don't have any value.",
        "solution": "Make sure the object exists and is not {{$2}} before trying to set its properties. Check that the object has been properly initialized.",
        "code_example": """
// Incorrect:
let user;
user.name = "John"; // Error: Cannot set property 'name' of undefined

// Correct:
let user = {}; // Initialize as an empty object first
user.name = "John"; // Now it works
""",
    },
    {
        "regex": r"Uncaught Error: Request failed with status code (\d+)",
        "title": "API Request Failed with Status Code {{$1}}",
        "explanation": "Your HTTP request failed with status code {{$1}}. This usually indicates a problem with the request or the server.",
        "solution": "Check what status code {{$1}} means. Common codes: 404 (not found), 401 (unauthorized), 500 (server error). Ensure your API endpoint is correct and you have the necessary permissions.",
        "code_example": """
// Better error handling:
axios.get('/api/data')
  .then(response => {
    // Handle successful response
    console.log(response.data);
  })
  .catch(error => {
    if (error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      console.log('Status:', error.response.status);
      console.log('Data:', error.response.data);
    } else if (error.request) {
      // The request was made but no response was received
      console.log('No response received');
    } else {
      // Something happened in setting up the request
      console.log('Error:', error.message);
    }
  });
""",
    },
    {
        "regex": r"Uncaught TypeError: ([^\']+) is not iterable",
        "title": '"{{$1}}" is Not Iterable',
        "explanation": "You're trying to use \"{{$1}}\" in a loop or iteration context (like for...of), but it's not an iterable object. Only arrays, strings, and certain objects are iterable in JavaScript.",
        "solution": 'Make sure "{{$1}}" is an iterable type (like an array) before trying to iterate over it. You might need to check if it exists and is the right type first.',
        "code_example": """
// Incorrect:
const data = null;
for (const item of data) { // Error: data is not iterable
  console.log(item);
}

// Correct:
const data = null;
if (data && typeof data[Symbol.iterator] === 'function') {
  for (const item of data) {
    console.log(item);
  }
} else {
  console.log('Data is not iterable or is null/undefined');
}

// Or simply:
const data = null;
const safeData = data || [];
for (const item of safeData) {
  console.log(item);
}
""",
    },
    {
        "regex": r"TypeError: Cannot read propert(?:y|ies) \'([^\']+)\' of ([^\']+)",
        "title": 'Cannot Read Property "{{$1}}"',
        "explanation": 'JavaScript cannot read the property "{{$1}}" because the object is {{$2}}. This usually happens when trying to access properties on null or undefined values.',
        "solution": "Check that your object exists and is properly initialized before trying to access its properties.",
        "code_example": """
// Incorrect:
const obj = null;
console.log(obj.length);  // Error: Cannot read property 'length' of null

// Correct:
const obj = null;
if (obj !== null && obj !== undefined) {
    console.log(obj.length);
} else {
    console.log('Object is null or undefined');
}
""",
        "difficulty": "beginner",
    },
    {
        "regex": r"ReferenceError: ([^\']+) is not defined",
        "title": 'Variable "{{$1}}" Not Defined',
        "explanation": "JavaScript cannot find a variable named \"{{$1}}\". This means you're trying to use a variable that hasn't been declared.",
        "solution": "Make sure you declare the variable before using it. Check for typos in variable names.",
        "code_example": """
// Incorrect:
console.log(someVar);  // Error: someVar is not defined

// Correct:
let someVar = 'Hello';
console.log(someVar);  // Works!
""",
        "difficulty": "beginner",
    },
    {
        "regex": r"TypeError: (.*) is not a function",
        "title": "TypeError: Not a Function",
        "explanation": "Your code is attempting to call something that is not a function. This might happen if you mistype the function name or if a variable expected to be a function is not.",
        "solution": "Ensure that the variable is actually a function. Check for typos and confirm its definition.",
        "code_example": """
// Incorrect:
var result = myVar();
 
// Correct:
function myVar() { return 42; }
var result = myVar();
""",
        "difficulty": "beginner"
    },
]

# HTML error patterns
HTML_PATTERNS = [
    {
        "regex": r"Unclosed tag \'([^\']+)\'",
        "title": "Unclosed HTML Tag: <{{$1}}>",
        "explanation": "You have an opening <{{$1}}> tag, but you're missing the closing </{{$1}}> tag. HTML tags must be properly closed.",
        "solution": "Add the missing closing tag </{{$1}}> in the appropriate place. Make sure your tags are properly nested.",
        "code_example": """
<!-- Incorrect -->
<div>
  <p>Some text
</div>

<!-- Correct -->
<div>
  <p>Some text</p>
</div>
""",
    },
    {
        "regex": r"Invalid character in markup: \'([^\']+)\'",
        "title": "Invalid Character in HTML",
        "explanation": 'The character "{{$1}}" is not allowed in HTML where you\'ve placed it. This often happens with special characters like "&", "<", or ">".',
        "solution": 'Replace special characters with their HTML entities: "&" becomes "&amp;", "<" becomes "&lt;", ">" becomes "&gt;".',
        "code_example": """
<!-- Incorrect -->
<p>This code: if (x < 10) will display an error</p>

<!-- Correct -->
<p>This code: if (x &lt; 10) will display correctly</p>
""",
    },
    {
        "regex": r"Error parsing HTML: Unexpected end tag \(([^\)]+)\)",
        "title": "Unexpected End Tag: </{{$1}}>",
        "explanation": "You have a closing </{{$1}}> tag that doesn't match any opening tag. Either you have an extra closing tag, or you're missing an opening tag.",
        "solution": "Remove the extra closing tag, or add the matching opening tag. Make sure your tags are properly nested.",
        "code_example": """
<!-- Incorrect -->
<div>
  <p>Some text</div>
</p>  <!-- Unexpected end tag </p> -->

<!-- Correct -->
<div>
  <p>Some text</p>
</div>
""",
    },
    {
        "regex": r'Error: Attribute "([^"]+)" not allowed on element "([^"]+)" at this point',
        "title": "Invalid Attribute: {{$1}} on {{$2}}",
        "explanation": "You're using the attribute \"{{$1}}\" on a <{{$2}}> element, but that attribute isn't valid for this element.",
        "solution": "Remove the invalid attribute, or make sure you're using the correct element for what you're trying to do.",
        "code_example": """
<!-- Incorrect -->
<div href="https://example.com">Click me</div>

<!-- Correct -->
<a href="https://example.com">Click me</a>
""",
    },
    {
        "regex": r'Error: End tag "([^"]+)" was not found',
        "title": "Missing End Tag: </{{$1}}>",
        "explanation": "You have an opening <{{$1}}> tag, but you never close it with </{{$1}}>. All HTML tags must be properly closed.",
        "solution": "Add the missing </{{$1}}> closing tag in the appropriate place.",
        "code_example": """
<!-- Incorrect -->
<div>
  <p>Some text

<!-- Correct -->
<div>
  <p>Some text</p>
</div>
""",
    },
    {
        "regex": r'Error: ID "([^"]+)" is already defined',
        "title": "Duplicate HTML ID: {{$1}}",
        "explanation": 'You have multiple HTML elements with the same id "{{$1}}". HTML IDs must be unique within the entire document.',
        "solution": "Use unique IDs for each element or consider using classes instead if you need to apply the same styling or behavior to multiple elements.",
        "code_example": """
<!-- Problematic HTML with duplicate IDs -->
<div id="container">
  <p id="text">First paragraph</p>
  <p id="text">Second paragraph</p>  <!-- Duplicate ID -->
</div>

<!-- Corrected HTML with unique IDs -->
<div id="container">
  <p id="text1">First paragraph</p>
  <p id="text2">Second paragraph</p>
</div>

<!-- Alternative: Using classes instead of IDs -->
<div class="container">
  <p class="text">First paragraph</p>
  <p class="text">Second paragraph</p>  <!-- Using class is fine for multiple elements -->
</div>
""",
    },
    {
        "regex": r'Error: Element "([^"]+)" is missing required attribute "([^"]+)"',
        "title": "Missing Required Attribute: {{$2}} in {{$1}} Element",
        "explanation": 'The HTML element <{{$1}}> is missing a required attribute "{{$2}}". Some HTML elements have attributes that are necessary for them to function correctly.',
        "solution": 'Add the required "{{$2}}" attribute to your <{{$1}}> element.',
        "code_example": """
<!-- Problematic HTML -->
<img src="">  <!-- Missing alt attribute -->
<input type="text">  <!-- Missing name attribute for form submission -->

<!-- Corrected HTML -->
<img src="image.jpg" alt="Description of the image">
<input type="text" name="username">

<!-- Common required attributes for elements -->
<a href="https://example.com">Link text</a>  <!-- href is required for links -->
<form action="/submit">...</form>  <!-- action is required for forms -->
""",
    },
    {
        "regex": r'Error: Unexpected token "<\/([^>]+)>" in <([^>]+)>',
        "title": "Mismatched HTML Tags: </{{$1}}> in <{{$2}}>",
        "explanation": "You have a closing tag </{{$1}}> that doesn't match the expected closing tag for <{{$2}}>. HTML tags must be properly nested and each opening tag must have a matching closing tag.",
        "solution": "Fix the nesting of your HTML tags. Make sure that tags are closed in the reverse order they were opened.",
        "code_example": """
<!-- Problematic HTML with mismatched tags -->
<div><p>Some text</div></p>  <!-- Incorrect nesting -->

<!-- Corrected HTML -->
<div><p>Some text</p></div>  <!-- Correct nesting -->

<!-- Another example of incorrect nesting -->
<ul>
  <li>Item 1
  <li>Item 2
</ul>

<!-- Properly closed tags -->
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>
""",
    },
    {
        "regex": r"Error: Element ([^ ]+) not allowed as child of element ([^ ]+)",
        "title": "HTML Tag Nesting Error",
        "explanation": "The element {{$1}} is not allowed as a child of {{$2}}. This means your HTML structure is incorrect and elements are nested improperly.",
        "solution": "Revisit the HTML specification for allowed element nesting or restructure your HTML so that the element {{$1}} is placed appropriately.",
        "code_example": """
<!-- Incorrect -->
<ul>
  <p>List item</p>
</ul>

<!-- Correct -->
<ul>
  <li><p>List item</p></li>
</ul>
""",
        "difficulty": "beginner"
    },
]

# CSS error patterns
CSS_PATTERNS = [
    {
        "regex": r"Unknown property: \'([^\']+)\'",
        "title": 'Unknown CSS Property: "{{$1}}"',
        "explanation": "The CSS property \"{{$1}}\" doesn't exist or isn't recognized. This might be a typo, or you might be using a newer property that's not supported in all browsers.",
        "solution": "Check for typos in the property name. If you're using a newer property, consider adding appropriate vendor prefixes or a fallback.",
        "code_example": """
/* Incorrect */
.element {
  colour: red;  /* Typo: "colour" instead of "color" */
}

/* Correct */
.element {
  color: red;
}
""",
    },
    {
        "regex": r"Invalid value for property \'([^\']+)\': \'([^\']+)\'",
        "title": "Invalid Value for CSS Property",
        "explanation": 'The value "{{$2}}" is not valid for the CSS property "{{$1}}". Each CSS property only accepts specific types of values.',
        "solution": 'Check the documentation for the "{{$1}}" property to see what values it accepts. Fix the value accordingly.',
        "code_example": """
/* Incorrect */
.element {
  width: 100px%;  /* Can't mix units like this */
}

/* Correct */
.element {
  width: 100%;
  /* or */
  width: 100px;
}
""",
    },
    {
        "regex": r"Invalid property value: ([^:]+): ([^\n]+)",
        "title": "Invalid CSS Value: {{$2}}",
        "explanation": 'The value "{{$2}}" is not valid for the CSS property "{{$1}}". Each CSS property expects values in a specific format.',
        "solution": 'Check the syntax for the "{{$1}}" property. Make sure you\'re using valid values and formats.',
        "code_example": """
/* Incorrect */
.element {
  {{$1}}: {{$2}};
}

/* Example of correct syntax (adjust for your specific property) */
.element {
  color: #336699;  /* Use valid color format */
  width: 100px;    /* Include units for dimensions */
}
""",
    },
    {
        "regex": r"Error: unexpected token \'([^\']+)\'",
        "title": "Unexpected Token in CSS: {{$1}}",
        "explanation": 'CSS encountered an unexpected character or symbol "{{$1}}" while parsing your styles. This usually indicates a syntax error.',
        "solution": 'Check your CSS syntax around where "{{$1}}" appears. Look for missing semicolons, brackets, or quotes.',
        "code_example": """
/* Incorrect */
.element {
  color: red
  background-color: blue;  /* Missing semicolon after "red" */
}

/* Correct */
.element {
  color: red;
  background-color: blue;
}
""",
    },
    {
        "regex": r"Unexpected end of input",
        "title": "Unexpected End of CSS",
        "explanation": "Your CSS ended abruptly, likely due to an unclosed bracket, parenthesis, or quote.",
        "solution": "Check your CSS for any unclosed structures. Make sure all opening braces { have matching closing braces }.",
        "code_example": """
/* Incorrect */
.element {
  color: red;
  padding: 10px;
  /* Missing closing brace */

/* Correct */
.element {
  color: red;
  padding: 10px;
}
""",
    },
    {
        "regex": r'Property "([^"]+)" doesn\'t exist',
        "title": "Unknown CSS Property: {{$1}}",
        "explanation": "The CSS property \"{{$1}}\" doesn't exist in the CSS specification or it's misspelled.",
        "solution": "Check for typos in the property name. Make sure you're using standard CSS properties or appropriate vendor prefixes for experimental properties.",
        "code_example": """
/* Problematic CSS */
.element {
  paddin: 10px;  /* Typo: should be "padding" */
  font-weight: heavyer;  /* Invalid value, should be "bold", "normal", or a number */
}

/* Corrected CSS */
.element {
  padding: 10px;
  font-weight: bold;
}
""",
    },
    {
        "regex": r"Unterminated string constant",
        "title": "Unterminated String in CSS",
        "explanation": "You have a string in your CSS (such as in a url() or content property) that is missing its closing quote mark.",
        "solution": "Add the missing closing quote (either single or double quote) to complete the string.",
        "code_example": """
/* Problematic CSS with unterminated string */
.element {
  background-image: url('image.jpg;  /* Missing closing quote */
  content: "Hello world;  /* Missing closing quote */
}

/* Corrected CSS */
.element {
  background-image: url('image.jpg');
  content: "Hello world";
}
""",
    },
    {
        "regex": r"Unexpected @([^ ]+) rule",
        "title": "Invalid or Misplaced CSS @{{$1}} Rule",
        "explanation": "You're using an @{{$1}} rule that either doesn't exist or is placed in an invalid location in your CSS.",
        "solution": "Check the syntax and placement of the @{{$1}} rule. Most at-rules need to be at the top level of your CSS, not nested inside selectors.",
        "code_example": """
/* Problematic CSS with misplaced at-rule */
.container {
  @media (max-width: 600px) {  /* @media can't be nested inside a selector */
    width: 100%;
  }
}

/* Corrected CSS */
.container {
  width: 80%;
}

@media (max-width: 600px) {
  .container {
    width: 100%;
  }
}
""",
    },
    {
        "regex": r"Expected ([^,]+), found \'([^\']+)\'",
        "title": "CSS Syntax Error: Expected {{$1}}",
        "explanation": 'CSS expected {{$1}} at a certain point in your code, but found "{{$2}}" instead. This indicates a syntax error in your CSS.',
        "solution": "Fix the syntax error by providing the expected {{$1}} where needed. Check for missing punctuation like semicolons, brackets, or colons.",
        "code_example": """
/* Problematic CSS with syntax error */
.element {
  color: red
  background-color: blue;  /* Missing semicolon after "red" */
}

/* Corrected CSS */
.element {
  color: red;
  background-color: blue;
}

/* Another common error */
.element {
  padding: 10px
}  /* Missing semicolon and/or closing brace */

/* Corrected */
.element {
  padding: 10px;
}
""",
    },
    {
        "regex": r"Error: unclosed comment",
        "title": "Unclosed CSS Comment",
        "explanation": "A CSS comment was not properly closed with '*/'. This can cause the stylesheet to fail to compile.",
        "solution": "Ensure that all CSS comments are properly closed. Each comment should start with /* and end with */.",
        "code_example": """
/* Incorrect:
body { color: red;  /* missing closing comment

Correct:
body { color: red; }  /* properly closed comment */
""",
        "difficulty": "beginner"
    },
]

# General error patterns (not specific to any language)
GENERAL_PATTERNS = [
    {
        "regex": r"(\d+) is not a valid port number",
        "title": "Invalid Port Number: {{$1}}",
        "explanation": "The port number {{$1}} is not valid. Port numbers must be between 0 and 65535.",
        "solution": "Choose a port number between 0 and 65535. Common ports for development servers are 3000, 5000, or 8000. Make sure the port is not already in use by another application.",
        "code_example": """
# Example for a Node.js server:
const express = require('express');
const app = express();
const PORT = 3000; // Use a valid port between 0-65535

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
""",
    },
    {
        "regex": r"Permission denied",
        "title": "Permission Denied",
        "explanation": "Your program doesn't have the necessary permissions to perform an operation, such as accessing a file, connecting to a port, or modifying system settings.",
        "solution": "Check file or directory permissions. You might need to run your program with elevated privileges (as administrator/sudo), or modify the permissions of the resource you're trying to access.",
        "code_example": """
# For file permission issues:
# Linux/macOS:
chmod 644 filename  # Read/write for owner, read for others
chmod 755 directory  # Executable bit needed for directories

# For running with elevated privileges (use with caution):
# Linux/macOS:
sudo python script.py

# Windows (run Command Prompt as Administrator):
python script.py
""",
    },
    {
        "regex": r"Address already in use",
        "title": "Address Already in Use",
        "explanation": "The network address (usually an IP address and port) that your program is trying to use is already being used by another program.",
        "solution": "Choose a different port number, or stop the other program that's using the port. You can use task manager or process tools to find and stop the other program.",
        "code_example": """
# Finding processes using a port:
# Linux/macOS:
lsof -i :3000  # Replace 3000 with your port number

# Windows:
netstat -ano | findstr :3000  # Replace 3000 with your port number

# In your code, try using a different port:
const PORT = 3001;  // Try a different port
""",
    },
    {
        "regex": r"Connection refused",
        "title": "Connection Refused",
        "explanation": "Your program tried to connect to a server or service, but the connection was actively refused. This usually means the server is not running, or it's running but not listening on the expected port.",
        "solution": "Make sure the server or service you're trying to connect to is running. Check that you're using the correct host and port. If it's your own server, start it. If it's a remote service, check your internet connection.",
        "code_example": """
# Check if you can connect to the service:
# Using curl:
curl http://localhost:3000

# If it's your own server, make sure it's running:
# Start a Node.js server:
node server.js

# Start a Python Flask server:
python app.py
""",
    },
    {
        "regex": r"Timeout exceeded",
        "title": "Connection Timeout",
        "explanation": "Your program tried to connect to a server or service, but the connection attempt took too long and timed out. This could mean the server is down, overloaded, or there's a network issue.",
        "solution": "Check your internet connection. Make sure the server is up and running. Consider increasing the timeout value in your code if the server is known to be slow. If you're connecting to your own server, check server logs for performance issues.",
        "code_example": """
// JavaScript example with increased timeout:
fetch('https://api.example.com/data', {
  timeout: 10000  // 10 seconds instead of default
})
.then(response => response.json())
.catch(error => console.error('Fetch error:', error));

# Python example with increased timeout:
import requests
try:
    response = requests.get('https://api.example.com/data', timeout=10)
    data = response.json()
except requests.exceptions.Timeout:
    print("Request timed out. Server might be slow or down.")
""",
    },
    {
        "regex": r"Memory limit exceeded",
        "title": "Memory Limit Exceeded",
        "explanation": "Your program is trying to use more memory than is allowed or available. This can happen with large data structures, infinite loops that keep creating new objects, or memory leaks.",
        "solution": "Optimize your code to use less memory. Avoid creating unnecessarily large arrays or objects. Make sure you don't have infinite loops. Consider processing data in smaller chunks instead of all at once.",
        "code_example": """
# Instead of loading an entire file into memory:

# Bad approach (loads entire file):
with open("large_file.txt", "r") as file:
    content = file.read()  # Loads everything into memory
    # Process content...

# Better approach (process line by line):
with open("large_file.txt", "r") as file:
    for line in file:  # Reads one line at a time
        # Process line...
""",
    },
]

# Java error patterns
JAVA_PATTERNS = [
    {
        "regex": r"cannot find symbol\s*\n\s*symbol:\s*(.*)\s*\n\s*location:\s*(.*)",
        "title": "Java Symbol Not Found Error",
        "explanation": "This error occurs when Java cannot find a referenced symbol (variable, method, class) in the specified location. The compiler is looking for {{$1}} in {{$2}} but it can't find it.",
        "solution": "Check for typos in the symbol name. Make sure the symbol is properly declared and accessible from the location where it's being used. Verify that all necessary imports are present.",
        "difficulty": "beginner",
        "code_example": """
// Example fix for a common 'cannot find symbol' error
import java.util.ArrayList; // Missing import

public class Example {
    public void method() {
        ArrayList<String> list = new ArrayList<>(); // Now it works
    }
}
"""
    },
    {
        "regex": r"incompatible types: (.*) cannot be converted to (.*)",
        "title": "Java Type Conversion Error",
        "explanation": "Java is strongly typed and cannot automatically convert between incompatible types. You're trying to assign a value of type {{$1}} to a variable of type {{$2}}.",
        "solution": "You need to either use compatible types or explicitly cast the value to the required type if it's a valid conversion. In some cases, you might need to use appropriate conversion methods.",
        "difficulty": "beginner",
        "code_example": """
// Example fix for incompatible types
String numberStr = "123";
int number = Integer.parseInt(numberStr); // Convert String to int correctly
"""
    },
    {
        "regex": r"java\.lang\.NullPointerException: Cannot (invoke|read|call|perform) \"([^\"]+)\" because \"([^\"]+)\" is null",
        "title": "Null Pointer Exception",
        "explanation": "You're trying to {{$1}} '{{$2}}' on '{{$3}}', but '{{$3}}' is null. This happens when you try to use a method or access a property on an object that doesn't exist.",
        "solution": "Always check if an object is null before using it. Initialize objects properly or provide default values/behaviors for null cases.",
        "difficulty": "beginner",
        "code_example": """
// Incorrect:
String name = null;
System.out.println(name.length()); // Error: NullPointerException

// Correct:
String name = null;
if (name != null) {
    System.out.println(name.length());
} else {
    System.out.println("Name is null");
}

// Java 8+ approach with Optional:
Optional<String> optName = Optional.ofNullable(name);
optName.ifPresent(n -> System.out.println(n.length()));
"""
    },
    {
        "regex": r"java\.lang\.ArrayIndexOutOfBoundsException: Index (\d+) out of bounds for length (\d+)",
        "title": "Array Index Out of Bounds",
        "explanation": "You're trying to access index {{$1}} in an array that only has {{$2}} elements (indexes 0 to {{$2-1}}). Array indexes in Java start at 0, not 1.",
        "solution": "Check your array access logic. Make sure loop conditions don't exceed array bounds. Use array.length to determine the size of the array rather than hardcoding values.",
        "difficulty": "beginner",
        "code_example": """
// Incorrect:
int[] numbers = new int[5]; // Has indexes 0-4
System.out.println(numbers[5]); // Error: Index 5 is out of bounds

// Correct:
int[] numbers = new int[5];
for (int i = 0; i < numbers.length; i++) {
    // Safe access within bounds
    numbers[i] = i;
}
"""
    },
    {
        "regex": r"java\.lang\.ClassCastException: ([^\s]+) cannot be cast to ([^\s]+)",
        "title": "Invalid Class Cast",
        "explanation": "You're trying to cast an object of type {{$1}} to type {{$2}}, but these types are not compatible for casting. An object can only be cast to its own type or a supertype/interface it implements.",
        "solution": "Check your object types and make sure you're only casting to compatible types. Use 'instanceof' to verify the object's type before casting.",
        "difficulty": "intermediate", 
        "code_example": """
// Incorrect:
Object obj = "Hello";
Integer num = (Integer) obj; // Error: String cannot be cast to Integer

// Correct:
Object obj = "Hello";
if (obj instanceof String) {
    String str = (String) obj; // Safe cast
    System.out.println(str);
} else if (obj instanceof Integer) {
    Integer num = (Integer) obj;
    System.out.println(num);
}
"""
    },
    {
        "regex": r"exception in thread \"main\" java\.lang\.StackOverflowError",
        "title": "Stack Overflow Error",
        "explanation": "This error occurs when the Java call stack overflows due to too many method calls. This is typically caused by infinite recursion (a method that keeps calling itself without a proper stopping condition).",
        "solution": "Ensure recursive methods have a proper base case that will stop the recursion. Consider using iteration instead of recursion for deeply nested operations.",
        "difficulty": "intermediate",
        "code_example": """
// Incorrect (infinite recursion):
public int factorial(int n) {
    return n * factorial(n - 1); // No base case!
}

// Correct:
public int factorial(int n) {
    if (n <= 1) { // Base case
        return 1;
    }
    return n * factorial(n - 1);
}

// Alternative iterative approach:
public int factorial(int n) {
    int result = 1;
    for (int i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}
"""
    },
    {
        "regex": r"java\.lang\.NumberFormatException: For input string: \"([^\"]+)\"",
        "title": "Number Format Exception",
        "explanation": "Java couldn't convert the string \"{{$1}}\" to a number. This happens when you try to parse a string that doesn't represent a valid number.",
        "solution": "Make sure the string contains only valid numerical characters for the number type you're trying to parse. Add validation before attempting to parse strings to numbers.",
        "difficulty": "beginner",
        "code_example": """
// Incorrect:
String notANumber = "abc123";
int number = Integer.parseInt(notANumber); // Error: NumberFormatException

// Correct with validation:
String input = "abc123";
try {
    int number = Integer.parseInt(input);
    System.out.println("Number: " + number);
} catch (NumberFormatException e) {
    System.out.println("Invalid number format: " + input);
}

// Or check if it's a valid number first:
String input = "abc123";
if (input.matches("\\d+")) {
    int number = Integer.parseInt(input);
    System.out.println("Number: " + number);
} else {
    System.out.println("Not a valid number");
}
"""
    }
]

# Ruby error patterns
RUBY_PATTERNS = [
    {
        "regex": r"NameError: uninitialized constant (.*)",
        "title": "Ruby Uninitialized Constant Error",
        "explanation": "This error occurs when Ruby tries to use a constant ({{$1}}) that hasn't been defined yet. Constants in Ruby are typically class or module names that start with a capital letter.",
        "solution": "Make sure the class or module is properly defined and the name is spelled correctly. Check that you've required the necessary files that define this constant.",
        "difficulty": "beginner",
        "code_example": """
# Example fix for uninitialized constant error
require 'my_module'  # Add the missing require statement

# Or define the missing constant
module MyModule
  class MyClass
    # Class implementation
  end
end
"""
    },
    {
        "regex": r"NoMethodError: undefined method `(.*)' for (.*)",
        "title": "Ruby Undefined Method Error",
        "explanation": "This error occurs when you try to call a method ({{$1}}) on an object ({{$2}}) that doesn't have that method defined.",
        "solution": "Check that you're calling the right method on the right object. Make sure the object is of the expected type. You may need to define the method or use a different method.",
        "difficulty": "beginner",
        "code_example": """
# Example fix for undefined method error
# Instead of:
# some_variable.undefined_method

# Make sure the variable is the right type
puts some_variable.class  # Check what kind of object it is

# Then use a method that exists for that type
some_variable.to_s  # For example, convert to string
"""
    },
    {
        "regex": r"ArgumentError: wrong number of arguments \(given (\d+), expected (\d+)\)",
        "title": "Ruby Wrong Number of Arguments Error",
        "explanation": "This error occurs when you call a method with {{$1}} arguments, but it expects {{$2}} arguments.",
        "solution": "Check the method's documentation to see how many arguments it expects. Adjust your code to provide the correct number of arguments.",
        "difficulty": "beginner",
        "code_example": """
# Example fix for wrong number of arguments
# Instead of:
# my_method(arg1, arg2, arg3)  # Too many arguments

# Check the method definition
def my_method(arg1, arg2)
  # Method only expects 2 arguments
end

# Correct the call
my_method(arg1, arg2)  # Correct number of arguments
"""
    },
    {
        "regex": r"SyntaxError: (.*)",
        "title": "Ruby Syntax Error",
        "explanation": "This error occurs when Ruby can't understand your code because it doesn't follow the rules of Ruby syntax. Specifically: {{$1}}",
        "solution": "Check the indicated line for syntax errors like missing end keywords, mismatched brackets, or incorrect punctuation.",
        "difficulty": "beginner",
        "code_example": """
# Common syntax errors in Ruby:

# Missing 'end' keyword
def my_method
  if condition
    # code
  end
end  # Add missing 'end'

# Mismatched brackets
hash = { key: 'value' }  # Correct bracket matching

# Missing commas in arrays or hashes
array = [1, 2, 3]  # Commas between elements
"""
    },
    {
        "regex": r"undefined local variable or method `(.*)' for (.*)",
        "title": "Ruby Undefined Variable Error",
        "explanation": "This error occurs when you try to use a variable or method ({{$1}}) that hasn't been defined in the current scope.",
        "solution": "Make sure you've defined the variable before using it. Check for typos in the variable name. If it's a method, ensure it's defined in the class or module you're using.",
        "difficulty": "beginner",
        "code_example": """
# Define variables before using them
my_variable = "Hello"  # Define the variable
puts my_variable      # Then use it

# For class variables, make sure they're defined
class MyClass
  def initialize
    @instance_var = "value"  # Define instance variable
  end
  
  def my_method
    puts @instance_var  # Now it's defined in this scope
  end
end
"""
    },
    {
        "regex": r"LoadError: cannot load such file -- (.*)",
        "title": "Ruby Load Error",
        "explanation": "This error occurs when Ruby can't find the file or library ({{$1}}) that you're trying to require or load.",
        "solution": "Check that the gem or file you're trying to load is installed and the path is correct. You may need to install the gem with 'gem install' or adjust your load path.",
        "difficulty": "intermediate",
        "code_example": """
# Fix for LoadError
# Install missing gems
# $ gem install missing_gem

# Or fix the require statement
require 'correct_name'

# Or specify the full path
require_relative '../path/to/my_file'
"""
    },
    {
        "regex": r"TypeError: (.*)",
        "title": "Ruby Type Error",
        "explanation": "This error occurs when you try to perform an operation on an object that doesn't support that operation. Specifically: {{$1}}",
        "solution": "Check the types of objects you're working with. You may need to convert objects to the correct type before performing operations on them.",
        "difficulty": "intermediate",
        "code_example": """
# Fix for TypeError
# Convert objects to appropriate types before operations
number = "10".to_i     # Convert string to integer
string = 10.to_s       # Convert integer to string
array = [1, 2, 3]
hash = { a: 1, b: 2 }

# Check object type before operations
if object.is_a?(String)
  # String operations
elsif object.is_a?(Array)
  # Array operations
end
"""
    },
    {
        "regex": r"ZeroDivisionError: divided by 0",
        "title": "Ruby Division by Zero Error",
        "explanation": "This error occurs when you try to divide a number by zero, which is mathematically undefined.",
        "solution": "Add a check to prevent division by zero. Validate denominators before performing division operations.",
        "difficulty": "beginner",
        "code_example": """
# Incorrect:
result = 10 / 0  # Error: divided by 0

# Correct:
denominator = 0
if denominator != 0
  result = 10 / denominator
else
  puts "Cannot divide by zero"
  result = nil  # or some default value
end

# Alternative with exception handling:
begin
  result = 10 / denominator
rescue ZeroDivisionError
  puts "Cannot divide by zero"
  result = nil
end
"""
    },
    {
        "regex": r"Errno::ENOENT: No such file or directory - (.*)",
        "title": "Ruby File Not Found Error",
        "explanation": "This error occurs when Ruby tries to access a file ({{$1}}) that doesn't exist at the specified path.",
        "solution": "Check that the file exists at the specified path. Make sure you're using the correct file name and path. You may need to create the file if it doesn't exist.",
        "difficulty": "beginner",
        "code_example": """
# Check if file exists before opening
file_path = "path/to/file.txt"

if File.exist?(file_path)
  File.open(file_path, "r") do |file|
    # File operations
  end
else
  puts "File doesn't exist!"
  # Create the file or handle the error
end
"""
    },
    {
        "regex": r"RuntimeError: (.*)",
        "title": "Ruby Runtime Error",
        "explanation": "This is a generic error that occurs while your program is running. Specifically: {{$1}}",
        "solution": "The solution depends on the specific error message. Check the error details and look at where the error occurred in your code. You may need to add error handling with begin/rescue blocks.",
        "difficulty": "intermediate",
        "code_example": """
# Use begin/rescue for error handling
begin
  # Code that might raise an error
  result = risky_operation()
rescue => e
  # Handle the error
  puts "Error occurred: #{e.message}"
  # Provide fallback or recovery code
end
"""
    },
    {
        "regex": r"NoMethodError: undefined method `([^']+)' for ([^:]+):([^:]+)",
        "title": "Undefined Method '{{$1}}' for {{$2}}",
        "explanation": "You're trying to call a method named '{{$1}}' on an object of type {{$3}}, but that method doesn't exist for this type of object.",
        "solution": "Make sure you're calling the correct method for this object type. Check the documentation to see what methods are available. Check for typos in method names.",
        "difficulty": "beginner",
        "code_example": """
# Incorrect:
number = 42
number.each { |n| puts n }  # Error: undefined method 'each' for Integer

# Correct:
number = 42
puts number  # Just print the number directly

# Or if you meant to iterate over a range:
(1..number).each { |n| puts n }  # Works on a Range object
"""
    },
]

# Update ERROR_PATTERNS dictionary to include Ruby
ERROR_PATTERNS = {
    "python": PYTHON_PATTERNS,
    "javascript": JAVASCRIPT_PATTERNS,
    "html": HTML_PATTERNS,
    "css": CSS_PATTERNS,
    "java": JAVA_PATTERNS,
    "ruby": RUBY_PATTERNS,
    "general": GENERAL_PATTERNS,
}
