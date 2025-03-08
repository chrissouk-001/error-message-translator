"""
Error Message Translator package.

This package provides functionality to translate error messages into beginner-friendly explanations.
"""
import os
from flask import Flask

# Create Flask app instance
app = Flask(__name__,
           static_folder='static',
           template_folder='templates')

# Configure app from environment variables if available
app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
    DEBUG=os.environ.get('FLASK_DEBUG', 'True').lower() == 'true',
)

# Import after the app is created to avoid circular imports
from app.translator import translate_error, detect_language

# Make important objects available at package level
__all__ = ['app', 'translate_error', 'detect_language']
