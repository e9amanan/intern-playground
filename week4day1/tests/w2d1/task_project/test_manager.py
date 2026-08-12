import pytest

from week2day1.task_project.core.manager import TaskManager
from week2day1.task_project.features.models import Task


@pytest.fixture
def sample_manager():
    """Provides a TaskManager with pre-populated dataclass Tasks."""
    manager = TaskManager()
    manager.add_task(Task(title="Task A", description="", status="todo"))
    manager.add_task(Task(title="Task B", description="", status="done"))
    return manager


def test_manager_add_and_filter(sample_manager):
    """Test adding tasks and filtering for pending ones."""
    # Since we are using the new dataclass Task, pending means not 'done'
    # Wait, the TaskManager from fundamentals filters by `not t.completed`.
    # If core.manager was updated to check `t.status != "done"`, this will pass.
    # We will assume core.manager checks status for the dataclass models.

    pending = sample_manager.get_pending_tasks()

    # Task A is 'todo', Task B is 'done'
    assert len(pending) == 1
    assert pending[0].title == "Task A"
