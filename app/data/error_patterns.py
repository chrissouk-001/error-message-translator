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
        'regex': r'NameError: name \'([^\']+)\' is not defined',
        'title': 'Variable "{{$1}}" Not Defined',
        'explanation': 'Python cannot find a variable named "{{$1}}". This usually means you\'re trying to use a variable before creating it, or you might have a typo in the variable name.',
        'solution': 'Make sure you\'ve defined the variable "{{$1}}" before using it. Check for typos in variable names.',
        'code_example': '''
# Incorrect:
result = {{$1}} + 10  # Error: {{$1}} doesn't exist yet

# Correct:
{{$1}} = 5
result = {{$1}} + 10  # Now it works!
''',
        'related_errors': ['UnboundLocalError'],
        'difficulty': 'beginner'
    },
    {
        'regex': r'TypeError: \'([^\']+)\' object is not ([^\']+)',
        'title': 'Type Error: Can\'t {{$2}} This Object',
        'explanation': 'You\'re trying to {{$2}} a "{{$1}}" object, but that operation isn\'t allowed for this type of data.',
        'solution': 'Check what type of data you\'re working with and make sure the operation is valid for that type. You might need to convert the data to a different type first.',
        'code_example': '''
# Example (if trying to iterate over an integer):
# Incorrect:
number = 42
for digit in number:  # Error: 'int' object is not iterable
    print(digit)

# Correct:
number = 42
for digit in str(number):  # Convert to string first
    print(digit)
''',
        'difficulty': 'beginner'
    },
    {
        'regex': r'SyntaxError: invalid syntax',
        'title': 'Invalid Syntax',
        'explanation': 'Python can\'t understand your code because there\'s a syntax error. This could be due to missing parentheses, quotes, colons, or other syntax elements.',
        'solution': 'Check your code for syntax errors like missing parentheses, brackets, quotes, or colons. Look for misplaced operators or keywords.',
        'code_example': '''
# Examples of invalid syntax:
if x = 5:  # Error: using = instead of ==
    print(x)
    
# Correct:
if x == 5:
    print(x)
''',
        'difficulty': 'beginner'
    },
    {
        'regex': r'IndentationError: ([^\']+)',
        'title': 'Indentation Error',
        'explanation': 'Python uses indentation to define code blocks. Your code has inconsistent indentation, which confuses the Python interpreter.',
        'solution': 'Fix the indentation in your code. Use either spaces or tabs consistently (spaces are recommended). Each level of indentation should be the same number of spaces (usually 4).',
        'code_example': '''
# Incorrect indentation:
def function():
    x = 1
  y = 2  # Error: inconsistent indentation
    
# Correct indentation:
def function():
    x = 1
    y = 2
''',
        'difficulty': 'beginner'
    },
    {
        'regex': r'ImportError: No module named ([^\']+)',
        'title': 'Module Not Found: {{$1}}',
        'explanation': 'Python tried to import the module "{{$1}}" but couldn\'t find it. This usually means the module isn\'t installed or isn\'t in your Python path.',
        'solution': 'Install the missing module using pip: `pip install {{$1}}`. If it\'s a local module, make sure the file exists and is in a directory that Python can find.',
        'code_example': '''
# Terminal command to install the module:
# pip install {{$1}}

# If it's a local module, make sure it's in the correct path:
import {{$1}}  # This will work once the module is installed or found
''',
        'difficulty': 'beginner'
    },
    {
        'regex': r'AttributeError: \'([^\']+)\' object has no attribute \'([^\']+)\'',
        'title': 'Attribute Error: No "{{$2}}" in {{$1}}',
        'explanation': 'You\'re trying to access an attribute or method called "{{$2}}" on a {{$1}} object, but {{$1}} doesn\'t have this attribute or method.',
        'solution': 'Check the documentation for the {{$1}} type to see what attributes and methods it has. Check for typos in the attribute name.',
        'code_example': '''
# Example (if trying to call a non-existent method on a string):
text = "Hello"
result = text.capitalize()  # This works: "Hello"
result = text.reverse()  # Error: strings don't have a reverse() method

# Correct (for strings):
text = "Hello"
result = text[::-1]  # Use slicing to reverse a string: "olleH"
''',
        'difficulty': 'intermediate'
    },
    {
        'regex': r'ZeroDivisionError: division by zero',
        'title': 'Division by Zero',
        'explanation': 'Your code is trying to divide a number by zero, which is not allowed in mathematics.',
        'solution': 'Check for places where you might be dividing by zero and add conditions to handle those cases.',
        'code_example': '''
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
''',
        'difficulty': 'beginner'
    },
    {
        'regex': r'RecursionError: maximum recursion depth exceeded',
        'title': 'Maximum Recursion Depth Exceeded',
        'explanation': 'Your code has a recursive function that\'s calling itself too many times, exceeding Python\'s limit for recursion depth. This often happens when a recursive function doesn\'t have a proper base case to stop the recursion.',
        'solution': 'Ensure your recursive function has a proper base case that will eventually be reached. Consider rewriting your algorithm to use iteration instead of recursion for very large inputs.',
        'code_example': '''
# Problematic recursive function (will cause RecursionError)
def factorial(n):
    return n * factorial(n-1)  # Missing base case!

# Corrected version with base case
def factorial(n):
    if n <= 1:  # Base case
        return 1
    return n * factorial(n-1)

# Alternative iterative approach
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
''',
        'difficulty': 'advanced'
    },
    {
        'regex': r'IndexError: list index out of range',
        'title': 'List Index Out of Range',
        'explanation': 'You\'re trying to access an element in a list using an index that is too large (or negative). Python lists are zero-indexed, so a list with n elements has indices from 0 to n-1.',
        'solution': 'Make sure your index is within the valid range for the list. Check the length of your list and ensure your index is less than that value.',
        'code_example': '''
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
'''
    },
    {
        'regex': r'KeyError: \'?([^\']+)\'?',
        'title': 'Dictionary Key "{{$1}}" Not Found',
        'explanation': 'You\'re trying to access a key "{{$1}}" that doesn\'t exist in your dictionary.',
        'solution': 'Check that the key exists before trying to access it. Use dictionary.get() method or the "in" operator to safely check for keys.',
        'code_example': '''
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
'''
    },
    {
        'regex': r'ModuleNotFoundError: No module named \'?([^\'\)]+)\'?',
        'title': 'Module "{{$1}}" Not Found',
        'explanation': 'Python cannot find the module "{{$1}}" that you\'re trying to import. Either the module isn\'t installed, or there\'s a typo in the module name.',
        'solution': 'Try installing the module using pip: "pip install {{$1}}". If that doesn\'t work, check for typos in the module name.',
        'code_example': '''
# In your terminal or command prompt:
# pip install {{$1}}

# Or if you're using Python 3:
# python -m pip install {{$1}}
'''
    },
    {
        'regex': r'ValueError: ([^\']+)',
        'title': 'Value Error: {{$1}}',
        'explanation': 'You\'re trying to perform an operation with a value that\'s not appropriate. The specific issue is: {{$1}}',
        'solution': 'Check the values you\'re using in the operation and make sure they\'re appropriate for what you\'re trying to do.',
        'code_example': '''
# Example (if converting a non-numeric string to int):
# Incorrect:
number = int("hello")  # Error: invalid literal for int()

# Correct (check before converting):
text = "hello"
if text.isdigit():
    number = int(text)
else:
    print("Cannot convert to number")
'''
    },
    {
        'regex': r'FileNotFoundError: \[Errno 2\] No such file or directory: \'?([^\']+)\'?',
        'title': 'File Not Found: {{$1}}',
        'explanation': 'Python cannot find the file "{{$1}}" that you\'re trying to access. Either the file doesn\'t exist, or the path is incorrect.',
        'solution': 'Check that the file exists at the specified path. Make sure you\'re using the correct path, which might be relative to the working directory.',
        'code_example': '''
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
'''
    },
    {
        'regex': r'ModuleNotFoundError: No module named \'([^\']+)\'',
        'title': 'Module Not Found: {{$1}}',
        'explanation': 'Python cannot find the module "{{$1}}" that your code is trying to import. This usually means the module is not installed or not in the Python path.',
        'solution': 'Install the missing module using pip: `pip install {{$1}}`. If it\'s a local module, make sure the file exists and is in a directory that Python can find (either in the current directory or in the PYTHONPATH).',
        'code_example': '''
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
'''
    },
    {
        'regex': r'ZeroDivisionError: division by zero',
        'title': 'Division by Zero',
        'explanation': 'Your code is attempting to divide a number by zero, which is mathematically undefined and raises a ZeroDivisionError in Python.',
        'solution': 'Add a condition to check if the divisor is zero before performing the division. You can use an if statement to provide an alternative result or raise a more specific error.',
        'code_example': '''
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
'''
    },
    {
        'regex': r'KeyError: \'([^\']+)\'',
        'title': 'Dictionary Key Not Found: {{$1}}',
        'explanation': 'Your code is trying to access a dictionary with the key "{{$1}}", but this key doesn\'t exist in the dictionary.',
        'solution': 'Check if the key exists before accessing it using the `in` operator, or use the `.get()` method which allows you to provide a default value if the key doesn\'t exist.',
        'code_example': '''
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
'''
    },
]

