"""Error Patterns Module

This module imports and aggregates error patterns from all language-specific modules.
"""
import logging
from typing import List, Dict

# Configure logging
logger = logging.getLogger(__name__)

# Define supported languages
SUPPORTED_LANGUAGES = [
    "python",
    "javascript",
    "java",
    "ruby",
    "html",
    "css"
]

# Type definition for patterns
Pattern = Dict[str, str]
PatternList = List[Pattern]

# Initialize pattern collections
language_patterns: Dict[str, PatternList] = {lang: [] for lang in SUPPORTED_LANGUAGES}
ALL_PATTERNS: PatternList = []

def import_language_patterns(language: str) -> None:
    """Import patterns for a specific language."""
    try:
        module = __import__(f"app.data.patterns.{language}", fromlist=["PATTERNS"])
        language_patterns[language] = module.PATTERNS
        ALL_PATTERNS.extend(module.PATTERNS)
        logger.info(f"Loaded {len(module.PATTERNS)} patterns for {language}")
    except ImportError as e:
        logger.warning(f"Could not import {language} error patterns: {e}")

# Import patterns for all supported languages
for language in SUPPORTED_LANGUAGES:
    import_language_patterns(language)

# Print pattern counts for debugging
for lang in SUPPORTED_LANGUAGES:
    print(f"{lang.capitalize()} patterns: {len(language_patterns[lang])}")
print(f"Total patterns: {len(ALL_PATTERNS)}")

# Add new patterns or load from JSON/database here as needed
# This allows for easier management of a large number of patterns 
