# Error Message Translator

A web application designed to help beginner developers understand cryptic error messages by translating them into plain, understandable language with practical solutions.

> **Research Notice**: This project is for research purposes to evaluate how Large Language Models (LLMs) perform on software development projects. Everyone is welcome to contribute to this repository as part of this research test.

![Error Message Translator Screenshot](screenshots/app_screenshot.png)

## Features

- **Error Message Translation**: Converts complex error messages into beginner-friendly explanations
- **Multi-language Support**: Works with Python, JavaScript, HTML, and CSS errors
- **Code Examples**: Provides practical code examples showing how to fix each error
- **Copy to Clipboard**: Easily copy code solutions
- **Recent Searches**: Keep track of your recently translated errors
- **Responsive Design**: Works well on desktop and mobile devices

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python with Flask
- **Storage**: Browser localStorage for recent searches
- **Testing**: pytest for unit and integration tests, Selenium for frontend tests

## Prerequisites

Before running this application, you need to have the following installed:

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/error-message-translator.git
   cd error-message-translator
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   # Install app dependencies only
   pip install -r requirements.txt
   
   # Or install both app and testing dependencies
   pip install -r requirements-test.txt
   ```

## Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5001
   ```

## Testing

The application includes comprehensive test coverage with pytest:

1. Make sure you have the testing dependencies installed:
   ```bash
   pip install -r requirements-test.txt
   ```

2. Run all tests:
   ```bash
   ./run_tests.sh
   ```

3. Run only unit tests:
   ```bash
   ./run_tests.sh --unit
   ```

4. Run only integration tests:
   ```bash
   ./run_tests.sh --integration
   ```

5. Run tests with coverage report:
   ```bash
   ./run_tests.sh --coverage
   ```

6. Run Selenium frontend tests:
   ```bash
   ./run_selenium_tests.sh
   ```
   
   Selenium test options:
   ```bash
   # Run with verbose output
   ./run_selenium_tests.sh --verbose
   
   # Run only theme toggle tests
   ./run_selenium_tests.sh --theme-only
   
   # Run only recent searches tests
   ./run_selenium_tests.sh --searches-only
   ```

## How It Works

1. The app analyzes error messages using regular expressions to identify patterns.
2. It matches these patterns against a database of known error templates.
3. When a match is found, it generates a beginner-friendly explanation and solution.
4. The matched components of the error are integrated into the explanation for context.

## Project Structure

```
error-message-translator/
├── app.py                  # Main Flask application
├── requirements.txt        # Application dependencies
├── requirements-test.txt   # Testing dependencies (includes app dependencies)
├── app/
│   ├── translator.py       # Core translation logic
│   ├── data/
│   │   └── error_patterns.py # Database of error patterns
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css  # Application styles
│   │   └── js/
│   │       └── main.js     # Frontend JavaScript
│   └── templates/
│       └── index.html      # Main HTML template
├── tests/
│   ├── conftest.py        # Test configuration and fixtures
│   ├── unit/              # Unit tests
│   │   ├── test_translator.py
│   │   ├── test_error_patterns.py
│   │   └── test_frontend.py
│   └── integration/       # Integration tests
│       ├── test_api.py
│       ├── test_recent_searches.py  # Selenium tests for recent searches
│       └── test_theme_toggle.py     # Selenium tests for theme toggle
└── screenshots/            # Project screenshots
```

## Extending the Error Database

To add new error patterns, edit the `app/data/error_patterns.py` file and add a new pattern following the existing structure:

```python
{
    'regex': r'YourRegexPattern',
    'title': 'Error Title',
    'explanation': 'Beginner-friendly explanation',
    'solution': 'How to fix the error',
    'code_example': '''
# Example code showing the fix
    ''',
    'related_errors': ['Related', 'Errors']
}
```

## Todo List

- [ ] Add syntax highlighting for code examples
- [ ] Implement more advanced language detection
- [ ] Add user feedback mechanism for translations
- [ ] Support more programming languages
- [ ] Add ability to share translations via URL
- [ ] Refactor frontend code for better structure.
- [ ] Add integration tests for new features.
- [ ] Create documentation for API usage.
- [ ] Setup CI/CD pipeline.
- [ ] Integrate caching layer for error translations
- [ ] Add unit tests for the translate_text function
- [ ] Optimize performance of regex matching
- [ ] Implement error message validation in JavaScript

## Contributing

Contributions are welcome! If you'd like to add more error patterns or improve the application:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to all the beginner developers whose struggles inspired this project
- All open-source libraries and tools used in this project