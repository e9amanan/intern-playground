from dataclasses import dataclass
from datetime import date
from typing import Literal

@dataclass
class Task:
    """Task with validation."""
    title: str
    description: str
    status: Literal["todo", "in_progress", "done"] = "todo"
    due_date: date | None = None
    
    def __post_init__(self):
        """Validate after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty")
        
        if self.due_date and self.due_date < date.today():
            raise ValueError("Due date cannot be in the past")
    
    def transition_to(self, new_status: Literal["todo", "in_progress", "done"]) -> None:
        """Change status with validation."""
        valid_transitions = {
            "todo": ["in_progress"],
            "in_progress": ["done", "todo"],
            "done": ["todo"]
        }
        
        if new_status not in valid_transitions[self.status]:
            raise ValueError(f"Cannot transition from {self.status} to {new_status}")
        
        self.status = new_status