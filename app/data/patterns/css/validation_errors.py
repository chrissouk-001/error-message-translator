"""
CSS Validation Error Patterns

This module contains error patterns for CSS validation errors.
"""

from app.data.patterns.css import PATTERNS

# Invalid Property
PATTERNS.append({
    "regex": r"Unknown property|whenInvalid property|Unrecognized property",
    "title": "Invalid CSS Property",
    "explanation": "The CSS property is not recognized. This could be because it's misspelled, not supported by the browser you're targeting, or it might be a vendor-specific property that needs a prefix.",
    "solution": "Check the spelling of the property, verify it's supported in your target browsers, or add the appropriate vendor prefix if needed. You can also use a CSS preprocessor or PostCSS to automatically add vendor prefixes.",
    "code_example": """
/* Incorrect - misspelled property */
.element {
    colour: red;  /* 'colour' is incorrect */
}

/* Correct */
.element {
    color: red;  /* 'color' is the correct spelling */
}

/* For experimental or browser-specific properties, use vendor prefixes */
.element {
    -webkit-user-select: none;  /* Chrome, Safari, newer versions of Opera */
    -moz-user-select: none;     /* Firefox */
    -ms-user-select: none;      /* Internet Explorer/Edge */
    user-select: none;          /* Standard syntax */
}
""",
    "related_errors": ["Unknown property", "Property doesn't exist"],
    "difficulty": "beginner"
})

# Invalid Value
PATTERNS.append({
    "regex": r"Invalid value|Unrecognized value|Bad value",
    "title": "Invalid CSS Value",
    "explanation": "The value is not valid for the CSS property it's being applied to. Each CSS property accepts specific types of values (like colors, lengths, or keywords).",
    "solution": "Check the documentation for the property to see what values it accepts. Make sure you're using the correct units for measurements, valid color formats, or appropriate keywords.",
    "code_example": """
/* Incorrect - invalid values */
.element {
    width: 100px%;  /* Can't mix units like px and % */
    color: dark-blue;  /* 'dark-blue' is not a valid color name */
    display: blocks;  /* 'blocks' is not a valid display value */
}

/* Correct */
.element {
    width: 100%;  /* Use either px or %, not both */
    color: darkblue;  /* Use a valid color name or hex/rgb value */
    display: block;  /* 'block' is a valid display value */
}
""",
    "related_errors": ["Unrecognized value", "Value not allowed"],
    "difficulty": "beginner"
})

# Missing Semicolon
PATTERNS.append({
    "regex": r"Missing semicolon|Expected semicolon|Unterminated rule|Unexpected token",
    "title": "Missing Semicolon in CSS",
    "explanation": "A semicolon is missing at the end of a CSS declaration. In CSS, each property-value pair should end with a semicolon, except for the last one in a rule (though including it is recommended for consistency).",
    "solution": "Add the missing semicolon at the end of the CSS declaration. It's good practice to always include semicolons, even for the last declaration in a rule, to avoid errors when adding more properties later.",
    "code_example": """
/* Incorrect - missing semicolons */
.element {
    color: red
    font-size: 16px
    margin: 10px
}

/* Correct */
.element {
    color: red;
    font-size: 16px;
    margin: 10px;  /* Including semicolon on last declaration is recommended */
}
""",
    "related_errors": ["Unterminated rule", "Unexpected token"],
    "difficulty": "beginner"
})

# Missing Closing Brace
PATTERNS.append({
    "regex": r"Missing closing brace|Expected closing brace|Unclosed block|Unterminated rule set",
    "title": "Missing Closing Brace in CSS",
    "explanation": "A CSS rule is missing its closing curly brace ('}'), which is used to mark the end of a declaration block. This can cause subsequent CSS to be interpreted incorrectly.",
    "solution": "Add the missing closing brace at the end of the CSS rule. Make sure each opening brace '{' has a corresponding closing brace '}'.",
    "code_example": """
/* Incorrect - missing closing brace */
.element {
    color: red;
    font-size: 16px;
    margin: 10px;
/* The closing brace is missing here */

.another-element {
    padding: 5px;  /* This will be interpreted as part of .element */
}

/* Correct */
.element {
    color: red;
    font-size: 16px;
    margin: 10px;
}  /* Closing brace added */

.another-element {
    padding: 5px;
}
""",
    "related_errors": ["Unclosed block", "Unterminated rule set"],
    "difficulty": "beginner"
})

