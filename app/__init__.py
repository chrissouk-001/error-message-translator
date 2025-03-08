"""
Error Message Translator package.

This package provides functionality to translate error messages into beginner-friendly explanations.
"""
from flask import Flask

# Import after the app is created to avoid circular imports
from app.translator import translate_error, detect_language

# Create Flask app instance
app = Flask(__name__,
           static_folder='static',
           template_folder='templates')

# Make important objects available at package level
__all__ = ['app', 'translate_error', 'detect_language']
