"""
JavaScript TypeError Patterns

This module contains error patterns for JavaScript TypeError exceptions.
"""

from app.data.patterns.javascript import PATTERNS

# TypeError: X is not a function
PATTERNS.append({
    "regex": r"TypeError: ([^(]*) is not a function",
    "title": "Not a Function: {{$1}}",
    "explanation": "You're trying to call '{{$1}}' as a function, but it's not a function. This could be because the variable doesn't exist, it holds a different type of value, or there's a typo in the function name.",
    "solution": "Check if '{{$1}}' exists and is actually a function. Look for typos in function names and make sure you're not overwriting functions with other types of values.",
    "code_example": """
// Incorrect:
const data = { message: "Hello World" };
data.alert();  // TypeError: data.alert is not a function

// Correct:
const data = { message: "Hello World" };
console.log(data.message);  // Use a function that exists

// Or add the method to the object:
const data = {
    message: "Hello World",
    alert() {
        console.log(this.message);
    }
};
data.alert();  // Now it works!
""",
    "related_errors": ["ReferenceError: X is not defined"],
    "difficulty": "beginner",
})

# TypeError: Cannot read property 'X' of undefined
PATTERNS.append({
    "regex": r"TypeError: Cannot read (?:property|properties) '([^']*)' of (undefined|null)",
    "title": "Cannot Access '{{$1}}' on {{$2}}",
    "explanation": "You're trying to access a property '{{$1}}' on a value that is {{$2}}. This happens when you try to access a property of an object that doesn't exist or hasn't been initialized yet.",
    "solution": "Before accessing '{{$1}}', check if the object exists and is not {{$2}}. Use conditional checks, the optional chaining operator (?.), or provide default values with the nullish coalescing operator (??).",
    "code_example": """
// Incorrect:
const user = undefined;
console.log(user.name);  // TypeError: Cannot read property 'name' of undefined

// Correct:
// Option 1: Check if the object exists
const user = undefined;
if (user) {
    console.log(user.name);
} else {
    console.log("User not found");
}

// Option 2: Use optional chaining (ES2020+)
console.log(user?.name);  // Returns undefined instead of throwing an error

// Option 3: Provide a default value
const user = undefined;
const userData = user || { name: "Guest" };
console.log(userData.name);  // "Guest"
""",
    "related_errors": ["TypeError: X is undefined"],
    "difficulty": "beginner",
})

# TypeError: X is not iterable
PATTERNS.append({
    "regex": r"TypeError: ([^(]*) is not iterable",
    "title": "Cannot Iterate: {{$1}}",
    "explanation": "You're trying to use '{{$1}}' in a loop or spread operation, but it's not an iterable object (like an array, string, Map, Set, etc.).",
    "solution": "Make sure '{{$1}}' is an iterable object before using it in loops or with the spread operator. Convert non-iterable values to arrays or other iterable types as needed.",
    "code_example": """
// Incorrect:
const count = 42;
for (const digit of count) {  // TypeError: count is not iterable
    console.log(digit);
}

// Correct:
const count = 42;
const digits = String(count).split('');  // Convert to array of strings
for (const digit of digits) {
    console.log(digit);  // Works now!
}

// Or for a different example with an object:
const user = { name: "John", age: 30 };
for (const [key, value] of Object.entries(user)) {  // Make it iterable
    console.log(`${key}: ${value}`);
}
""",
    "related_errors": ["TypeError: X is not a function"],
    "difficulty": "intermediate",
})

# TypeError: invalid assignment to const
PATTERNS.append({
    "regex": r"TypeError: (?:[Ii]nvalid|[Aa]ttempt to) assign(?:ment)? to const",
    "title": "Cannot Reassign a Constant",
    "explanation": "You're trying to change the value of a variable that was declared with 'const'. Constants in JavaScript can't be reassigned after they're initialized.",
    "solution": "If you need to change the value, use 'let' instead of 'const' when declaring the variable. Only use 'const' for values that should never change.",
    "code_example": """
// Incorrect:
const PI = 3.14;
PI = 3.14159;  // TypeError: invalid assignment to const 'PI'

// Correct:
// Option 1: Use 'let' if the value needs to change
let pi = 3.14;
pi = 3.14159;  // Works!

// Option 2: Keep 'const' but don't try to reassign it
const PI = 3.14159;  // Set the correct value initially
console.log(PI);  // Use the constant without changing it

// Note: Objects and arrays declared with 'const' can still have their properties/elements modified:
const user = { name: "John" };
user.name = "Jane";  // This works - we're not reassigning 'user', just modifying a property
""",
    "related_errors": ["SyntaxError: identifier has already been declared"],
    "difficulty": "beginner",
})

