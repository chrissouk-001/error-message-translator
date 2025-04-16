"""
Java Runtime Exception Patterns

This module contains error patterns for Java runtime exceptions.
"""

from app.data.patterns.java import PATTERNS

# NullPointerException
PATTERNS.append({
    "regex": r"java\.lang\.NullPointerException(?:\s*:\s*(.+))?",
    "title": "Null Pointer Exception",
    "explanation": "You tried to use an object reference that's null. This happens when you try to access methods or fields of an object that hasn't been initialized or has been set to null.",
    "solution": "Always check if an object is null before using it. Use conditional checks to handle null cases, or make sure objects are properly initialized before use.",
    "code_example": """
// Incorrect:
public class Example {
    public static void main(String[] args) {
        String text = null;
        int length = text.length();  // NullPointerException - calling a method on null
    }
}

// Correct:
public class Example {
    public static void main(String[] args) {
        // Option 1: Check for null before using
        String text = null;
        if (text != null) {
            int length = text.length();
            System.out.println(length);
        } else {
            System.out.println("Text is null");
        }
        
        // Option 2: Initialize with a non-null value
        String safeText = "";  // Empty string instead of null
        int safeLength = safeText.length();  // Works fine (returns 0)
        
        // Option 3: Use Java 8+ Optional for cleaner null handling
        import java.util.Optional;
        Optional<String> optText = Optional.ofNullable(text);
        optText.ifPresent(t -> System.out.println(t.length()));
    }
}
""",
    "related_errors": ["java.lang.IllegalArgumentException"],
    "difficulty": "beginner",
})

# ArrayIndexOutOfBoundsException
PATTERNS.append({
    "regex": r"java\.lang\.ArrayIndexOutOfBoundsException(?::\s+Index\s+(\d+)\s+out\s+of\s+bounds\s+for\s+length\s+(\d+))?",
    "title": "Array Index Out of Bounds: Index {{$1}} for Length {{$2}}",
    "explanation": "You're trying to access an element at index {{$1}} in an array with length {{$2}}. Valid indices are from 0 to length-1, so this index is outside the valid range.",
    "solution": "Make sure your array indices are within the valid range (0 to array.length-1). Check your loop conditions and array access logic to avoid going beyond the array boundaries.",
    "code_example": """
// Incorrect:
public class Example {
    public static void main(String[] args) {
        int[] numbers = new int[5];  // Array with 5 elements (indices 0-4)
        numbers[5] = 10;  // ArrayIndexOutOfBoundsException - index 5 is out of bounds for length 5
    }
}

// Correct:
public class Example {
    public static void main(String[] args) {
        int[] numbers = new int[5];  // Array with 5 elements (indices 0-4)
        
        // Option 1: Use a valid index
        numbers[4] = 10;  // Last valid index is 4
        
        // Option 2: Use a loop with proper bounds
        for (int i = 0; i < numbers.length; i++) {  // Note the < (not <=)
            numbers[i] = i * 10;
        }
        
        // Option 3: Use enhanced for loop to avoid index issues
        for (int number : numbers) {
            System.out.println(number);
        }
    }
}
""",
    "related_errors": ["java.lang.StringIndexOutOfBoundsException", "java.lang.IndexOutOfBoundsException"],
    "difficulty": "beginner",
})

# ClassCastException
PATTERNS.append({
    "regex": r"java\.lang\.ClassCastException(?::\s+([a-zA-Z0-9._$]+)\s+cannot\s+be\s+cast\s+to\s+([a-zA-Z0-9._$]+))?",
    "title": "Invalid Class Cast: {{$1}} to {{$2}}",
    "explanation": "You're trying to cast an object of type '{{$1}}' to type '{{$2}}', but this cast is not valid. The object is not an instance of '{{$2}}' or any of its subclasses.",
    "solution": "Only cast objects to compatible types. Use 'instanceof' to check an object's type before casting, or restructure your code to avoid the need for casting.",
    "code_example": """
// Incorrect:
public class Example {
    public static void main(String[] args) {
        Object obj = new Integer(42);
        String str = (String) obj;  // ClassCastException - Integer cannot be cast to String
    }
}

// Correct:
public class Example {
    public static void main(String[] args) {
        Object obj = new Integer(42);
        
        // Option 1: Check type before casting
        if (obj instanceof String) {
            String str = (String) obj;
            System.out.println(str);
        } else {
            System.out.println("Object is not a String");
        }
        
        // Option 2: Cast to the correct type
        if (obj instanceof Integer) {
            Integer num = (Integer) obj;
            System.out.println(num);
        }
        
        // Option 3: Use Java 16+ pattern matching for instanceof
        if (obj instanceof String str) {  // Java 16+ feature
            System.out.println(str);
        }
    }
}
""",
    "related_errors": ["java.lang.IllegalArgumentException"],
    "difficulty": "intermediate",
})

