"""
Module defining Task and UrgentTask classes demonstrating inheritance.
"""

class Task:
    """Represents a standard task."""

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.completed = False

    def mark_complete(self) -> None:
        """Marks the task as completed."""
        self.completed = True

    def __repr__(self) -> str:
        """Returns a string representation of the task."""
        status = '✓' if self.completed else "o"
        return f"{status} {self.title}"


class UrgentTask(Task):
    """Represents a task with an added deadline."""

    def __init__(self, title: str, description: str, deadline: str):
       
        super().__init__(title, description)
        self.deadline = deadline

    def is_overdue(self, current_date: str) -> bool:
        """Checks if the deadline has passed."""
        
        return self.deadline < current_date

    def __repr__(self) -> str:
        """Returns the base representation plus the deadline."""
        base = super().__repr__()
        return f"{base} (Due: {self.deadline})"