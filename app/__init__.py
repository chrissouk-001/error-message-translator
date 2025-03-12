"""
Error Message Translator package.

This package provides functionality to translate error messages into beginner-friendly explanations.
"""
import os
from flask import Flask, request, jsonify

# Create Flask app instance
app = Flask(__name__, static_folder="static", template_folder="templates")

# Configure app from environment variables if available
app.config.from_mapping(
    SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
    DEBUG=os.environ.get("FLASK_DEBUG", "True").lower() == "true",
)

# Import after the app is created to avoid circular imports
from app.translator import translate_error, detect_language

# API route for translating error messages
@app.route("/api/translate", methods=["POST"])
def api_translate():
    """API endpoint to translate error messages."""
    data = request.get_json()
    
    if not data or "error_message" not in data:
        return jsonify({"error": "No error message provided"}), 400
    
    error_message = data.get("error_message", "")
    language = data.get("language", "auto")
    output_language = data.get("output_language", None)
    
    # Call the translator function
    translation = translate_error(error_message, language, output_language)
    
    return jsonify(translation)

# Add CORS headers to allow cross-origin requests
@app.after_request
def add_cors_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    return response

# Make important objects available at package level
__all__ = ["app", "translate_error", "detect_language"]
