import pytest

from week2day1.oopsfundamentals import Person, Task, TaskManager, UrgentTask

# --- Person Class Tests ---


@pytest.fixture
def sample_person():
    return Person("Jane", "Doe", 30)


def test_person_initialization(sample_person):
    """Test instance and class attributes."""
    assert sample_person.first_name == "Jane"
    assert sample_person._age == 30
    assert Person.species == "homo sapiens"


def test_person_full_name_property(sample_person):
    """Test the @property decorator for full_name."""
    assert sample_person.full_name == "Jane Doe"


def test_person_full_name_setter(sample_person):
    """Test the @full_name.setter updates underlying attributes."""
    sample_person.full_name = "Ada Lovelace"
    assert sample_person.first_name == "Ada"
    assert sample_person.last_name == "Lovelace"


def test_person_full_name_setter_invalid():
    """Test that the setter raises a ValueError for incomplete names."""
    p = Person("Jane", "Doe", 30)
    with pytest.raises(
        ValueError, match="must provide both a first name and a last name"
    ):
        p.full_name = "Cher"  # Single name should fail


def test_person_dunder_methods(sample_person):
    """Test __str__, __repr__, and __eq__."""
    # Test __str__
    assert str(sample_person) == "Jane Doe, 30 years old"

    # Test __repr__
    assert repr(sample_person) == "Person(full_name='Jane Doe', age=30)"

    # Test __eq__
    clone = Person("Jane", "Doe", 30)
    different = Person("John", "Doe", 30)

    assert sample_person == clone
    assert sample_person != different
    assert sample_person != "Not a Person Object"


# --- Inheritance & Composition Tests ---


def test_task_inheritance():
    """Test that UrgentTask inherits from Task and overrides display()."""
    standard = Task("Buy Groceries")
    urgent = UrgentTask("Pay Bills", "Friday")

    assert standard.display() == "Task: Buy Groceries"
    assert urgent.display() == "Task: Pay Bills (DUE: Friday)"


def test_task_manager_composition():
    """Test that TaskManager can hold and filter a collection of Task objects."""
    manager = TaskManager()
    t1 = Task("Task 1")
    t2 = UrgentTask("Task 2", "Tomorrow")

    # Mark t1 as complete
    t1.completed = True

    manager.add_task(t1)
    manager.add_task(t2)

    pending = manager.get_pending_tasks()

    assert len(pending) == 1
    assert pending[0].title == "Task 2"
