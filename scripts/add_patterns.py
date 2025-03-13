#!/usr/bin/env python3
"""
Add Error Patterns Script

This script helps you generate and add new error patterns to the appropriate files.
It can process patterns from a CSV or JSON file, or you can use it interactively.
"""

import os
import sys
import json
import csv
import re
from pathlib import Path
import argparse

# Add the parent directory to sys.path to allow importing app modules
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

# Languages supported by the application
SUPPORTED_LANGUAGES = ["python", "javascript", "java", "ruby", "html", "css", "general"]

# Pattern template
PATTERN_TEMPLATE = """\
PATTERNS.append({
    "regex": r"{regex}",
    "title": '{title}',
    "explanation": '{explanation}',
    "solution": '{solution}',
    "code_example": \"\"\"
{code_example}
\"\"\",
    "related_errors": {related_errors},
    "difficulty": "{difficulty}",
})
"""

def create_pattern_category_file(language, category):
    """Create a new pattern category file if it doesn't exist."""
    patterns_dir = os.path.join(parent_dir, "app", "data", "patterns", language)
    os.makedirs(patterns_dir, exist_ok=True)
    
    file_path = os.path.join(patterns_dir, f"{category}.py")
    
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(f'''"""
{language.capitalize()} {category.replace('_', ' ').title()} Patterns

This module contains error patterns for {language.capitalize()} {category.replace('_', ' ').title()} exceptions.
"""

from app.data.patterns.{language} import PATTERNS

# Add patterns below
''')
        print(f"Created new file: {file_path}")
    
    return file_path

def update_init_file(language, category):
    """Update the __init__.py file to import the new category module."""
    init_path = os.path.join(parent_dir, "app", "data", "patterns", language, "__init__.py")
    
    with open(init_path, "r") as f:
        content = f.read()
    
    # Check if import already exists
    import_line = f"from app.data.patterns.{language} import {category}"
    if import_line not in content:
        # Find the try block
        try_block_match = re.search(r"try:\s+([^\n]+)", content)
        if try_block_match:
            # Insert new import after existing imports
            updated_content = content.replace(
                try_block_match.group(1),
                f"{try_block_match.group(1)}\n    from app.data.patterns.{language} import {category}"
            )
            with open(init_path, "w") as f:
                f.write(updated_content)
            print(f"Updated {init_path} to import {category}")
        else:
            print(f"Warning: Could not find try block in {init_path}")

def add_pattern_to_file(file_path, pattern_data):
    """Add a pattern to the specified file."""
    # Convert related_errors to properly formatted list
    if isinstance(pattern_data["related_errors"], str):
        if pattern_data["related_errors"]:
            related_errors = [err.strip() for err in pattern_data["related_errors"].split(",")]
        else:
            related_errors = []
    else:
        related_errors = pattern_data["related_errors"] or []
    
    # Format pattern using the template
    pattern_str = PATTERN_TEMPLATE.format(
        regex=pattern_data["regex"],
        title=pattern_data["title"],
        explanation=pattern_data["explanation"],
        solution=pattern_data["solution"],
        code_example=pattern_data["code_example"],
        related_errors=related_errors,
        difficulty=pattern_data["difficulty"]
    )
    
    # Append to file
    with open(file_path, "a") as f:
        f.write("\n# " + pattern_data.get("comment", "New pattern") + "\n")
        f.write(pattern_str + "\n")
    
    print(f"Added pattern for '{pattern_data['title']}' to {file_path}")

def process_csv_file(csv_file):
    """Process patterns from a CSV file."""
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        patterns = list(reader)
    
    for pattern in patterns:
        language = pattern.get("language", "").lower()
        if language not in SUPPORTED_LANGUAGES:
            print(f"Warning: Unsupported language '{language}'. Skipping pattern.")
            continue
        
        category = pattern.get("category", "general_errors")
        file_path = create_pattern_category_file(language, category)
        update_init_file(language, category)
        add_pattern_to_file(file_path, pattern)
    
    print(f"Processed {len(patterns)} patterns from {csv_file}")

def process_json_file(json_file):
    """Process patterns from a JSON file."""
    with open(json_file, "r", encoding="utf-8") as f:
        patterns = json.load(f)
    
    if isinstance(patterns, dict):
        # Handle format with language as keys
        for language, language_patterns in patterns.items():
            if language not in SUPPORTED_LANGUAGES:
                print(f"Warning: Unsupported language '{language}'. Skipping patterns.")
                continue
            
            for pattern in language_patterns:
                category = pattern.get("category", "general_errors")
                file_path = create_pattern_category_file(language, category)
                update_init_file(language, category)
                add_pattern_to_file(file_path, pattern)
    elif isinstance(patterns, list):
        # Handle flat list of patterns
        for pattern in patterns:
            language = pattern.get("language", "").lower()
            if language not in SUPPORTED_LANGUAGES:
                print(f"Warning: Unsupported language '{language}'. Skipping pattern.")
                continue
            
            category = pattern.get("category", "general_errors")
            file_path = create_pattern_category_file(language, category)
            update_init_file(language, category)
            add_pattern_to_file(file_path, pattern)
    
    print(f"Processed patterns from {json_file}")

def interactive_mode():
    """Interactive mode for adding patterns."""
    print("=== Interactive Pattern Addition ===")
    
    # Get language
    print("\nSupported languages:")
    for i, lang in enumerate(SUPPORTED_LANGUAGES, 1):
        print(f"  {i}. {lang}")
    
    language_idx = int(input("\nSelect language (number): ")) - 1
    language = SUPPORTED_LANGUAGES[language_idx]
    
    # Get category
    category = input("Enter pattern category (e.g., syntax_errors, type_errors): ")
    if not category:
        category = "general_errors"
    
    # Create pattern file
    file_path = create_pattern_category_file(language, category)
    update_init_file(language, category)
    
    # Get pattern details
    pattern = {
        "regex": input("Enter regex pattern: "),
        "title": input("Enter title: "),
        "explanation": input("Enter explanation: "),
        "solution": input("Enter solution: "),
        "code_example": input("Enter code example (use \\n for line breaks): ").replace("\\n", "\n"),
        "related_errors": input("Enter related errors (comma-separated): "),
        "difficulty": input("Enter difficulty (beginner/intermediate/advanced): ") or "beginner",
        "comment": input("Enter comment for this pattern: ") or "New pattern"
    }
    
    # Add pattern to file
    add_pattern_to_file(file_path, pattern)
    
    print("\nPattern added successfully!")

def main():
    parser = argparse.ArgumentParser(description="Add error patterns to the application")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--csv", help="Path to CSV file with patterns")
    group.add_argument("--json", help="Path to JSON file with patterns")
    group.add_argument("--interactive", action="store_true", help="Use interactive mode")
    
    args = parser.parse_args()
    
    if args.csv:
        process_csv_file(args.csv)
    elif args.json:
        process_json_file(args.json)
    elif args.interactive:
        interactive_mode()
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 