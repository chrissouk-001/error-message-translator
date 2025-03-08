from flask import Flask, render_template, request
from pathlib import Path
import os
import argparse
from app.translator import translate_error, detect_language
from app.data.error_patterns import PYTHON_PATTERNS, JAVASCRIPT_PATTERNS, HTML_PATTERNS, CSS_PATTERNS

# Define the Flask app
app = Flask(__name__, 
            static_folder='app/static',
            template_folder='app/templates')

@app.route('/')
def index():
    """Render the main page of the application."""
    return render_template('index.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the Error Message Translator app')
    parser.add_argument('--port', type=int, default=5001, help='Port to run the app on')
    args = parser.parse_args()
    
    app.run(debug=True, port=args.port) 