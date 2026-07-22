"""
Module demonstrating Inheritance and Composition.
"""


class Task:
    """Base class for all tasks."""

    def __init__(self, title: str):
        self.title = title
        self.completed = False

    def display(self) -> str:
        """Returns the basic task title."""
        return f"Task: {self.title}"


class UrgentTask(Task):
    """Subclass that adds a deadline to a task."""

    def __init__(self, title: str, deadline: str):

        super().__init__(title)
        self.deadline = deadline

    def display(self) -> str:
        """Overrides parent display to include the deadline."""

        base_display = super().display()
        return f"{base_display} (DUE: {self.deadline})"


class TaskManager:
    """Class demonstrating composition: a manager containing a list of tasks."""

    def __init__(self):
        self._tasks: list = []

    def add_task(self, task: Task):
        """Adds a Task or UrgentTask object to the manager."""
        self._tasks.append(task)

    def get_pending_tasks(self) -> list:
        """Filters the list for tasks that are not yet completed."""
        return [t for t in self._tasks if not t.completed]
