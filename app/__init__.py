"""
Error Message Translator package.

This package provides functionality to translate error messages into beginner-friendly explanations.
"""
import os
import secrets
import time
from functools import wraps
from flask import Flask, request, jsonify

# Create Flask app instance
app = Flask(__name__, static_folder="static", template_folder="templates")

# Configure app from environment variables if available
# Use a more secure method for SECRET_KEY generation with secrets module
secret_key = os.environ.get("SECRET_KEY")
if not secret_key:
    # Generate a more secure random key with secrets module if not provided
    secret_key = secrets.token_hex(32)  # 64 character hex string (256 bits)
    
# Configure app with improved security settings
app.config.from_mapping(
    SECRET_KEY=secret_key,
    DEBUG=os.environ.get("FLASK_DEBUG", "False").lower() == "true",
    # Add session cookie security
    SESSION_COOKIE_SECURE=not app.config.get("DEBUG", False),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    PERMANENT_SESSION_LIFETIME=1800,  # 30 minutes
)

# Import after the app is created to avoid circular imports
from app.translator import translate_error, detect_language

# Simple rate limiting implementation
request_history = {}
RATE_LIMIT = 30  # requests per minute
RATE_WINDOW = 60  # seconds

def rate_limit(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get client identifier - prefer X-Forwarded-For if behind proxy
        client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        if client_ip not in request_history:
            request_history[client_ip] = []
        
        # Clean old requests outside the time window
        current_time = time.time()
        request_history[client_ip] = [t for t in request_history[client_ip] 
                                      if current_time - t < RATE_WINDOW]
        
        # Check if rate limit exceeded
        if len(request_history[client_ip]) >= RATE_LIMIT:
            app.logger.warning(f"Rate limit exceeded for {client_ip}")
            return jsonify({"error": "Rate limit exceeded. Please try again later."}), 429
        
        # Add current request timestamp
        request_history[client_ip].append(current_time)
        
        return f(*args, **kwargs)
    return decorated_function

# API route for translating error messages
@app.route("/api/translate", methods=["POST"])
@rate_limit
def api_translate():
    """API endpoint to translate error messages."""
    # Validate content type
    if not request.content_type or 'application/json' not in request.content_type:
        return jsonify({"error": "Content-Type must be application/json"}), 415
        
    try:
        data = request.get_json(silent=True)
        
        # Validate request data
        if not data or not isinstance(data, dict):
            return jsonify({"error": "Invalid JSON data"}), 400
            
        if "error_message" not in data:
            return jsonify({"error": "No error message provided"}), 400
        
        # Validate and sanitize inputs
        error_message = str(data.get("error_message", ""))[:5000]  # Limit length to prevent abuse
        if not error_message.strip():
            return jsonify({"error": "Empty error message provided"}), 400
        
        # Validate language parameter
        language = data.get("language", "auto")
        valid_languages = ["auto", "python", "javascript", "java", "ruby", "html", "css", "general"]
        if language not in valid_languages:
            language = "auto"  # Default to auto if invalid
            
        output_language = data.get("output_language")
        if output_language and not isinstance(output_language, str):
            output_language = None
            
        # Call the translator function
        translation = translate_error(error_message, language, output_language)
        
        return jsonify(translation)
        
    except Exception as e:
        app.logger.error(f"Error processing translate request: {str(e)}")
        # Don't expose detailed error information
        return jsonify({"error": "An error occurred processing your request"}), 500

# Add CORS handling
@app.route('/api/translate', methods=['OPTIONS'])
def handle_options():
    """Handle preflight OPTIONS requests for CORS"""
    response = app.make_default_options_response()
    add_security_headers(response)
    return response

# Add security headers to responses
@app.after_request
def add_security_headers(response):
    # Restrict CORS to specific origins - always use a whitelist approach
    allowed_origins = os.environ.get('ALLOWED_ORIGINS', 'http://localhost:5001')
    origin = request.headers.get('Origin')
    
    # Only set CORS headers when origin matches allowed list - even in debug mode
    if origin and (origin in allowed_origins.split(',') or app.config['DEBUG']):
        response.headers.add("Access-Control-Allow-Origin", origin)
        response.headers.add("Access-Control-Allow-Headers", "Content-Type, X-Requested-With")
        response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        response.headers.add("Access-Control-Max-Age", "3600")  # Cache preflight for 1 hour
    
    # Add standard security headers
    response.headers.update({
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",  # Stricter than SAMEORIGIN
        "X-XSS-Protection": "1; mode=block",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Permissions-Policy": "accelerometer=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=()",
        "Cache-Control": "no-store, max-age=0" if not app.config['DEBUG'] else ""
    })
    
    # Improve Content Security Policy - reduce unsafe-inline usage where possible
    # Ideally you would use nonces or hashes for inline scripts, but for now we'll tighten other aspects
    csp = []
    csp.append("default-src 'self'")
    csp.append("script-src 'self' https://cdnjs.cloudflare.com 'unsafe-inline'")  # Future improvement: use nonces
    csp.append("style-src 'self' https://cdnjs.cloudflare.com https://fonts.googleapis.com 'unsafe-inline'")
    csp.append("font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com")
    csp.append("img-src 'self' data:")
    csp.append("connect-src 'self'")
    csp.append("frame-ancestors 'none'")  # Prevents embedding in iframes (similar to X-Frame-Options: DENY)
    csp.append("form-action 'self'")  # Restricts where forms can be submitted
    csp.append("base-uri 'self'")  # Restricts use of <base> tag
    
    response.headers["Content-Security-Policy"] = "; ".join(csp)
    
    return response

# Make important objects available at package level
__all__ = ["app", "translate_error", "detect_language"]
