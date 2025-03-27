"""Base pattern structure for error patterns."""
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ErrorPattern:
    """Represents an error pattern with all its attributes."""
    regex: str
    title: str
    explanation: str
    solution: str
    language: str
    difficulty: str
    code_example: Optional[str] = None
    related_errors: List[str] = None
    
    def __post_init__(self):
        """Validate pattern attributes after initialization."""
        if not self.regex or not self.title or not self.explanation or not self.solution:
            raise ValueError("Required pattern fields cannot be empty")
        if self.difficulty not in ["beginner", "intermediate", "advanced"]:
            raise ValueError("Invalid difficulty level")
        if self.related_errors is None:
            self.related_errors = []