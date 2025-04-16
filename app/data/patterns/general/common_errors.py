"""
General Common Error Patterns

This module contains error patterns that apply across multiple programming languages.
"""

from app.data.patterns.general import PATTERNS

# Permission Denied
PATTERNS.append({
    "regex": r"Permission denied|Access denied|Operation not permitted",
    "title": "Permission Denied",
    "explanation": "Your program doesn't have the necessary permissions to access a file or resource. This is a system-level restriction rather than a programming error.",
    "solution": "Check the file or directory permissions. You may need to change permissions with chmod (Unix/Mac) or file properties (Windows), or run the program with elevated privileges.",
    "code_example": """
# Unix/Mac solution
chmod +r filename  # For read permission
chmod +w filename  # For write permission
chmod +x filename  # For execute permission

# Or for all permissions
chmod 755 directory_name  # For directories (rwx for owner, rx for others)
chmod 644 filename  # For files (rw for owner, r for others)

# Windows solution (Command Prompt as Administrator)
icacls "filename" /grant YourUsername:F  # F for Full control

# Or run your program as administrator/with sudo
sudo python script.py  # On Unix/Mac
# Run as Administrator on Windows
""",
    "related_errors": ["Access denied", "Operation not permitted"],
    "difficulty": "intermediate"
})

# File Not Found
PATTERNS.append({
    "regex": r"No such file or directory|File not found|Cannot find",
    "title": "File Not Found",
    "explanation": "Your program is trying to access a file or directory that doesn't exist or is in a different location than expected.",
    "solution": "Check if the file exists and is in the location your program is looking for it. Verify the path, correct any typos in the filename, or create the file if it's supposed to be there.",
    "code_example": """
# Check if file exists before trying to access it
import os

file_path = "example.txt"
if os.path.exists(file_path):
    # File exists, proceed
    with open(file_path, 'r') as file:
        content = file.read()
else:
    # File doesn't exist, handle this case
    print(f"Warning: {file_path} does not exist")
    # Consider creating the file or using a default
    with open(file_path, 'w') as file:
        file.write("Default content")
""",
    "related_errors": ["FileNotFoundError", "ENOENT", "Cannot open"],
    "difficulty": "beginner"
})

# Memory Error
PATTERNS.append({
    "regex": r"Out of memory|Memory limit|MemoryError|allocation failed|Cannot allocate memory",
    "title": "Out of Memory Error",
    "explanation": "Your program is trying to use more memory than is available. This often happens when working with large datasets, creating too many objects, or in infinite recursion.",
    "solution": "Optimize your code to use less memory. Consider processing data in smaller chunks, using generators for large datasets, or fixing recursive functions that might be causing a stack overflow.",
    "code_example": """
# Instead of loading entire dataset into memory:
# Bad approach
with open('large_file.csv', 'r') as file:
    all_data = file.readlines()  # Might cause memory error for very large files
    for line in all_data:
        process(line)

# Better approach - process one line at a time
with open('large_file.csv', 'r') as file:
    for line in file:  # File is read line by line, not all at once
        process(line)
        
# For large data processing, consider using generators
def process_large_dataset(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield process_line(line)  # Return one result at a time

# Then use it like:
for result in process_large_dataset('large_file.csv'):
    do_something_with(result)
""",
    "related_errors": ["StackOverflowError", "Segmentation fault", "allocation failed"],
    "difficulty": "advanced"
})

# Timeout Error
PATTERNS.append({
    "regex": r"Timeout|timed out|deadline exceeded",
    "title": "Operation Timed Out",
    "explanation": "Your program took too long to complete an operation, and it was interrupted. This could be due to slow network connections, inefficient code, or trying to process too much data at once.",
    "solution": "Optimize your code to be more efficient, add timeout handling for network operations, or break large operations into smaller chunks that can complete within the time limit.",
    "code_example": """
# Python example with timeout handling for network requests
import requests
from requests.exceptions import Timeout

try:
    # Set a timeout for the request (in seconds)
    response = requests.get('https://example.com', timeout=5)
    response.raise_for_status()  # Raise an exception for 4XX/5XX responses
except Timeout:
    print("The request timed out. The server might be slow or unreachable.")
    # Implement a retry mechanism or fallback
    # Maybe try again with a longer timeout
    try:
        response = requests.get('https://example.com', timeout=10)
    except Timeout:
        print("Still timing out, using cached data instead")
        response = get_cached_data()
except requests.RequestException as e:
    print(f"Request failed: {e}")
""",
    "related_errors": ["Connection timeout", "Read timeout", "Deadline exceeded"],
    "difficulty": "intermediate"
})

