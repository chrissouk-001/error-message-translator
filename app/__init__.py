"""
Error Message Translator package.

This package provides functionality to translate error messages into beginner-friendly explanations.
"""
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
import logging

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Error handlers
    @app.errorhandler(HTTPException)
    def handle_http_error(error):
        """Handle HTTP errors."""
        response = jsonify({
            "error": {
                "code": error.code,
                "name": error.name,
                "description": error.description
            }
        })
        response.status_code = error.code
        return response
    
    @app.errorhandler(Exception)
    def handle_generic_error(error):
        """Handle non-HTTP errors."""
        app.logger.error(f"Unhandled error: {str(error)}", exc_info=True)
        response = jsonify({
            "error": {
                "code": 500,
                "name": "Internal Server Error",
                "description": "An unexpected error occurred"
            }
        })
        response.status_code = 500
        return response
        
    return app

# Make important objects available at package level
__all__ = ["create_app", "translate_error", "detect_language"]