# NumberFormatException
PATTERNS.append({
    "regex": r"java\.lang\.NumberFormatException(?::\s+([^:]+))?",
    "title": "Invalid Number Format: {{$1}}",
    "explanation": "You're trying to convert a string to a number, but the string doesn't have a valid number format. The error message indicates what was wrong: '{{$1}}'.",
    "solution": "Make sure the string represents a valid number before trying to parse it. Add validation or error handling to deal with incorrect input formats.",
    "code_example": """
// Incorrect:
public class Example {
    public static void main(String[] args) {
        String input = "42abc";
        int number = Integer.parseInt(input);  // NumberFormatException - "42abc" is not a valid number
    }
}

// Correct:
public class Example {
    public static void main(String[] args) {
        // Option 1: Use try-catch to handle parsing errors
        String input = "42abc";
        try {
            int number = Integer.parseInt(input);
            System.out.println(number);
        } catch (NumberFormatException e) {
            System.out.println("Invalid number format: " + input);
        }
        
        // Option 2: Validate the string before parsing
        if (input.matches("\\d+")) {  // Check if string contains only digits
            int number = Integer.parseInt(input);
            System.out.println(number);
        } else {
            System.out.println("Not a valid integer: " + input);
        }
    }
}
""",
    "related_errors": ["java.lang.IllegalArgumentException"],
    "difficulty": "beginner",
})

# ArithmeticException: / by zero
PATTERNS.append({
    "regex": r"java\.lang\.ArithmeticException(?::\s+\/\s+by\s+zero)?",
    "title": "Division by Zero",
    "explanation": "You're trying to divide a number by zero, which is not allowed in Java for integer division. This is a common mathematical error that happens in calculations where the divisor could be zero.",
    "solution": "Always check if the divisor is zero before performing division. Add conditions to handle this case or provide alternative logic when the divisor is zero.",
    "code_example": """
// Incorrect:
public class Example {
    public static void main(String[] args) {
        int a = 10;
        int b = 0;
        int result = a / b;  // ArithmeticException: / by zero
    }
}

// Correct:
public class Example {
    public static void main(String[] args) {
        int a = 10;
        int b = 0;
        
        // Option 1: Check for zero before dividing
        if (b != 0) {
            int result = a / b;
            System.out.println(result);
        } else {
            System.out.println("Cannot divide by zero");
        }
        
        // Option 2: Use a try-catch block
        try {
            int result = a / b;
            System.out.println(result);
        } catch (ArithmeticException e) {
            System.out.println("Division by zero error");
        }
        
        // Option 3: Use double instead of int for mathematical safety
        double x = 10.0;
        double y = 0.0;
        double z = x / y;  // Returns Infinity instead of throwing an exception
        System.out.println(z);  // Prints "Infinity"
    }
}
""",
    "related_errors": ["java.lang.NumberFormatException"],
    "difficulty": "beginner",
})

# Add ConcurrentModificationException pattern
PATTERNS.append({
    "regex": r"java\.util\.ConcurrentModificationException(?:\s+at\s+(.+))?",
    "title": "Concurrent Modification Exception",
    "explanation": "You're trying to modify a collection (like ArrayList, HashMap, etc.) while iterating over it with a for-each loop or Iterator.",
    "solution": "Don't modify a collection while iterating over it. Instead, use an Iterator with its remove() method, use removeIf(), or create a copy of the collection to modify.",
    "code_example": """
// Incorrect:
ArrayList<String> list = new ArrayList<>(Arrays.asList("A", "B", "C"));
for (String element : list) {
    if (element.equals("B")) {
        list.remove(element);  // ConcurrentModificationException
    }
}

// Correct with Iterator:
ArrayList<String> list = new ArrayList<>(Arrays.asList("A", "B", "C"));
Iterator<String> iterator = list.iterator();
while (iterator.hasNext()) {
    String element = iterator.next();
    if (element.equals("B")) {
        iterator.remove();  // Safe removal during iteration
    }
}

// Correct with Java 8+ removeIf:
ArrayList<String> list = new ArrayList<>(Arrays.asList("A", "B", "C"));
list.removeIf(element -> element.equals("B"));
""",
    "related_errors": ["UnsupportedOperationException"],
    "difficulty": "intermediate",
})

