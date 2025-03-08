"""
Entry point for the Flask application.

This file serves as the entry point for running the Error Message Translator application.
"""
import argparse
from app import app


# Register routes
@app.route("/")
def index():
    """Render the main page of the application."""
    from flask import render_template

    return render_template("index.html")


def main():
    """Run the Flask application."""
    parser = argparse.ArgumentParser(description="Run the Error Message Translator app")
    parser.add_argument("--port", type=int, default=5001, help="Port to run the app on")
    args = parser.parse_args()

    app.run(debug=True, port=args.port)


if __name__ == "__main__":
    main()