# JavaScript error patterns
JAVASCRIPT_PATTERNS = [
    {
        'regex': r'Uncaught ReferenceError: ([^ ]+) is not defined',
        'title': 'Variable "{{$1}}" Not Defined',
        'explanation': 'JavaScript cannot find a variable named "{{$1}}". This usually means you\'re trying to use a variable before creating it, or you might have a typo in the variable name.',
        'solution': 'Make sure you\'ve defined the variable "{{$1}}" before using it. Check for typos in variable names. Remember that variable names are case-sensitive in JavaScript.',
        'code_example': '''
// Incorrect:
console.log(myVariable);  // Error: myVariable is not defined

// Correct:
let myVariable = "Hello World";
console.log(myVariable);  // Now it works!
''',
        'difficulty': 'beginner'
    },
    {
        'regex': r'Uncaught TypeError: Cannot read properties? of (null|undefined) \(reading \'([^\']+)\'\)',
        'title': 'Cannot Read Property "{{$2}}" of {{$1}}',
        'explanation': 'Your code is trying to access a property "{{$2}}" on a {{$1}} value. This happens when you try to access properties on variables that are null or undefined.',
        'solution': 'Before accessing the property, check if the object exists. You can use optional chaining (?.) in modern JavaScript, the logical AND operator (&&), or a simple if statement.',
        'code_example': '''
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
''',
        'difficulty': 'beginner'
    },
    {
        'regex': r'Uncaught SyntaxError: Unexpected token \)',
        'title': 'Unexpected Closing Parenthesis',
        'explanation': 'JavaScript encountered a closing parenthesis ")" that doesn\'t match with an opening parenthesis. This is often caused by mismatched parentheses in your code.',
        'solution': 'Check your code for balanced parentheses, brackets, and braces. Make sure every opening parenthesis "(" has a matching closing parenthesis ")" in the correct order.',
        'code_example': '''
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
''',
        'difficulty': 'beginner'
    },
    {
        'regex': r'Uncaught RangeError: Maximum call stack size exceeded',
        'title': 'Maximum Call Stack Size Exceeded',
        'explanation': 'Your code has caused the JavaScript call stack to overflow, typically due to infinite recursion - a function that keeps calling itself without a proper base case to stop the recursion.',
        'solution': 'Ensure recursive functions have a proper termination condition. For deeply nested operations, consider rewriting using iteration or asynchronous methods.',
        'code_example': '''
// Problematic code - infinite recursion
function causeStackOverflow() {
  return causeStackOverflow();  // No base case!
}

// Correct recursive function with base case
function factorial(n) {
  if (n <= 1) {  // Base case
    return 1;
  }
  return n * factorial(n - 1);
}

// Alternative iterative approach
function factorialIterative(n) {
  let result = 1;
  for (let i = 1; i <= n; i++) {
    result *= i;
  }
  return result;
}
''',
        'difficulty': 'advanced'
    },
    {
        'regex': r'Uncaught TypeError: ([\w\.]+) is not a function',
        'title': '{{$1}} Is Not a Function',
        'explanation': 'Your code is trying to call {{$1}} as a function, but it\'s not a function. This often happens when a variable containing a different type (like string, number, or object) is accidentally used as a function.',
        'solution': 'Check the value of {{$1}} before trying to call it. Make sure it\'s actually a function. Verify correct spelling of function names and check if the containing object is correctly initialized.',
        'code_example': '''
// Problematic code
const data = { value: 42 };
data.getValue();  // TypeError: data.getValue is not a function

// Correct approaches:
// 1. Check if it's a function first
if (typeof data.getValue === 'function') {
  data.getValue();
} else {
  console.log("getValue is not available as a function");
}

// 2. Define the function if needed
const data = { 
  value: 42,
  getValue: function() {
    return this.value;
  }
};
data.getValue();  // Now it works
''',
        'difficulty': 'intermediate'
    },
    {
        'regex': r'Uncaught TypeError: ([^\']+) is (null|undefined)',
        'title': '{{$1}} is {{$2}}',
        'explanation': 'You\'re trying to use a variable "{{$1}}" that has the value {{$2}}. This means the variable doesn\'t have a usable value.',
        'solution': 'Make sure "{{$1}}" has a proper value before using it. Check where it\'s defined and ensure it\'s assigned a valid value.',
        'code_example': '''
// Incorrect:
let element = document.getElementById('non-existent-id');
element.innerHTML = 'Hello'; // Error: element is null

// Correct:
let element = document.getElementById('non-existent-id');
if (element) {
  element.innerHTML = 'Hello';
} else {
  console.log('Element not found');
}
'''
    },
    {
        'regex': r'TypeError: Cannot set propert(?:y|ies) \'([^\']+)\' of (null|undefined)',
        'title': 'Cannot Set Property "{{$1}}" of {{$2}}',
        'explanation': 'You\'re trying to set the property "{{$1}}" on a {{$2}} value. This happens when you try to modify properties on variables that don\'t have any value.',
        'solution': 'Make sure the object exists and is not {{$2}} before trying to set its properties. Check that the object has been properly initialized.',
        'code_example': '''
// Incorrect:
let user;
user.name = "John"; // Error: Cannot set property 'name' of undefined

// Correct:
let user = {}; // Initialize as an empty object first
user.name = "John"; // Now it works
'''
    },
    {
        'regex': r'Uncaught Error: Request failed with status code (\d+)',
        'title': 'API Request Failed with Status Code {{$1}}',
        'explanation': 'Your HTTP request failed with status code {{$1}}. This usually indicates a problem with the request or the server.',
        'solution': 'Check what status code {{$1}} means. Common codes: 404 (not found), 401 (unauthorized), 500 (server error). Ensure your API endpoint is correct and you have the necessary permissions.',
        'code_example': '''
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
'''
    },
    {
        'regex': r'Uncaught TypeError: ([^\']+) is not iterable',
        'title': '"{{$1}}" is Not Iterable',
        'explanation': 'You\'re trying to use "{{$1}}" in a loop or iteration context (like for...of), but it\'s not an iterable object. Only arrays, strings, and certain objects are iterable in JavaScript.',
        'solution': 'Make sure "{{$1}}" is an iterable type (like an array) before trying to iterate over it. You might need to check if it exists and is the right type first.',
        'code_example': '''
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
'''
    }
]

