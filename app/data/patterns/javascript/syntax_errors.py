"""
JavaScript SyntaxError Patterns

This module contains error patterns for JavaScript SyntaxError exceptions.
"""

from app.data.patterns.javascript import PATTERNS

# SyntaxError: missing ) after argument list
PATTERNS.append({
    "regex": r"SyntaxError: [Mm]issing [)]+ after argument list",
    "title": "Missing Closing Parenthesis",
    "explanation": "JavaScript found an opening parenthesis '(' but couldn't find the matching closing parenthesis ')'. This typically happens when you're calling a function and forget to close the parentheses.",
    "solution": "Check your function calls and make sure each opening parenthesis has a matching closing parenthesis. Pay special attention to nested function calls.",
    "code_example": """
// Incorrect:
console.log("Hello world"  // SyntaxError: missing ) after argument list

// Correct:
console.log("Hello world")  // Added the closing parenthesis
""",
    "related_errors": ["SyntaxError: missing ) after condition", "SyntaxError: unexpected token"],
    "difficulty": "beginner",
})

# SyntaxError: Unexpected token
PATTERNS.append({
    "regex": r"SyntaxError: [Uu]nexpected token ([^\s]+)",
    "title": "Unexpected Token '{{$1}}'",
    "explanation": "JavaScript encountered a character or token '{{$1}}' that it wasn't expecting at that position in the code. This often happens when you have mismatched brackets, extra commas, or other syntax errors.",
    "solution": "Look at the line where the error occurred and check for mismatched brackets or parentheses, extra or missing commas, and invalid syntax around the token '{{$1}}'.",
    "code_example": """
// Incorrect:
const user = {
    name: "John",
    age: 30,  // Extra comma
}  // SyntaxError: Unexpected token }

// Correct:
const user = {
    name: "John",
    age: 30  // Removed the extra comma
}
""",
    "related_errors": ["SyntaxError: unexpected end of input", "SyntaxError: invalid syntax"],
    "difficulty": "beginner",
})

# SyntaxError: Unexpected end of input
PATTERNS.append({
    "regex": r"SyntaxError: [Uu]nexpected end of input",
    "title": "Unexpected End of Code",
    "explanation": "JavaScript reached the end of your code but was still expecting more. This typically happens when you have unclosed brackets, parentheses, or string literals.",
    "solution": "Check your code for missing closing brackets, braces, or parentheses. Look for unclosed string literals or multi-line comments.",
    "code_example": """
// Incorrect:
function calculateTotal(items) {
    let total = 0;
    items.forEach(item => {
        total += item.price;
    // Missing closing bracket for the function!

// Correct:
function calculateTotal(items) {
    let total = 0;
    items.forEach(item => {
        total += item.price;
    });
}  // Added the missing brackets
""",
    "related_errors": ["SyntaxError: unexpected token", "SyntaxError: missing } after function body"],
    "difficulty": "beginner",
})

# SyntaxError: Invalid or unexpected token
PATTERNS.append({
    "regex": r"SyntaxError: [Ii]nvalid or unexpected token",
    "title": "Invalid Character in Code",
    "explanation": "JavaScript encountered a character that's not valid in this context. This often happens with string literals that use different quote types (like mixing ' and \") or when using special characters incorrectly.",
    "solution": "Check your string literals to ensure they start and end with the same type of quote (' or \"). Look for special characters that might need to be escaped with a backslash (\\).",
    "code_example": """
// Incorrect:
const message = 'It's a beautiful day';  // SyntaxError: Invalid or unexpected token

// Correct:
const message = "It's a beautiful day";  // Use double quotes around a string with a single quote
// Or
const message = 'It\\'s a beautiful day';  // Escape the single quote with a backslash
""",
    "related_errors": ["SyntaxError: unterminated string literal"],
    "difficulty": "beginner",
})

# SyntaxError: Missing semicolon
PATTERNS.append({
    "regex": r"SyntaxError: [Mm]issing semicolon",
    "title": "Missing Semicolon",
    "explanation": "JavaScript expects a semicolon at the end of a statement. While JavaScript often inserts semicolons automatically (ASI), there are cases where it's required or its absence causes unexpected behavior.",
    "solution": "Add a semicolon at the end of the statement. While modern JavaScript allows omitting semicolons in many cases, it's often safer to include them to avoid potential issues.",
    "code_example": """
// Incorrect:
let a = 5
let b = 10  // JavaScript might interpret this as "let a = 5(let b = 10)" in some cases

// Correct:
let a = 5;
let b = 10;  // Added semicolons for clarity and safety
""",
    "related_errors": ["SyntaxError: unexpected token"],
    "difficulty": "beginner",
}) 