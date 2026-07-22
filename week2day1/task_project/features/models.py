"""
Module demonstrating the use of dataclasses for cleaner, more robust data objects.
"""

from dataclasses import dataclass
from datetime import date
from typing import Literal


@dataclass
class Task:
    """Represents a task with status tracking and validation."""

    title: str
    description: str
    status: Literal["todo", "in_progress", "done"]
    due_date: date | None = None

    def __post_init__(self):
        """
        Runs automatically after __init__ to validate the data.
        """
        if not self.title.strip():
            raise ValueError("Title cannot be empty")

        if self.due_date and self.due_date < date.today():
            raise ValueError("Due date cannot be in the past")

    def advance_status(self):
        """Moves the task forward through its workflow."""
        if self.status == "todo":
            self.status = "in_progress"
        elif self.status == "in_progress":
            self.status = "done"
