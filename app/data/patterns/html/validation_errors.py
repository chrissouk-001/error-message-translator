"""
HTML Validation Error Patterns

This module contains error patterns for HTML validation errors.
"""

from app.data.patterns.html import PATTERNS

# Unclosed tag
PATTERNS.append({
    "regex": r"(?:Error:|Unclosed tag)(?:.*?)([a-zA-Z0-9]+)(?:\s+tag)?",
    "title": "Unclosed HTML Tag: {{$1}}",
    "explanation": "Your HTML has an opening <{{$1}}> tag without a matching closing </{{$1}}> tag. Most HTML tags must be properly closed to form valid HTML.",
    "solution": "Add the missing closing tag </{{$1}}> at the appropriate position. Make sure each opening tag has a corresponding closing tag in the correct order.",
    "code_example": """
<!-- Incorrect -->
<div>
  <h1>My Title
  <p>My paragraph</p>
</div>

<!-- Correct -->
<div>
  <h1>My Title</h1>
  <p>My paragraph</p>
</div>
""",
    "related_errors": ["Stray end tag", "Missing end tag"],
    "difficulty": "beginner",
})

# Stray end tag
PATTERNS.append({
    "regex": r"(?:Error:|Stray end tag)(?:.*?)([a-zA-Z0-9]+)",
    "title": "Stray End Tag: {{$1}}",
    "explanation": "Your HTML has a closing </{{$1}}> tag without a matching opening <{{$1}}> tag. Each closing tag must have a corresponding opening tag.",
    "solution": "Either add a matching opening <{{$1}}> tag or remove the stray closing tag. Check your nesting order - tags must be closed in the reverse order they were opened.",
    "code_example": """
<!-- Incorrect -->
<div>
  <p>My paragraph</p>
  </h2>  <!-- Stray end tag - there's no opening h2 tag -->
</div>

<!-- Correct -->
<div>
  <p>My paragraph</p>
</div>
""",
    "related_errors": ["Unclosed tag", "Missing start tag"],
    "difficulty": "beginner",
})

# Invalid attribute
PATTERNS.append({
    "regex": r"(?:Error:|Invalid attribute)(?:.*?)([a-zA-Z0-9-]+)(?:.*?)for(?:.*?)([a-zA-Z0-9]+)",
    "title": "Invalid Attribute: {{$1}} for {{$2}}",
    "explanation": "The attribute '{{$1}}' is not valid for the <{{$2}}> tag. Each HTML element has a specific set of allowed attributes.",
    "solution": "Remove the invalid attribute or check if you're using the correct element for your purpose. Also check for typos in attribute names.",
    "code_example": """
<!-- Incorrect -->
<img loop="true" src="image.jpg">  <!-- 'loop' is not a valid attribute for img -->

<!-- Correct -->
<img src="image.jpg">  <!-- Removed the invalid attribute -->

<!-- Or maybe you wanted a different element? -->
<video loop autoplay>
  <source src="video.mp4" type="video/mp4">
</video>
""",
    "related_errors": ["Unknown attribute", "Attribute not allowed"],
    "difficulty": "intermediate",
})

# Element missing required attribute
PATTERNS.append({
    "regex": r"(?:Error:|Element)(?:.*?)([a-zA-Z0-9]+)(?:.*?)missing required attribute(?:.*?)([a-zA-Z0-9-]+)",
    "title": "Missing Required Attribute: {{$2}} in {{$1}}",
    "explanation": "The <{{$1}}> element is missing a required attribute '{{$2}}'. Some HTML elements have mandatory attributes that must be included.",
    "solution": "Add the required '{{$2}}' attribute to the <{{$1}}> tag. This is necessary for the element to function properly and for valid HTML.",
    "code_example": """
<!-- Incorrect -->
<img>  <!-- Missing required 'src' attribute -->

<!-- Correct -->
<img src="image.jpg">  <!-- Added the required 'src' attribute -->

<!-- Another example -->
<!-- Incorrect -->
<input type="radio" name="options">  <!-- 'value' attribute is required for radio buttons -->

<!-- Correct -->
<input type="radio" name="options" value="option1">  <!-- Added the required 'value' attribute -->
""",
    "related_errors": ["Invalid attribute", "Missing attribute"],
    "difficulty": "beginner",
})

# Duplicate ID
PATTERNS.append({
    "regex": r"(?:Error:|Duplicate ID)(?:.*?)([a-zA-Z0-9_-]+)",
    "title": "Duplicate ID: {{$1}}",
    "explanation": "The ID '{{$1}}' is used more than once in your HTML document. IDs must be unique within a single HTML document.",
    "solution": "Give each element a unique ID. If multiple elements need the same styling or behavior, use classes instead of IDs.",
    "code_example": """
<!-- Incorrect -->
<div id="container">First container</div>
<div id="container">Second container</div>  <!-- Duplicate ID 'container' -->

<!-- Correct -->
<div id="container1">First container</div>
<div id="container2">Second container</div>

<!-- Or use classes for shared styling -->
<div class="container">First container</div>
<div class="container">Second container</div>
""",
    "related_errors": ["Invalid ID", "Duplicate attribute"],
    "difficulty": "beginner",
}) 