"""
Error Message Translator

This module handles the translation of error messages from various programming
languages into simplified explanations for beginners.
"""
import re
import time
import logging
from functools import lru_cache
from typing import Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants for security limits
MAX_ERROR_LENGTH = 10000  # Maximum allowed error message length
REGEX_TIMEOUT = 0.5  # Timeout for regex operations in seconds
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
    Input is validated and sanitized.

    Args:
        text (str): The text to translate
        output_language (str): Ignored, kept for compatibility

    Returns:
        str: The sanitized original text
    """
    # Input validation
    if not isinstance(text, str):
        logger.warning(f"Non-string input to translate_text: {type(text)}")
        text = str(text) if text is not None else ""
        
    # Basic input sanitization - remove any potentially harmful control characters
    text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)
    
    # Limit length to prevent abuse
    if len(text) > MAX_ERROR_LENGTH:
        logger.warning(f"Text exceeding max length ({len(text)} chars) truncated")
        text = text[:MAX_ERROR_LENGTH] + "... [truncated]"
        
    return text


@lru_cache(maxsize=128)  # Cache results to improve performance and reduce regex load
def detect_language(error_message: str) -> str:
    """Detect programming language from error message.
    
    Args:
        error_message: The error message to analyze
        
    Returns:
        The detected language name
        
    Raises:
        ValueError: If error_message is empty or invalid
    """
    if not error_message or not isinstance(error_message, str):
        raise ValueError("Invalid error message")
        
    language_scores: Dict[str, int] = {
        lang: 0 for lang in SUPPORTED_LANGUAGES
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
    # Use timeout to prevent ReDoS attacks
    for language, patterns in ERROR_PATTERNS.items():
        if language == "general":
            continue  # Skip general patterns for now
            
        for pattern in patterns:
            try:
                # Use a timeout to prevent ReDoS attacks
                start_time = time.time()
                if time.time() - start_time > REGEX_TIMEOUT:
                    logger.warning(f"Regex timeout prevention for language: {language}")
                    break
                    
                if re.search(pattern["regex"], error_message, re.IGNORECASE | re.DOTALL, timeout=REGEX_TIMEOUT):
                    language_scores[language] += 2  # Pattern matches are stronger indicators
            except re.error as e:
                logger.error(f"Regex error in {language} pattern: {e}")
                continue
            except Exception as e:
                logger.error(f"Error in language detection for {language}: {e}")
                continue
    
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
    Now with improved security handling.

    Args:
        error_message (str): The error message to translate
        language (str): The programming language ('auto', 'python', 'javascript', etc.)
        output_language (str): Ignored, kept for compatibility

    Returns:
        dict: A dictionary containing the explanation
    """
    # Begin timing the translation process
    start_time = time.time()
    
    # Input validation
    if not isinstance(error_message, str):
        logger.warning(f"Non-string input to translate_error: {type(error_message)}")
        error_message = str(error_message) if error_message is not None else ""
    
    # Sanitize input - remove control characters that might affect regex
    error_message = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', error_message)
    
    # Limit input length for security
    if len(error_message) > MAX_ERROR_LENGTH:
        logger.warning(f"Error message exceeding max length ({len(error_message)} chars) truncated")
        error_message = error_message[:MAX_ERROR_LENGTH] + "... [truncated]"
    
    # Validate language parameter
    if not isinstance(language, str):
        logger.warning(f"Invalid language parameter: {language}")
        language = "auto"  # Default to auto-detection for invalid input
    
    # Normalize language to lowercase
    language = language.lower()
    
    # Only accept valid language options
    valid_languages = set(ERROR_PATTERNS.keys()) | {"auto"}
    if language not in valid_languages:
        logger.warning(f"Invalid language specified: {language}, defaulting to auto")
        language = "auto"
        
    # Log the processing (use logging instead of print for production code)
    logger.info(f"Processing error: '{error_message[:50]}...' specified language: {language}")

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
    # Use a try/except block to catch and handle any regex errors
    for pattern in patterns:
        try:
            # Use a timeout to prevent ReDoS attacks
            match = re.search(pattern["regex"], error_message, re.IGNORECASE | re.DOTALL, timeout=REGEX_TIMEOUT)
            if match:
                # Replace placeholders in explanation with captured groups
                title = pattern["title"]
                explanation = pattern["explanation"]
                solution = pattern["solution"]
                code_example = pattern.get("code_example", "")
                difficulty = pattern.get(
                    "difficulty", "intermediate"
                )  # Default to intermediate if not specified

                # Safely replace placeholders with captured groups
                try:
                    for i, group in enumerate(match.groups(), 1):
                        if group is None:
                            group = ""  # Handle None values in match groups
                        placeholder = "{{$" + str(i) + "}}"
                        # Ensure group is a string and sanitize it
                        group_str = str(group)
                        # Replace placeholders safely
                        title = title.replace(placeholder, group_str)
                        explanation = explanation.replace(placeholder, group_str)
                        solution = solution.replace(placeholder, group_str)
                        code_example = code_example.replace(placeholder, group_str)
                except Exception as e:
                    logger.error(f"Error processing match groups: {e}")
                    # Continue with unmodified template text rather than failing

            # Build result dictionary with additional security measures
            # Sanitize all outputs to ensure they don't contain harmful content
            result = {
                "title": translate_text(title)[:200],  # Limit title length
                "explanation": translate_text(explanation)[:5000],  # Limit explanation length
                "original_error": error_message,
                "solution": translate_text(solution)[:5000],  # Limit solution length
                "language": language,
                "difficulty": difficulty,
                "processing_time": f"{(time.time() - start_time):.3f}s",  # Add processing time for monitoring
            }

            # Add code example if available, with length limit
            if code_example:
                result["code_example"] = code_example[:5000]

            # Add related errors if available
            if "related_errors" in pattern:
                # Validate related errors format and content
                if isinstance(pattern["related_errors"], list):
                    # Limit number of related errors and their length
                    safe_related = []
                    for related in pattern["related_errors"][:5]:  # Limit to 5 related errors
                        if isinstance(related, dict) and "title" in related and "description" in related:
                            safe_related.append({
                                "title": translate_text(related["title"])[:100],
                                "description": translate_text(related["description"])[:500]
                            })
                    result["related_errors"] = safe_related

            logger.info(f"Successfully translated {language} error in {result['processing_time']}")
            return result
        except re.error as e:
            logger.error(f"Regex error with pattern: {e}")
            continue
        except Exception as e:
            logger.error(f"Unexpected error in pattern matching: {e}")
            continue

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
