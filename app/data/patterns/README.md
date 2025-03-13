# Error Patterns

This directory contains error patterns for various programming languages. The patterns are organized by language and category.

## Directory Structure

```
patterns/
├── python/
│   ├── __init__.py
│   ├── name_errors.py
│   ├── type_errors.py
│   └── ...
├── javascript/
│   ├── __init__.py
│   ├── reference_errors.py
│   └── ...
├── java/
│   ├── __init__.py
│   └── ...
├── ruby/
│   ├── __init__.py
│   └── ...
├── html/
│   ├── __init__.py
│   └── ...
├── css/
│   ├── __init__.py
│   └── ...
└── general/
    ├── __init__.py
    └── ...
```

## Pattern Format

Each pattern is defined as a Python dictionary with the following keys:

- `regex`: Regular expression to match the error message
- `title`: A concise title summarizing the error
- `explanation`: Detailed explanation in beginner-friendly terms
- `solution`: Steps to resolve the issue
- `code_example`: (Optional) Example code showing the fix
- `related_errors`: (Optional) List of related errors
- `difficulty`: Level of difficulty (beginner, intermediate, advanced)

Example:

```python
PATTERNS.append({
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
})
```

## Adding New Patterns

You can add new patterns in several ways:

1. **Manually**: Create or edit a pattern file in the appropriate language directory.
2. **Using the script**: Run the `scripts/add_patterns.py` script to add patterns interactively or from a CSV/JSON file.

### Using the Script

```bash
# Interactive mode
python scripts/add_patterns.py --interactive

# From a CSV file
python scripts/add_patterns.py --csv path/to/patterns.csv

# From a JSON file
python scripts/add_patterns.py --json path/to/patterns.json
```

## CSV Format

When adding patterns from a CSV file, the file should have the following columns:

- `language`: The programming language (python, javascript, java, ruby, html, css, general)
- `category`: The category of the error (e.g., syntax_errors, type_errors)
- `regex`: Regular expression to match the error
- `title`: A concise title summarizing the error
- `explanation`: Detailed explanation in beginner-friendly terms
- `solution`: Steps to resolve the issue
- `code_example`: Example code showing the fix
- `related_errors`: Comma-separated list of related errors
- `difficulty`: Level of difficulty (beginner, intermediate, advanced)

## JSON Format

When adding patterns from a JSON file, the file can be in one of two formats:

1. A list of pattern objects, each with a `language` field:

```json
[
  {
    "language": "python",
    "category": "name_errors",
    "regex": "NameError: name \\'([^\\']+)\\' is not defined",
    "title": "Variable \"{{$1}}\" Not Defined",
    "explanation": "Python cannot find a variable named \"{{$1}}\"...",
    "solution": "Make sure you've defined the variable \"{{$1}}\" before using it...",
    "code_example": "# Incorrect:\nresult = {{$1}} + 10...",
    "related_errors": ["UnboundLocalError"],
    "difficulty": "beginner"
  },
  ...
]
```

2. A dictionary with language keys and lists of pattern objects:

```json
{
  "python": [
    {
      "category": "name_errors",
      "regex": "NameError: name \\'([^\\']+)\\' is not defined",
      "title": "Variable \"{{$1}}\" Not Defined",
      "explanation": "Python cannot find a variable named \"{{$1}}\"...",
      "solution": "Make sure you've defined the variable \"{{$1}}\" before using it...",
      "code_example": "# Incorrect:\nresult = {{$1}} + 10...",
      "related_errors": ["UnboundLocalError"],
      "difficulty": "beginner"
    },
    ...
  ],
  "javascript": [
    ...
  ],
  ...
}
``` 