# Invalid Selector
PATTERNS.append({
    "regex": r"Invalid selector|Unrecognized selector|Selector syntax error",
    "title": "Invalid CSS Selector",
    "explanation": "The CSS selector contains syntax errors or uses invalid characters. CSS selectors must follow specific syntax rules to correctly target HTML elements.",
    "solution": "Check your selector syntax. Make sure class selectors start with a dot (.), ID selectors start with a hash (#), and element selectors use valid HTML tag names. Also verify that you're using the correct combinators and pseudo-classes.",
    "code_example": """
/* Incorrect - invalid selectors */
.#element {  /* Can't combine . and # without an element name */
    color: red;
}

div:hover:wrong {  /* 'wrong' is not a valid pseudo-class */
    background-color: yellow;
}

/* Correct */
#element {  /* ID selector */
    color: red;
}

div.element {  /* Element with class */
    color: blue;
}

div:hover {  /* Element with valid pseudo-class */
    background-color: yellow;
}
""",
    "related_errors": ["Selector syntax error", "Unrecognized pseudo-class"],
    "difficulty": "intermediate"
})

# Add CSS Grid error pattern
PATTERNS.append({
    "regex": r"Invalid property value.+?grid-template-areas",
    "title": "Invalid Grid Template Areas",
    "explanation": "Your CSS grid-template-areas property has an invalid value. Grid areas must form a rectangle and each cell must be named or have a period (.) to indicate an empty cell.",
    "solution": "Make sure all rows in your grid-template-areas have the same number of cells and form a complete rectangle. Each named area must be rectangular.",
    "code_example": """
/* Incorrect - uneven rows */
.grid {
  grid-template-areas:
    "header header"
    "sidebar main main"; /* Error: uneven number of columns */
}

/* Incorrect - non-rectangular area */
.grid {
  grid-template-areas:
    "header header header"
    "sidebar main main"
    "sidebar footer footer"; /* Error: 'sidebar' is not rectangular */
}

/* Correct */
.grid {
  grid-template-areas:
    "header header header"
    "sidebar main main"
    "footer footer footer";
}
""",
    "related_errors": ["Property grid-template-columns doesn't exist"],
    "difficulty": "intermediate",
})

# Add CSS Media Query error
PATTERNS.append({
    "regex": r"Error in parsing value for 'media'.+?at line (\d+)",
    "title": "Invalid Media Query Syntax",
    "explanation": "There's a syntax error in your media query at line {{$1}}. Media queries have a specific syntax that must be followed.",
    "solution": "Check your media query syntax. Media features must be wrapped in parentheses, and logical operators (and/or) must be used correctly.",
    "code_example": """
/* Incorrect - missing parentheses */
@media screen and min-width: 768px {
  /* styles */
}

/* Incorrect - missing 'and' operator */
@media screen (min-width: 768px) {
  /* styles */
}

/* Correct */
@media screen and (min-width: 768px) {
  /* styles */
}

/* Correct with multiple conditions */
@media screen and (min-width: 768px) and (max-width: 1200px) {
  /* styles */
}
""",
    "related_errors": ["Expected media feature name but found"],
    "difficulty": "beginner",
})

# Add CSS Variable error
PATTERNS.append({
    "regex": r"Invalid variable reference.+?var\(([^)]+)\)",
    "title": "Invalid CSS Variable Reference",
    "explanation": "There's an issue with your CSS variable (custom property) reference: var({{$1}}). The variable might not be defined or the syntax is incorrect.",
    "solution": "Make sure the CSS variable is properly defined with -- prefix in a parent element or :root. Also check for typos in the variable name.",
    "code_example": """
/* Incorrect - using variable without defining it */
.element {
  color: var(--primary-color); /* Error if --primary-color is not defined */
}

/* Incorrect - wrong syntax */
:root {
  primary-color: blue; /* Missing -- prefix */
}

/* Correct */
:root {
  --primary-color: blue; /* Define with -- prefix */
}

.element {
  color: var(--primary-color); /* Now it works */
}

/* With fallback value */
.element {
  color: var(--primary-color, #333); /* Fallback to #333 if variable not defined */
}
""",
    "related_errors": ["Property doesn't exist"],
    "difficulty": "beginner",
})

