"""
Java Compilation Error Patterns

This module contains error patterns for Java compilation errors.
"""

from app.data.patterns.java import PATTERNS

# Cannot find symbol
PATTERNS.append({
    "regex": r"(?:error:|Error:)?\s*cannot find symbol\s+symbol:\s+(?:class|variable|method)\s+([a-zA-Z0-9_]+)",
    "title": "Cannot Find Symbol: {{$1}}",
    "explanation": "Java cannot find a declaration for '{{$1}}'. This means you're trying to use a variable, method, or class that hasn't been declared or imported, or you might have a typo in the name.",
    "solution": "Check for typos in '{{$1}}'. Make sure the variable, method, or class is properly declared. If it's from another package, make sure you've imported it correctly.",
    "code_example": """
// Incorrect:
public class Example {
    public static void main(String[] args) {
        System.out.println(message);  // Error: cannot find symbol - variable message
    }
}

// Correct:
public class Example {
    public static void main(String[] args) {
        String message = "Hello, World!";
        System.out.println(message);  // Works!
    }
}
""",
    "related_errors": ["variable might not have been initialized", "class not found"],
    "difficulty": "beginner",
})

# ';' expected
PATTERNS.append({
    "regex": r"(?:error:|Error:)?\s*';' expected",
    "title": "Missing Semicolon",
    "explanation": "Java requires a semicolon (;) at the end of statements. The compiler found a statement without a semicolon at the end.",
    "solution": "Add a semicolon at the end of the statement. In Java, most statements (except for control structures like if, for, while, and class/method declarations) need to end with a semicolon.",
    "code_example": """
// Incorrect:
public class Example {
    public static void main(String[] args) {
        int x = 10
        System.out.println(x)  // Error: ';' expected
    }
}

// Correct:
public class Example {
    public static void main(String[] args) {
        int x = 10;  // Added semicolon
        System.out.println(x);  // Added semicolon
    }
}
""",
    "related_errors": ["illegal start of expression"],
    "difficulty": "beginner",
})

# Class X is public, should be declared in a file named X.java
PATTERNS.append({
    "regex": r"(?:error:|Error:)?\s*class\s+([A-Za-z0-9_]+)\s+is public, should be declared in a file named\s+([A-Za-z0-9_]+\.java)",
    "title": "Public Class Name Doesn't Match Filename",
    "explanation": "In Java, if a class is declared as public, the file name must match the class name exactly (including capitalization). Your public class '{{$1}}' needs to be in a file named '{{$2}}'.",
    "solution": "Either rename your class to match the file name, or rename your file to match the class name. Remember that Java is case-sensitive, so 'MyClass' and 'myclass' are different names.",
    "code_example": """
// Incorrect (in a file named "program.java"):
public class Example {  // Error: class Example is public, should be declared in a file named Example.java
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

// Correct options:
// Option 1: Rename the file to "Example.java"

// Option 2: Change the class to match the filename
// (in a file named "program.java"):
public class Program {  // Class name now matches file name
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

// Option 3: Remove 'public' if this isn't the main class
// (in a file named "program.java"):
class Example {  // No longer a public class, so no filename requirement
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
""",
    "related_errors": ["cannot find symbol"],
    "difficulty": "beginner",
})

# Incompatible types
PATTERNS.append({
    "regex": r"(?:error:|Error:)?\s*incompatible types:\s+([a-zA-Z0-9_.<>]+)\s+cannot be converted to\s+([a-zA-Z0-9_.<>]+)",
    "title": "Incompatible Types: {{$1}} to {{$2}}",
    "explanation": "Java cannot automatically convert a value of type '{{$1}}' to the required type '{{$2}}'. This happens when you try to assign a value to a variable of an incompatible type.",
    "solution": "Either use an explicit type cast if the conversion is valid, or modify your code to use compatible types. For reference types, make sure there's a proper inheritance relationship.",
    "code_example": """
// Incorrect:
public class Example {
    public static void main(String[] args) {
        int number = "42";  // Error: incompatible types: String cannot be converted to int
    }
}

// Correct:
public class Example {
    public static void main(String[] args) {
        // Option 1: Use the correct type
        String text = "42";  // Use String for text

        // Option 2: Parse the string to get an int
        int number = Integer.parseInt("42");  // Convert String to int

        // Option 3: For object types, ensure proper casting
        Object obj = "Hello";
        String str = (String) obj;  // Explicit cast when you're sure of the type
    }
}
""",
    "related_errors": ["possible lossy conversion", "ClassCastException"],
    "difficulty": "beginner",
})

# Variable might not have been initialized
PATTERNS.append({
    "regex": r"(?:error:|Error:)?\s*variable\s+([a-zA-Z0-9_]+)\s+might not have been initialized",
    "title": "Variable '{{$1}}' Not Initialized",
    "explanation": "You're trying to use the variable '{{$1}}' before giving it a value. In Java, local variables must be explicitly initialized before they can be used.",
    "solution": "Initialize the variable with a value before using it. All local variables in Java must be assigned a value before they are read.",
    "code_example": """
// Incorrect:
public class Example {
    public static void main(String[] args) {
        int x;
        System.out.println(x);  // Error: variable x might not have been initialized
    }
}

// Correct:
public class Example {
    public static void main(String[] args) {
        int x = 0;  // Initialize with a default value
        System.out.println(x);  // Works!
        
        // Or initialize it before using:
        int y;
        y = 10;  // Initialize before use
        System.out.println(y);  // Also works!
    }
}

// Note: Class and instance variables are automatically initialized to default values (0, false, null)
""",
    "related_errors": ["cannot find symbol"],
    "difficulty": "beginner",
})

# Illegal start of expression
PATTERNS.append({
    "regex": r"(?:error:|Error:)?\\s*illegal start of expression",
    "title": "Illegal Start of Expression",
    "explanation": "Java encountered code where it didn't expect an expression. This often happens due to misplaced braces, missing semicolons, or incorrect method/class structure.",
    "solution": "Check for missing or extra braces, misplaced code outside of methods, or missing semicolons. Make sure all statements are inside methods or constructors, and that your class structure is correct.",
    "code_example": """
// Incorrect:
public class Example {
    int x = 10
    public static void main(String[] args) {
        System.out.println(x);
    }
}

// Correct:
public class Example {
    int x = 10;
    public static void main(String[] args) {
        System.out.println(new Example().x);
    }
}
""",
    "related_errors": ["';' expected", "cannot find symbol"],
    "difficulty": "beginner",
}) 