# Encoding Error
PATTERNS.append({
    "regex": r"Encoding error|UnicodeDecodeError|UnicodeEncodeError|character encoding|codec can't",
    "title": "Character Encoding Error",
    "explanation": "Your program encountered text that it couldn't encode or decode properly. This happens when working with text in different encodings (like UTF-8, ASCII, etc.) without proper handling.",
    "solution": "Explicitly specify the encoding when reading from or writing to files. Use UTF-8 for most modern applications, or identify and use the correct encoding for your specific data.",
    "code_example": """
# Python example with proper encoding handling

# Reading a file with explicit encoding
with open('file.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# For files with unknown encoding, you might need to try different encodings
encodings_to_try = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
for encoding in encodings_to_try:
    try:
        with open('file.txt', 'r', encoding=encoding) as file:
            content = file.read()
            print(f"Successfully read with {encoding} encoding")
            break
    except UnicodeDecodeError:
        print(f"Failed to decode with {encoding} encoding")

# Writing to a file with explicit encoding
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write("Text with unicode characters: äöüß")
""",
    "related_errors": ["UnicodeError", "codec can't decode", "codec can't encode"],
    "difficulty": "intermediate"
})

# Connection Refused
PATTERNS.append({
    "regex": r"Connection refused|ECONNREFUSED|connection was forcibly closed|could not connect to server",
    "title": "Connection Refused",
    "explanation": "Your program tried to connect to a server or service, but the connection was refused. This usually means the server is not running, is not accepting connections, or is blocked by a firewall.",
    "solution": "Check that the server or service is running and listening on the correct port. Make sure there are no firewall or network issues blocking the connection. Verify the hostname and port are correct.",
    "code_example": """
# Example in Python
import socket
s = socket.socket()
try:
    s.connect(('localhost', 5432))
except ConnectionRefusedError:
    print("Could not connect to the server. Is it running?")

# Example in JavaScript (Node.js)
const net = require('net');
const client = net.createConnection({ port: 5432 }, () => {});
client.on('error', (err) => {
  if (err.code === 'ECONNREFUSED') {
    console.log('Connection refused. Is the server running?');
  }
});
""",
    "related_errors": ["Connection timed out", "Network unreachable", "Server not found"],
    "difficulty": "beginner",
})

# Disk Full / No Space Left
PATTERNS.append({
    "regex": r"Disk full|No space left on device|ENOSPC",
    "title": "Disk Full / No Space Left",
    "explanation": "The system has run out of disk space. Your program tried to write to a file or perform an operation that required more disk space than available.",
    "solution": "Free up disk space on the relevant drive or partition. Delete unnecessary files, clear caches, or move data to another storage location. Increase the disk size if possible.",
    "code_example": """
# Check disk space before performing large writes (platform-specific)

# Linux/Mac (using os module in Python)
import os
stat = os.statvfs('/')  # Check root partition
free_space_gb = (stat.f_bavail * stat.f_frsize) / (1024**3)

if free_space_gb < 1: # Example: check if less than 1GB free
    print("Warning: Low disk space!")
    # Handle the situation, e.g., stop the operation or notify the user

# General solution: Clean up disk space manually or via scripts
# Example commands (Linux/Mac):
# Check usage: df -h
# Find large files/dirs: du -sh /path/to/check/* | sort -rh | head -n 10
# Remove logs: rm /var/log/*.log
# Clear package cache (Debian/Ubuntu): sudo apt-get clean
# Clear package cache (Fedora): sudo dnf clean all
""",
    "related_errors": ["IOException", "Permission denied"],
    "difficulty": "intermediate",
}) 