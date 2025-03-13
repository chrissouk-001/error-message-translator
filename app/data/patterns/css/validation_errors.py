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