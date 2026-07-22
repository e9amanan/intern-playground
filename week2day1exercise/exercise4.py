"""
Module defining the TaskManager class to handle collections of Tasks.
"""

from exercise3 import Task


class TaskManager:
    """Manages a list of Task objects."""

    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        """Adds a new Task to the manager."""
        self.tasks.append(task)

    def get_incomplete_tasks(self) -> list[Task]:
        """Returns all tasks that are not completed."""
        return [task for task in self.tasks if not task.completed]

    def get_complete_tasks(self) -> list[Task]:
        """Returns all tasks that are completed."""
        return [task for task in self.tasks if task.completed]

    def mark_task_complete(self, title: str) -> bool:
        """
        Marks a task as complete by searching for its title.
        Returns True if found, False otherwise.
        """
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return True

        return False

    def __len__(self) -> int:
        """Returns the number of tasks in the manager."""
        return len(self.tasks)