# Add ClassCastException pattern
PATTERNS.append({
    "regex": r"java\.lang\.ClassCastException: ([^\s]+) cannot be cast to ([^\s]+)",
    "title": "Invalid Class Cast",
    "explanation": "You're trying to cast an object of type {{$1}} to type {{$2}}, but these types are not compatible for casting.",
    "solution": "Make sure you only cast objects to compatible types. Use 'instanceof' to check if an object is of a particular type before casting it.",
    "code_example": """
// Incorrect:
Object obj = new Integer(42);
String str = (String) obj;  // ClassCastException: Integer cannot be cast to String

// Correct with type check:
Object obj = new Integer(42);
if (obj instanceof String) {
    String str = (String) obj;
} else {
    // Handle case where obj is not a String
    System.out.println("Not a string: " + obj);
}

// Better with Java 10+ var and no casting:
var number = 42;  // Inferred as int
var text = number.toString();  // No casting needed
""",
    "related_errors": ["ArrayStoreException"],
    "difficulty": "beginner",
})

# Add IllegalArgumentException pattern
PATTERNS.append({
    "regex": r"java\.lang\.IllegalArgumentException(?::\s*(.+))?",
    "title": "Illegal Argument Exception: {{$1}}",
    "explanation": "You passed an argument to a method that is not valid or appropriate for that method, as described by the message: '{{$1}}'.",
    "solution": "Check the documentation for the method you're calling to understand the expected arguments. Ensure the value you're passing meets the method's requirements (e.g., within a specific range, not null, correct format).",
    "code_example": """
// Incorrect:
public class Example {
    public void setAge(int age) {
        if (age < 0) {
            throw new IllegalArgumentException("Age cannot be negative");
        }
        // ...
    }
    public static void main(String[] args) {
        Example ex = new Example();
        ex.setAge(-5);  // IllegalArgumentException: Age cannot be negative
    }
}

// Correct:
public class Example {
    public void setAge(int age) {
        if (age < 0) {
            throw new IllegalArgumentException("Age cannot be negative");
        }
        // ...
    }
    public static void main(String[] args) {
        Example ex = new Example();
        int inputAge = 25;
        if (inputAge >= 0) { // Validate before calling
            ex.setAge(inputAge);
        } else {
            System.out.println("Invalid age provided.");
        }
    }
}
""",
    "related_errors": ["java.lang.NullPointerException", "java.lang.NumberFormatException"],
    "difficulty": "beginner",
})

# Add NoSuchElementException pattern
PATTERNS.append({
    "regex": r"java\.util\.NoSuchElementException(?:\s+at\s+(.+))?",
    "title": "No Such Element Exception",
    "explanation": "You're trying to access an element that doesn't exist, typically when using an Iterator, Scanner, or retrieving the first element from an empty collection.",
    "solution": "Always check if an element exists before trying to access it. Use hasNext() for iterators and scanners, or isEmpty() for collections.",
    "code_example": """
// Incorrect:
LinkedList<String> list = new LinkedList<>();
String first = list.getFirst();  // NoSuchElementException: list is empty

// Incorrect Iterator usage:
Iterator<String> it = list.iterator();
String element = it.next();  // NoSuchElementException: no more elements

// Correct with check:
LinkedList<String> list = new LinkedList<>();
if (!list.isEmpty()) {
    String first = list.getFirst();  // Safe, we checked first
}

// Correct Iterator usage:
Iterator<String> it = list.iterator();
if (it.hasNext()) {
    String element = it.next();  // Safe, we checked first
}
""",
    "related_errors": ["IndexOutOfBoundsException", "EmptyStackException"],
    "difficulty": "beginner",
})

# Add OutOfMemoryError pattern
PATTERNS.append({
    "regex": r"java\.lang\.OutOfMemoryError: ([^\n]+)",
    "title": "Out of Memory Error",
    "explanation": "Your Java program has exhausted its available memory. The specific issue is: {{$1}}",
    "solution": "Reduce memory usage by fixing memory leaks, using more efficient data structures, or increasing the heap size using JVM flags (-Xmx).",
    "code_example": """
// Common causes of OutOfMemoryError:

// 1. Creating excessively large arrays/collections:
int[] hugeArray = new int[Integer.MAX_VALUE];  // OutOfMemoryError: Java heap space

// 2. Infinite recursion:
void infiniteRecursion() {
    List<Object> list = new ArrayList<>();
    while (true) {
        list.add(new byte[1000000]);  // Eventually: OutOfMemoryError
    }
}

// 3. Memory leaks (objects remain referenced when no longer needed)

// Solutions:
// 1. Increase heap space (command line):
// java -Xmx2g MyApplication

// 2. Fix memory usage in code:
void improvedMethod() {
    // Use try-with-resources for Closeable resources
    try (InputStream is = new FileInputStream("file.txt")) {
        // Resources automatically closed
    } catch (IOException e) {
        // Handle exception
    }
    
    // Use weak references for caches
    Map<Key, SoftReference<Value>> cache = new HashMap<>();
}
""",
    "related_errors": ["StackOverflowError", "GC overhead limit exceeded"],
    "difficulty": "advanced",
}) 