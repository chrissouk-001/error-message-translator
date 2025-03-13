"""
Error Patterns Module

This module imports and aggregates error patterns from all language-specific modules.
It provides the main interface for the application to access error patterns for all
supported programming languages.

Each pattern consists of:
- regex: Regular expression to match the error
- title: A concise title summarizing the error
- explanation: Detailed explanation in beginner-friendly terms
- solution: Steps to resolve the issue
- code_example: (Optional) Example code showing the fix
- related_errors: (Optional) List of related errors
- difficulty: Level of difficulty (beginner, intermediate, advanced)

Placeholders in the form {{$N}} can be used to reference captured groups
from the regular expression.
"""

# Import patterns from language-specific modules
try:
    from app.data.patterns.python import PATTERNS as PYTHON_PATTERNS
except ImportError:
    print("Warning: Could not import Python error patterns")
    PYTHON_PATTERNS = []

try:
    from app.data.patterns.javascript import PATTERNS as JAVASCRIPT_PATTERNS
except ImportError:
    print("Warning: Could not import JavaScript error patterns")
    JAVASCRIPT_PATTERNS = []

try:
    from app.data.patterns.java import PATTERNS as JAVA_PATTERNS
except ImportError:
    print("Warning: Could not import Java error patterns")
    JAVA_PATTERNS = []

try:
    from app.data.patterns.ruby import PATTERNS as RUBY_PATTERNS
except ImportError:
    print("Warning: Could not import Ruby error patterns")
    RUBY_PATTERNS = []

try:
    from app.data.patterns.html import PATTERNS as HTML_PATTERNS
except ImportError:
    print("Warning: Could not import HTML error patterns")
    HTML_PATTERNS = []

try:
    from app.data.patterns.css import PATTERNS as CSS_PATTERNS
except ImportError:
    print("Warning: Could not import CSS error patterns")
    CSS_PATTERNS = []

try:
    from app.data.patterns.general import PATTERNS as GENERAL_PATTERNS
except ImportError:
    print("Warning: Could not import general error patterns")
    GENERAL_PATTERNS = []

# Import the combined patterns if available
try:
    from app.data.patterns import ALL_PATTERNS
    print(f"Loaded {len(ALL_PATTERNS)} total patterns from app.data.patterns")
except ImportError:
    print("Warning: Could not import combined patterns from app.data.patterns")
    ALL_PATTERNS = []

# Print pattern counts for debugging
print(f"Python patterns: {len(PYTHON_PATTERNS)}")
print(f"JavaScript patterns: {len(JAVASCRIPT_PATTERNS)}")
print(f"Java patterns: {len(JAVA_PATTERNS)}")
print(f"Ruby patterns: {len(RUBY_PATTERNS)}")
print(f"HTML patterns: {len(HTML_PATTERNS)}")
print(f"CSS patterns: {len(CSS_PATTERNS)}")
print(f"General patterns: {len(GENERAL_PATTERNS)}")
print(f"Total patterns: {len(PYTHON_PATTERNS) + len(JAVASCRIPT_PATTERNS) + len(JAVA_PATTERNS) + len(RUBY_PATTERNS) + len(HTML_PATTERNS) + len(CSS_PATTERNS) + len(GENERAL_PATTERNS)}")

# Add new patterns or load from JSON/database here as needed
# This allows for easier management of a large number of patterns 