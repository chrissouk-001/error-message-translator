# Error Message Translator

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A web application designed to help beginner developers understand cryptic error messages by translating them into plain, understandable language with practical solutions.

> **Research Notice**: This project is for research purposes to evaluate how Large Language Models (LLMs) perform on software development projects. Everyone is welcome to contribute to this repository as part of this research test.

![Error Message Translator Interface](screenshots/interface_screenshot.png)

The Error Message Translator provides a clean, intuitive interface for translating error messages into beginner-friendly explanations.

## Features

- Supports multiple programming languages:
  - Python
  - JavaScript
  - Java
  - Ruby
  - HTML
  - CSS
  - General error patterns
- Provides clear explanations of error messages
- Offers step-by-step solutions
- Includes code examples showing how to fix common errors
- Automatic language detection

## TODO

- [ ] Add support for more programming languages (C++, PHP, Swift)
- [ ] Implement error pattern suggestions based on user history
- [ ] Add a browser extension for quick error translation
- [ ] Create a mobile app version
- [ ] Add unit tests for new error patterns
- [ ] Implement error pattern validation
- [ ] Add support for custom error pattern submissions
- [ ] Create a community-driven error pattern database

## Project Structure

```
error-msg-translator/
├── app/                      # Main application package
│   ├── __init__.py           # Flask application initialization
│   ├── translator.py         # Core translation functionality
│   ├── data/                 # Error pattern data
│   │   ├── error_patterns.py # Aggregates all error patterns
│   │   ├── patterns/         # Organized error patterns by language
│   │   │   ├── python/       # Python error patterns
│   │   │   ├── javascript/   # JavaScript error patterns
│   │   │   ├── java/         # Java error patterns
│   │   │   ├── ruby/         # Ruby error patterns
│   │   │   ├── html/         # HTML error patterns
│   │   │   ├── css/          # CSS error patterns
│   │   │   └── general/      # General error patterns
│   ├── static/               # Static assets (CSS, JS, images)
│   └── templates/            # HTML templates
├── scripts/                  # Utility scripts
│   └── add_patterns.py       # Script to add new error patterns
└── requirements.txt          # Python dependencies
```

## Error Pattern Structure

Each error pattern follows this structure:

```python
{
    "regex": r"pattern_to_match_error",
    "title": "Error Title",
    "explanation": "Beginner-friendly explanation",
    "solution": "Steps to fix the error",
    "code_example": """
    # Example code showing the error
    # and how to fix it
    """,
    "related_errors": ["Similar error 1", "Similar error 2"],
    "difficulty": "beginner|intermediate|advanced"
}
```

Placeholders in the form `{{$N}}` can be used to reference captured groups from the regular expression.

## Adding New Error Patterns

To add new error patterns:

1. Identify the appropriate language module in `app/data/patterns/`
2. Add your pattern to the corresponding file
3. Follow the pattern structure shown above
4. Make sure your regex is accurate and captures relevant parts of the error
5. Provide a clear explanation and solution
6. Include a code example if possible

## Running the Application

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```
   flask run
   ```

3. Open your browser and navigate to `http://localhost:5000`

## API Usage

The application provides a simple API for error translation:

```
POST /api/translate
Content-Type: application/json

{
    "error_message": "Your error message here",
    "language": "auto"  // or specify: python, javascript, java, ruby, html, css, general
}
```

Response:

```json
{
    "title": "Error Title",
    "explanation": "Beginner-friendly explanation",
    "solution": "Steps to fix the error",
    "code_example": "Example code",
    "language": "detected_language",
    "difficulty": "beginner"
}
```

## License

MIT