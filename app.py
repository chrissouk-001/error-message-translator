from flask import Flask, render_template, request, jsonify
from pathlib import Path
import os
import json
import argparse
from app.translator import translate_error, detect_language
from app.data.error_patterns import PYTHON_PATTERNS, JAVASCRIPT_PATTERNS, HTML_PATTERNS, CSS_PATTERNS
from flask_cors import CORS

# Define the Flask app as a named variable that can be imported by tests
app = Flask(__name__, 
            static_folder='app/static',
            template_folder='app/templates')

# Enable CORS for all routes
CORS(app)

@app.route('/')
def index():
    """Render the main page of the application."""
    return render_template('index.html')

@app.route('/api/languages')
def get_languages():
    """Return a list of supported programming languages"""
    languages = [
        {'id': 'auto', 'name': 'Auto-detect Language'},
        {'id': 'python', 'name': 'Python'},
        {'id': 'javascript', 'name': 'JavaScript'},
        {'id': 'html', 'name': 'HTML'},
        {'id': 'css', 'name': 'CSS'},
        {'id': 'general', 'name': 'General Code'}
    ]
    return jsonify(languages)

@app.route('/api/translate', methods=['POST'])
def translate():
    """Translate an error message"""
    data = request.get_json()
    
    # Check if error_message is present in the request
    if 'error_message' not in data:
        return jsonify({'error': 'Missing error message'}), 400
    
    error_message = data.get('error_message', '')
    language = data.get('language', 'auto')
    
    # English is now the only output language
    output_language = 'en'
    
    # Translate the error
    translation = translate_error(error_message, language, output_language)
    
    return jsonify(translation)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the Error Message Translator app')
    parser.add_argument('--port', type=int, default=5001, help='Port to run the app on')
    args = parser.parse_args()
    
    app.run(debug=True, port=args.port) 