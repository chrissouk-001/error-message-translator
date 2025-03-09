"""
Entry point for the Flask application.

This file serves as the entry point for running the Error Message Translator application.
"""
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
    args = parser.parse_args()

    # Start the Flask application with debug mode enabled
    app.run(debug=True, port=args.port)


# Entry point check to run the application
if __name__ == "__main__":
    main()