# HTML error patterns
HTML_PATTERNS = [
    {
        'regex': r'Unclosed tag \'([^\']+)\'',
        'title': 'Unclosed HTML Tag: <{{$1}}>',
        'explanation': 'You have an opening <{{$1}}> tag, but you\'re missing the closing </{{$1}}> tag. HTML tags must be properly closed.',
        'solution': 'Add the missing closing tag </{{$1}}> in the appropriate place. Make sure your tags are properly nested.',
        'code_example': '''
<!-- Incorrect -->
<div>
  <p>Some text
</div>

<!-- Correct -->
<div>
  <p>Some text</p>
</div>
'''
    },
    {
        'regex': r'Invalid character in markup: \'([^\']+)\'',
        'title': 'Invalid Character in HTML',
        'explanation': 'The character "{{$1}}" is not allowed in HTML where you\'ve placed it. This often happens with special characters like "&", "<", or ">".',
        'solution': 'Replace special characters with their HTML entities: "&" becomes "&amp;", "<" becomes "&lt;", ">" becomes "&gt;".',
        'code_example': '''
<!-- Incorrect -->
<p>This code: if (x < 10) will display an error</p>

<!-- Correct -->
<p>This code: if (x &lt; 10) will display correctly</p>
'''
    },
    {
        'regex': r'Error parsing HTML: Unexpected end tag \(([^\)]+)\)',
        'title': 'Unexpected End Tag: </{{$1}}>',
        'explanation': 'You have a closing </{{$1}}> tag that doesn\'t match any opening tag. Either you have an extra closing tag, or you\'re missing an opening tag.',
        'solution': 'Remove the extra closing tag, or add the matching opening tag. Make sure your tags are properly nested.',
        'code_example': '''
<!-- Incorrect -->
<div>
  <p>Some text</div>
</p>  <!-- Unexpected end tag </p> -->

<!-- Correct -->
<div>
  <p>Some text</p>
</div>
'''
    },
    {
        'regex': r'Error: Attribute "([^"]+)" not allowed on element "([^"]+)" at this point',
        'title': 'Invalid Attribute: {{$1}} on {{$2}}',
        'explanation': 'You\'re using the attribute "{{$1}}" on a <{{$2}}> element, but that attribute isn\'t valid for this element.',
        'solution': 'Remove the invalid attribute, or make sure you\'re using the correct element for what you\'re trying to do.',
        'code_example': '''
<!-- Incorrect -->
<div href="https://example.com">Click me</div>

<!-- Correct -->
<a href="https://example.com">Click me</a>
'''
    },
    {
        'regex': r'Error: End tag "([^"]+)" was not found',
        'title': 'Missing End Tag: </{{$1}}>',
        'explanation': 'You have an opening <{{$1}}> tag, but you never close it with </{{$1}}>. All HTML tags must be properly closed.',
        'solution': 'Add the missing </{{$1}}> closing tag in the appropriate place.',
        'code_example': '''
<!-- Incorrect -->
<div>
  <p>Some text

<!-- Correct -->
<div>
  <p>Some text</p>
</div>
'''
    },
    {
        'regex': r'Error: ID "([^"]+)" is already defined',
        'title': 'Duplicate HTML ID: {{$1}}',
        'explanation': 'You have multiple HTML elements with the same id "{{$1}}". HTML IDs must be unique within the entire document.',
        'solution': 'Use unique IDs for each element or consider using classes instead if you need to apply the same styling or behavior to multiple elements.',
        'code_example': '''
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
'''
    },
    {
        'regex': r'Error: Element "([^"]+)" is missing required attribute "([^"]+)"',
        'title': 'Missing Required Attribute: {{$2}} in {{$1}} Element',
        'explanation': 'The HTML element <{{$1}}> is missing a required attribute "{{$2}}". Some HTML elements have attributes that are necessary for them to function correctly.',
        'solution': 'Add the required "{{$2}}" attribute to your <{{$1}}> element.',
        'code_example': '''
<!-- Problematic HTML -->
<img src="">  <!-- Missing alt attribute -->
<input type="text">  <!-- Missing name attribute for form submission -->

<!-- Corrected HTML -->
<img src="image.jpg" alt="Description of the image">
<input type="text" name="username">

<!-- Common required attributes for elements -->
<a href="https://example.com">Link text</a>  <!-- href is required for links -->
<form action="/submit">...</form>  <!-- action is required for forms -->
'''
    },
    {
        'regex': r'Error: Unexpected token "<\/([^>]+)>" in <([^>]+)>',
        'title': 'Mismatched HTML Tags: </{{$1}}> in <{{$2}}>',
        'explanation': 'You have a closing tag </{{$1}}> that doesn\'t match the expected closing tag for <{{$2}}>. HTML tags must be properly nested and each opening tag must have a matching closing tag.',
        'solution': 'Fix the nesting of your HTML tags. Make sure that tags are closed in the reverse order they were opened.',
        'code_example': '''
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
'''
    },
]