# TypeError: X is undefined, cannot access Y property
PATTERNS.append({
    "regex": r"TypeError: (?:cannot read|cannot access) ([^(]*) (?:of|on) undefined",
    "title": "Object is Undefined",
    "explanation": "You're trying to access a property of an object that is undefined. This often happens when you try to use a variable before it's defined or when a function doesn't return the expected object.",
    "solution": "Check if the object exists before trying to access its properties. Use conditional checks, try/catch blocks, or the optional chaining operator (?.) to safely access nested properties.",
    "code_example": """
// Incorrect:
function getUser() {
    // Function doesn't return anything
}
const user = getUser();
console.log(user.name);  // TypeError: Cannot read property 'name' of undefined

// Correct:
// Option 1: Check if the object exists
function getUser() {
    // Function doesn't return anything
}
const user = getUser();
if (user) {
    console.log(user.name);
} else {
    console.log("User not available");
}

// Option 2: Make sure the function returns an object
function getUser() {
    return { name: "John" };  // Return a default object if no user is found
}
const user = getUser();
console.log(user.name);  // "John"

// Option 3: Use optional chaining (ES2020+)
const user = getUser();
console.log(user?.name);  // undefined (instead of throwing an error)
""",
    "related_errors": ["ReferenceError: X is not defined", "TypeError: Cannot read property of null"],
    "difficulty": "beginner",
})

# Add Promise-related TypeError
PATTERNS.append({
    "regex": r"TypeError: Promise resolver ([^(]+) is not a function",
    "title": "Invalid Promise Constructor Parameter",
    "explanation": "When creating a new Promise, you need to provide a function as the resolver parameter, but you provided a {{$1}} instead.",
    "solution": "Make sure to pass a function to the Promise constructor that takes 'resolve' and 'reject' parameters.",
    "code_example": """
// Incorrect:
const myPromise = new Promise(123);  // TypeError: Promise resolver 123 is not a function

// Correct:
const myPromise = new Promise((resolve, reject) => {
  // Do something asynchronous, then:
  resolve('Success!');  // or reject('Error!') if there's an error
});
""",
    "related_errors": ["SyntaxError: missing ) after argument list"],
    "difficulty": "intermediate",
})

# Add async/await TypeError
PATTERNS.append({
    "regex": r"TypeError: ([^(]+) is not a function or its return value is not iterable",
    "title": "Invalid Await Target",
    "explanation": "You're trying to use 'await' with {{$1}}, which is not a function that returns a Promise or an iterable object for use with for-await-of.",
    "solution": "Make sure you're awaiting a function that returns a Promise or using for-await-of with an async iterable.",
    "code_example": """
// Incorrect:
async function fetchData() {
  const data = await 123;  // TypeError: 123 is not a function or its return value is not iterable
  return data;
}

// Correct:
async function fetchData() {
  const response = await fetch('https://api.example.com/data');
  const data = await response.json();
  return data;
}
""",
    "related_errors": ["SyntaxError: await is only valid in async functions"],
    "difficulty": "intermediate",
})

# Add JSON parsing TypeError
PATTERNS.append({
    "regex": r"TypeError: JSON\.parse: unexpected (character|non-whitespace character) at line (\d+) column (\d+) of the JSON data",
    "title": "Invalid JSON Format",
    "explanation": "JSON.parse encountered an unexpected {{$1}} at line {{$2}}, column {{$3}} while trying to parse a string as JSON.",
    "solution": "Check your JSON string for syntax errors like missing quotes, commas, or brackets. Use a JSON validator to find and fix formatting issues.",
    "code_example": """
// Incorrect:
const jsonStr = '{"name": "John", "age": 30,}';  // Extra comma
const obj = JSON.parse(jsonStr);  // TypeError: JSON.parse: unexpected character

// Correct:
const jsonStr = '{"name": "John", "age": 30}';  // Valid JSON
const obj = JSON.parse(jsonStr);  // Works!
""",
    "related_errors": ["SyntaxError: JSON.parse: unexpected character"],
    "difficulty": "beginner",
})

# Add null or undefined property access TypeError
PATTERNS.append({
    "regex": r"TypeError: Cannot read (?:property|properties) '([^']+)' of (null|undefined)",
    "title": "Accessing Property of {{$2}}",
    "explanation": "You're trying to access the '{{$1}}' property of a {{$2}} value. This happens when a variable hasn't been initialized or doesn't exist.",
    "solution": "Add a check to make sure the object exists before accessing its properties. Use optional chaining (?.) or the nullish coalescing operator (??) in modern JavaScript.",
    "code_example": """
// Incorrect:
const user = null;
console.log(user.name);  // TypeError: Cannot read property 'name' of null

// Correct with if check:
if (user) {
  console.log(user.name);
}

// Correct with optional chaining (modern JS):
console.log(user?.name);  // Returns undefined instead of throwing error

// Correct with default value:
console.log((user || {}).name);  // Returns undefined
""",
    "related_errors": ["ReferenceError: variable is not defined"],
    "difficulty": "beginner",
})

# Add template literal TypeError
PATTERNS.append({
    "regex": r"TypeError: ([^(]+) is not a function$",
    "title": "Invalid Function Call",
    "explanation": "You're trying to call {{$1}} as if it were a function, but it's not a function.",
    "solution": "Check if you're using template literals (backticks) without a tag function, or if you've accidentally used parentheses after a non-function value.",
    "code_example": """
// Incorrect:
const name = "John";
const greeting = name`Hello`;  // TypeError: name is not a function

// Correct:
const name = "John";
const greeting = `Hello ${name}`;  // Works!

// Another common error:
const obj = { name: "John" };
const result = obj();  // TypeError: obj is not a function

// Correct:
const obj = { name: "John" };
const name = obj.name;  // Works!
""",
    "related_errors": ["SyntaxError: unexpected token"],
    "difficulty": "beginner",
}) 