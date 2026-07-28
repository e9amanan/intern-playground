import pytest


@pytest.fixture
def sample_string_list():
    """Provides a list with duplicates for frequency and dedupe testing."""
    return ["apple", "banana", "apple", "orange", "banana", "apple"]


@pytest.fixture
def sample_dict_list():
    """Provides a list of dictionaries for group_by testing."""
    return [
        {"id": 1, "status": "todo", "task": "Write tests"},
        {"id": 2, "status": "done", "task": "Learn pytest"},
        {"id": 3, "status": "todo", "task": "Mocking"},
    ]


@pytest.fixture
def sample_number_dict():
    """Provides a basic dictionary for mapping testing."""
    return {"a": 10, "b": 20, "c": 30}