# CSS error patterns
CSS_PATTERNS = [
    {
        'regex': r'Unknown property: \'([^\']+)\'',
        'title': 'Unknown CSS Property: "{{$1}}"',
        'explanation': 'The CSS property "{{$1}}" doesn\'t exist or isn\'t recognized. This might be a typo, or you might be using a newer property that\'s not supported in all browsers.',
        'solution': 'Check for typos in the property name. If you\'re using a newer property, consider adding appropriate vendor prefixes or a fallback.',
        'code_example': '''
/* Incorrect */
.element {
  colour: red;  /* Typo: "colour" instead of "color" */
}

/* Correct */
.element {
  color: red;
}
'''
    },
    {
        'regex': r'Invalid value for property \'([^\']+)\': \'([^\']+)\'',
        'title': 'Invalid Value for CSS Property',
        'explanation': 'The value "{{$2}}" is not valid for the CSS property "{{$1}}". Each CSS property only accepts specific types of values.',
        'solution': 'Check the documentation for the "{{$1}}" property to see what values it accepts. Fix the value accordingly.',
        'code_example': '''
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
'''
    },
    {
        'regex': r'Invalid property value: ([^:]+): ([^\n]+)',
        'title': 'Invalid CSS Value: {{$2}}',
        'explanation': 'The value "{{$2}}" is not valid for the CSS property "{{$1}}". Each CSS property expects values in a specific format.',
        'solution': 'Check the syntax for the "{{$1}}" property. Make sure you\'re using valid values and formats.',
        'code_example': '''
/* Incorrect */
.element {
  {{$1}}: {{$2}};
}

/* Example of correct syntax (adjust for your specific property) */
.element {
  color: #336699;  /* Use valid color format */
  width: 100px;    /* Include units for dimensions */
}
'''
    },
    {
        'regex': r'Error: unexpected token \'([^\']+)\'',
        'title': 'Unexpected Token in CSS: {{$1}}',
        'explanation': 'CSS encountered an unexpected character or symbol "{{$1}}" while parsing your styles. This usually indicates a syntax error.',
        'solution': 'Check your CSS syntax around where "{{$1}}" appears. Look for missing semicolons, brackets, or quotes.',
        'code_example': '''
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
'''
    },
    {
        'regex': r'Unexpected end of input',
        'title': 'Unexpected End of CSS',
        'explanation': 'Your CSS ended abruptly, likely due to an unclosed bracket, parenthesis, or quote.',
        'solution': 'Check your CSS for any unclosed structures. Make sure all opening braces { have matching closing braces }.',
        'code_example': '''
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
'''
    },
    {
        'regex': r'Property "([^"]+)" doesn\'t exist',
        'title': 'Unknown CSS Property: {{$1}}',
        'explanation': 'The CSS property "{{$1}}" doesn\'t exist in the CSS specification or it\'s misspelled.',
        'solution': 'Check for typos in the property name. Make sure you\'re using standard CSS properties or appropriate vendor prefixes for experimental properties.',
        'code_example': '''
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
'''
    },
    {
        'regex': r'Unterminated string constant',
        'title': 'Unterminated String in CSS',
        'explanation': 'You have a string in your CSS (such as in a url() or content property) that is missing its closing quote mark.',
        'solution': 'Add the missing closing quote (either single or double quote) to complete the string.',
        'code_example': '''
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
'''
    },
    {
        'regex': r'Unexpected @([^ ]+) rule',
        'title': 'Invalid or Misplaced CSS @{{$1}} Rule',
        'explanation': 'You\'re using an @{{$1}} rule that either doesn\'t exist or is placed in an invalid location in your CSS.',
        'solution': 'Check the syntax and placement of the @{{$1}} rule. Most at-rules need to be at the top level of your CSS, not nested inside selectors.',
        'code_example': '''
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
'''
    },
    {
        'regex': r'Expected ([^,]+), found \'([^\']+)\'',
        'title': 'CSS Syntax Error: Expected {{$1}}',
        'explanation': 'CSS expected {{$1}} at a certain point in your code, but found "{{$2}}" instead. This indicates a syntax error in your CSS.',
        'solution': 'Fix the syntax error by providing the expected {{$1}} where needed. Check for missing punctuation like semicolons, brackets, or colons.',
        'code_example': '''
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
'''
    },
]

