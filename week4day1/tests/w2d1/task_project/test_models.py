import pytest
from datetime import date, timedelta
from week2day1.task_project.features.models import Task

def test_task_dataclass_initialization():
    """Test successful creation of a dataclass instance."""
    t = Task(title="Learn Pytest", description="Mocking and Fixtures", status="todo")
    assert t.title == "Learn Pytest"
    assert t.status == "todo"
    assert t.due_date is None

def test_task_post_init_empty_title():
    """Test that an empty title triggers a ValueError in __post_init__."""
    with pytest.raises(ValueError, match="Title cannot be empty"):
        Task(title="   ", description="Empty", status="todo")

def test_task_post_init_past_due_date():
    """Test that a past date triggers a ValueError in __post_init__."""
    past_date = date.today() - timedelta(days=5)
    with pytest.raises(ValueError, match="Due date cannot be in the past"):
        Task(title="Late Task", description="Failed", status="todo", due_date=past_date)

def test_task_advance_status():
    """Test the workflow logic transitions status properly."""
    t = Task(title="Workflow", description="Test", status="todo")
    
    t.advance_status()
    assert t.status == "in_progress"
    
    t.advance_status()
    assert t.status == "done"
    
    # Advancing when already 'done' 
    t.advance_status()
    assert t.status == "done"