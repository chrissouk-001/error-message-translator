"""
Error Message Translator

This module handles the translation of error messages from various programming
languages into simplified explanations for beginners.
"""
import re
import json
from pathlib import Path
from app.data.error_patterns import (
    PYTHON_PATTERNS,
    JAVASCRIPT_PATTERNS,
    HTML_PATTERNS,
    CSS_PATTERNS,
    JAVA_PATTERNS,
    RUBY_PATTERNS,
    GENERAL_PATTERNS,
)

# Dictionary mapping language codes to pattern dictionaries
ERROR_PATTERNS = {
    "python": PYTHON_PATTERNS,
    "javascript": JAVASCRIPT_PATTERNS,
    "html": HTML_PATTERNS,
    "css": CSS_PATTERNS,
    "java": JAVA_PATTERNS,
    "ruby": RUBY_PATTERNS,
    "general": GENERAL_PATTERNS,
}


def translate_text(text, output_language=None):
    """
    Since we're English-only now, this function simply returns the original text.

    Args:
        text (str): The text to translate
        output_language (str): Ignored, kept for compatibility

    Returns:
        str: The original text
    """
    return text


def detect_language(error_message):
    """
    Attempt to detect the programming language from the error message.

    Args:
        error_message (str): The error message to analyze

    Returns:
        str: The detected language ('python', 'javascript', 'html', 'css', 'java', 'ruby', or 'general')
    """
    # Initialize counters for each language
    language_scores = {
        "python": 0,
        "javascript": 0,
        "java": 0,
        "html": 0,
        "css": 0,
        "ruby": 0,
    }
    
    # Common language-specific keywords to boost detection confidence
    language_keywords = {
        "python": ["python", "pyfile", "pythonpath", "traceback", "def ", "class ", "import ", "syntaxerror", "indentationerror", "valueerror", "typeerror", "importerror", "attributeerror"],
        "javascript": ["javascript", "js", "node", "npm", "const ", "let ", "var ", "undefined", "referenceerror", "typeerror", "syntaxerror", "uncaught", "function", "=>", "promise", "async ", "await ", "document."],
        "java": ["java", "javac", "exception", "nullpointerexception", "classcastexception", "jvm", "runtime", "class ", "public ", "private ", "static ", "void ", "interface ", "abstract ", "extends ", "implements "],
        "html": ["html", "<html", "</html>", "<div", "</div>", "<body", "</body>", "<head", "</head>", "<!doctype", "markup", "tag", "element"],
        "css": ["css", "stylesheet", "css file", "selector", "@media", "@keyframes", "color:", "background:", "margin:", "padding:", "width:", "height:", "px;", "em;", "rem;", "%;" ],
        "ruby": ["ruby", "rb", "gem", "bundler", "nameerror", "nomethoderror", "argumenterror", "runtimeerror", "loaderror", "typeerror", "zerodivisionerror", "syntaxerror", "notenoughargumentserror", "module", "def ", "end", "nil"]
    }
    
    # Check for language-specific keywords in the error message
    error_lower = error_message.lower()
    for language, keywords in language_keywords.items():
        for keyword in keywords:
            if keyword in error_lower:
                language_scores[language] += 1
    
    # Pattern matching - check if any pattern from a language matches
    for language, patterns in ERROR_PATTERNS.items():
        if language == "general":
            continue  # Skip general patterns for now
            
        for pattern in patterns:
            if re.search(pattern["regex"], error_message, re.IGNORECASE):
                language_scores[language] += 2  # Pattern matches are stronger indicators
    
    # Check for file extensions in the error message
    file_extensions = {
        ".py": "python",
        ".js": "javascript",
        ".java": "java",
        ".html": "html",
        ".htm": "html",
        ".css": "css"
    }
    
    for ext, lang in file_extensions.items():
        if ext in error_message:
            language_scores[lang] += 3  # File extensions are very strong indicators
    
    # Determine the language with highest score
    max_score = 0
    detected_language = "general"
    
    for language, score in language_scores.items():
        if score > max_score:
            max_score = score
            detected_language = language
    
    # If no strong match is found, default to general
    if max_score <= 1:
        detected_language = "general"
        
    print(f"Language detection scores: {language_scores}, detected: {detected_language}")
    
    return detected_language


def translate_error(error_message, language="auto", output_language=None):
    """
    Translate an error message to a human-readable explanation (English only).

    Args:
        error_message (str): The error message to translate
        language (str): The programming language ('auto', 'python', 'javascript', etc.)
        output_language (str): Ignored, kept for compatibility

    Returns:
        dict: A dictionary containing the explanation
    """
    # Debug print statement
    print(f"Processing error: '{error_message[:50]}...' detected as {language}")

    if not error_message:
        return {
            "title": "No error message provided",
            "explanation": "Please provide an error message to translate.",
            "original_error": "",
            "solution": "Enter an error message in the input field above.",
            "difficulty": "beginner",  # Default difficulty for empty error
            "language": "unknown",  # Change to 'unknown' for empty messages
        }

    # Detect programming language if set to auto
    if language == "auto":
        language = detect_language(error_message)

    # Load error patterns for the detected language
    patterns = ERROR_PATTERNS.get(language, GENERAL_PATTERNS)

    # Try to match the error with known patterns
    for pattern in patterns:
        match = re.search(pattern["regex"], error_message, re.IGNORECASE)
        if match:
            # Replace placeholders in explanation with captured groups
            title = pattern["title"]
            explanation = pattern["explanation"]
            solution = pattern["solution"]
            code_example = pattern.get("code_example", "")
            difficulty = pattern.get(
                "difficulty", "intermediate"
            )  # Default to intermediate if not specified

            # Replace placeholders with captured groups
            for i, group in enumerate(match.groups(), 1):
                placeholder = "{{$" + str(i) + "}}"
                title = title.replace(placeholder, group)
                explanation = explanation.replace(placeholder, group)
                solution = solution.replace(placeholder, group)
                code_example = code_example.replace(placeholder, group)

            # Build result dictionary
            result = {
                "title": title,
                "explanation": explanation,
                "original_error": error_message,
                "solution": solution,
                "language": language,
                "difficulty": difficulty,
            }

            # Add code example if available
            if code_example:
                result["code_example"] = code_example

            # Add related errors if available
            if "related_errors" in pattern:
                result["related_errors"] = pattern["related_errors"]

            return result

    # If no pattern matches, return a general response
    return get_general_response(error_message, language)


def get_general_response(error_message, language, output_language=None):
    """
    Provide a general response when no specific pattern matches.

    Args:
        error_message (str): The error message
        language (str): The programming language
        output_language (str): Ignored, kept for compatibility

    Returns:
        dict: A dictionary with generic error information
    """
    # General responses for different languages
    generic_titles = {
        "python": "Python Error",
        "javascript": "JavaScript Error",
        "html": "HTML Error",
        "css": "CSS Error",
        "java": "Java Error",
        "ruby": "Ruby Error",
        "general": "Code Error",
    }

    # Get the title based on the language
    title = generic_titles.get(language, "Code Error")
    if language == "general":
        title = "Unknown Error"

    # Generic explanation and solution
    explanation = "This appears to be an error in your code that I don't specifically recognize."
    solution = "Check your syntax around the line mentioned in the error. Make sure all parentheses, brackets, and braces are properly closed. Look for typos or incorrect variable names."

    return {
        "title": title,
        "original_error": error_message,
        "language": language,
        "explanation": explanation,
        "solution": solution,
    }
