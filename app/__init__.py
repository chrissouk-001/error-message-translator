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
    SECRET_KEY=os.environ.get("SECRET_KEY", os.urandom(24).hex()),
    DEBUG=os.environ.get("FLASK_DEBUG", "False").lower() == "true",
)

# Import after the app is created to avoid circular imports
from app.translator import translate_error, detect_language

# API route for translating error messages
@app.route("/api/translate", methods=["POST"])
def api_translate():
    """API endpoint to translate error messages."""
    # Validate content type
    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 415
        
    try:
        data = request.get_json()
        
        # Validate request data
        if not data or not isinstance(data, dict):
            return jsonify({"error": "Invalid JSON data"}), 400
            
        if "error_message" not in data:
            return jsonify({"error": "No error message provided"}), 400
        
        # Validate and sanitize inputs
        error_message = str(data.get("error_message", ""))[:5000]  # Limit length to prevent abuse
        
        # Validate language parameter
        language = data.get("language", "auto")
        valid_languages = ["auto", "python", "javascript", "java", "ruby", "html", "css", "general"]
        if language not in valid_languages:
            language = "auto"  # Default to auto if invalid
            
        output_language = data.get("output_language", None)
        
        # Call the translator function
        translation = translate_error(error_message, language, output_language)
        
        return jsonify(translation)
        
    except Exception as e:
        app.logger.error(f"Error processing translate request: {str(e)}")
        return jsonify({"error": "An error occurred processing your request"}), 500

# Add security headers to responses
@app.after_request
def add_security_headers(response):
    # Restrict CORS to specific origins in production, allow all in development
    if app.config['DEBUG']:
        response.headers.add("Access-Control-Allow-Origin", "*")
    else:
        # In production, restrict to your domain(s)
        allowed_origins = os.environ.get('ALLOWED_ORIGINS', 'http://localhost:5001')
        origin = request.headers.get('Origin')
        if origin and origin in allowed_origins.split(','):
            response.headers.add("Access-Control-Allow-Origin", origin)
    
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    
    # Add security headers
    response.headers.add("X-Content-Type-Options", "nosniff")
    response.headers.add("X-Frame-Options", "SAMEORIGIN")
    response.headers.add("X-XSS-Protection", "1; mode=block")
    response.headers.add("Referrer-Policy", "strict-origin-when-cross-origin")
    
    # Add basic Content Security Policy
    csp = "default-src 'self'; "
    csp += "script-src 'self' https://cdnjs.cloudflare.com 'unsafe-inline'; "
    csp += "style-src 'self' https://cdnjs.cloudflare.com https://fonts.googleapis.com 'unsafe-inline'; "
    csp += "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
    csp += "img-src 'self' data:; "
    csp += "connect-src 'self';"
    response.headers.add("Content-Security-Policy", csp)
    
    return response

# Make important objects available at package level
__all__ = ["app", "translate_error", "detect_language"]