# Add Flexbox error
PATTERNS.append({
    "regex": r"Property value .+? is invalid for .+?flex",
    "title": "Invalid Flexbox Property Value",
    "explanation": "You're using an invalid value for a flexbox property. Flexbox properties have specific accepted values.",
    "solution": "Check the documentation for the specific flexbox property you're using to see what values are valid.",
    "code_example": """
/* Incorrect - invalid value */
.container {
  display: flex;
  flex-direction: across; /* Error: 'across' is not a valid value */
}

/* Incorrect - using percentage for flex-basis in shorthand */
.item {
  flex: 1 1 50%; /* This actually works, but can cause confusion */
}

/* Correct flex-direction values */
.container {
  display: flex;
  flex-direction: row; /* or column, row-reverse, column-reverse */
}

/* Correct flex shorthand */
.item {
  flex: 1; /* flex-grow: 1, flex-shrink: 1, flex-basis: 0% */
}
""",
    "related_errors": ["Property doesn't exist"],
    "difficulty": "intermediate",
})

# Add CSS Animation error
PATTERNS.append({
    "regex": r"Error in parsing value for 'animation'.+?: .*?",
    "title": "Invalid CSS Animation Value",
    "explanation": "There's a syntax error in your CSS animation property. Animation properties require specific syntax for timing, easing, and keyframes.",
    "solution": "Check that your animation name matches a defined @keyframes rule and that you've specified the correct values for duration, timing function, delay, etc.",
    "code_example": """
/* Incorrect - animation name doesn't match keyframes or missing values */
.element {
  animation: slide 2s; /* Error if 'slide' keyframes not defined */
}

/* Incorrect - wrong order of values */
.element {
  animation: 2s infinite slide; /* Name should come first */
}

/* Correct with keyframes */
@keyframes slide {
  from { transform: translateX(0); }
  to { transform: translateX(100px); }
}

.element {
  animation: slide 2s ease infinite; /* name, duration, timing-function, iteration-count */
}

/* Multiple animations */
.element {
  animation: 
    slide 2s ease infinite,
    fade 1s ease-in;
}
""",
    "related_errors": ["Unknown property name"],
    "difficulty": "intermediate",
})

# Add Unknown Pseudo-class or Pseudo-element error
PATTERNS.append({
    "regex": r"Unknown pseudo-(class|element)|Unrecognized pseudo-(class|element)",
    "title": "Unknown Pseudo-class or Pseudo-element",
    "explanation": "The CSS uses a pseudo-class or pseudo-element that is not recognized. This could be due to a typo or using a feature not supported by the browser.",
    "solution": "Check the spelling of the pseudo-class or pseudo-element. Refer to the CSS specification or browser compatibility tables to ensure it's supported.",
    "code_example": """
/* Incorrect - typo in pseudo-class */
a:hovr {
    color: red;
}

/* Correct */
a:hover {
    color: red;
}

/* Incorrect - unsupported pseudo-element */
p::text {
    color: blue;
}

/* Correct */
p::first-line {
    color: blue;
}
""",
    "related_errors": ["Invalid selector", "Selector syntax error"],
    "difficulty": "intermediate",
})

# Add CSS Parse Error
PATTERNS.append({
    "regex": r"Parse Error|Lexical error|Syntax error at line",
    "title": "CSS Parse Error",
    "explanation": "The CSS parser encountered an unexpected character or syntax it couldn't understand. This is often caused by typos, unclosed comments, or misplaced symbols.",
    "solution": "Examine the line mentioned in the error message. Look for typos, missing or extra characters like braces {}, semicolons ;, colons :, or incorrect comment syntax (/* ... */).",
    "code_example": """
/* Incorrect - unclosed comment */
.element {
    color: red; /* This color is important
}

/* Incorrect - unexpected character */
.element {
    color: red;
    font-size: 16px&
}

/* Correct */
.element {
    color: red; /* This color is important */
    font-size: 16px;
}
""",
    "related_errors": ["Missing semicolon", "Missing closing brace", "Invalid property value"],
    "difficulty": "beginner",
})