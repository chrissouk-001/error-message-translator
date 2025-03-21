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
    debug_mode = False if args.prod else (args.debug or 'FLASK_DEBUG' in os.environ)
    
    # In production, only bind to loopback unless explicitly specified
    host = args.host
    
    # Configure production settings
    if args.prod:
        host = os.environ.get('HOST', '127.0.0.1')  # Default to loopback in production
        # Ensure we're not exposing debug features
        os.environ['FLASK_DEBUG'] = 'False'
        app.config['DEBUG'] = False
        print("Running in production mode with secure settings")
    
    # Start the Flask application with appropriate settings
    app.run(debug=debug_mode, host=host, port=args.port)


# Entry point check to run the application
if __name__ == "__main__":
    main()
