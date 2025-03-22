"""
Entry point for the Flask application.

This file serves as the entry point for running the Error Message Translator application.
"""
import os
import argparse
from app import app


# Define the main route for the application
@app.route("/")
def index():
    """Render the main page of the application."""
    from flask import render_template

    # Render and return the main HTML template
    return render_template("index.html")


# Main function to run the Flask application
def main():
    """Run the Flask application."""
    # Set up argument parser for command-line options
    parser = argparse.ArgumentParser(description="Run the Error Message Translator app")
    parser.add_argument("--port", type=int, default=5001, help="Port to run the app on")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host to bind to (use 0.0.0.0 for all interfaces)")
    parser.add_argument("--prod", action="store_true", help="Run in production mode with secure settings")
    args = parser.parse_args()
    
    # Determine if we're running in debug mode
    # In production mode, override any debug flags for security
    debug_mode = False if args.prod else (args.debug or os.environ.get('FLASK_DEBUG', 'False').lower() == 'true')
    
    # In production, only bind to loopback unless explicitly specified
    host = args.host
    
    # Configure production settings
    if args.prod:
        # Default to loopback in production for security
        host = os.environ.get('HOST', '127.0.0.1')
        
        # Ensure we're not exposing debug features
        os.environ['FLASK_DEBUG'] = 'False'
        app.config['DEBUG'] = False
        
        # Ensure secure cookie settings
        app.config['SESSION_COOKIE_SECURE'] = True
        app.config['SESSION_COOKIE_HTTPONLY'] = True
        app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
        
        # Disable JSON key sorting to prevent potential information leakage
        app.config['JSON_SORT_KEYS'] = False
        
        # Add additional security headers in production
        os.environ['ENABLE_STRICT_TRANSPORT_SECURITY'] = 'True'
        
        print("Running in production mode with secure settings")
    elif debug_mode:
        print("WARNING: Running in debug mode. Not recommended for production!")
        if host == '0.0.0.0':
            print("SECURITY WARNING: Debug mode is enabled and the server is accessible from all interfaces")
            print("Consider using 127.0.0.1 instead for local development")
    
    # Apply maximum request size limits to prevent DOS attacks
    app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1 MB limit
    
    # Start the Flask application with appropriate settings
    # In production mode, use a production-ready WSGI server instead of Flask's built-in server
    if args.prod:
        print("NOTE: For actual production deployment, use a production WSGI server like Gunicorn or uWSGI")
    
    app.run(debug=debug_mode, host=host, port=args.port, threaded=True)


# Entry point check to run the application
if __name__ == "__main__":
    main()