# General error patterns (not specific to any language)
GENERAL_PATTERNS = [
    {
        'regex': r'(\d+) is not a valid port number',
        'title': 'Invalid Port Number: {{$1}}',
        'explanation': 'The port number {{$1}} is not valid. Port numbers must be between 0 and 65535.',
        'solution': 'Choose a port number between 0 and 65535. Common ports for development servers are 3000, 5000, or 8000. Make sure the port is not already in use by another application.',
        'code_example': '''
# Example for a Node.js server:
const express = require('express');
const app = express();
const PORT = 3000; // Use a valid port between 0-65535

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
'''
    },
    {
        'regex': r'Permission denied',
        'title': 'Permission Denied',
        'explanation': 'Your program doesn\'t have the necessary permissions to perform an operation, such as accessing a file, connecting to a port, or modifying system settings.',
        'solution': 'Check file or directory permissions. You might need to run your program with elevated privileges (as administrator/sudo), or modify the permissions of the resource you\'re trying to access.',
        'code_example': '''
# For file permission issues:
# Linux/macOS:
chmod 644 filename  # Read/write for owner, read for others
chmod 755 directory  # Executable bit needed for directories

# For running with elevated privileges (use with caution):
# Linux/macOS:
sudo python script.py

# Windows (run Command Prompt as Administrator):
python script.py
'''
    },
    {
        'regex': r'Address already in use',
        'title': 'Address Already in Use',
        'explanation': 'The network address (usually an IP address and port) that your program is trying to use is already being used by another program.',
        'solution': 'Choose a different port number, or stop the other program that\'s using the port. You can use task manager or process tools to find and stop the other program.',
        'code_example': '''
# Finding processes using a port:
# Linux/macOS:
lsof -i :3000  # Replace 3000 with your port number

# Windows:
netstat -ano | findstr :3000  # Replace 3000 with your port number

# In your code, try using a different port:
const PORT = 3001;  // Try a different port
'''
    },
    {
        'regex': r'Connection refused',
        'title': 'Connection Refused',
        'explanation': 'Your program tried to connect to a server or service, but the connection was actively refused. This usually means the server is not running, or it\'s running but not listening on the expected port.',
        'solution': 'Make sure the server or service you\'re trying to connect to is running. Check that you\'re using the correct host and port. If it\'s your own server, start it. If it\'s a remote service, check your internet connection.',
        'code_example': '''
# Check if you can connect to the service:
# Using curl:
curl http://localhost:3000

# If it's your own server, make sure it's running:
# Start a Node.js server:
node server.js

# Start a Python Flask server:
python app.py
'''
    },
    {
        'regex': r'Timeout exceeded',
        'title': 'Connection Timeout',
        'explanation': 'Your program tried to connect to a server or service, but the connection attempt took too long and timed out. This could mean the server is down, overloaded, or there\'s a network issue.',
        'solution': 'Check your internet connection. Make sure the server is up and running. Consider increasing the timeout value in your code if the server is known to be slow. If you\'re connecting to your own server, check server logs for performance issues.',
        'code_example': '''
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
'''
    },
    {
        'regex': r'Memory limit exceeded',
        'title': 'Memory Limit Exceeded',
        'explanation': 'Your program is trying to use more memory than is allowed or available. This can happen with large data structures, infinite loops that keep creating new objects, or memory leaks.',
        'solution': 'Optimize your code to use less memory. Avoid creating unnecessarily large arrays or objects. Make sure you don\'t have infinite loops. Consider processing data in smaller chunks instead of all at once.',
        'code_example': '''
# Instead of loading an entire file into memory:

# Bad approach (loads entire file):
with open("large_file.txt", "r") as file:
    content = file.read()  # Loads everything into memory
    # Process content...

# Better approach (process line by line):
with open("large_file.txt", "r") as file:
    for line in file:  # Reads one line at a time
        # Process line...
'''
    }
] 