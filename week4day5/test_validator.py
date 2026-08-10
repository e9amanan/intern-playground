"""Unit tests for validators.DataValidator — the EXTRACT/VALIDATE stage."""

import pytest

from week4day2.validators import DataValidator


def test_valid_row_is_yielded(csv_file):
    path = csv_file(
        "title,description,status,categories,due_date\n"
        'Setup Django,Initial config,done,"Python,Backend",2026-08-01\n'
    )
    v = DataValidator()
    results = list(v.validate_task_csv(path))

    assert len(results) == 1
    assert results[0]["title"] == "Setup Django"
    assert results[0]["categories"] == ["Python", "Backend"]
    assert v.errors == []


def test_validate_task_csv_is_a_generator(csv_file):
    path = csv_file("title,description,status,categories,due_date\n")
    v = DataValidator()
    gen = v.validate_task_csv(path)
    # it's a generator, not a materialized list
    assert hasattr(gen, "__next__")


def test_empty_title_is_rejected(csv_file):
    path = csv_file(
        "title,description,status,categories,due_date\n"
        ",Empty title test,todo,Error,2026-08-02\n"
    )
    v = DataValidator()
    results = list(v.validate_task_csv(path))

    assert results == []
    assert len(v.errors) == 1
    assert v.errors[0]["field"] == "title"
    assert v.errors[0]["row"] == 1


def test_whitespace_only_title_is_rejected(csv_file):
    path = csv_file(
        "title,description,status,categories,due_date\n" "   ,desc,todo,Python,\n"
    )
    v = DataValidator()
    results = list(v.validate_task_csv(path))
    assert results == []
    assert v.errors[0]["field"] == "title"


@pytest.mark.parametrize("bad_status", ["invalid_stat", "", "Done", "TODO"])
def test_invalid_status_is_rejected(csv_file, bad_status):
    path = csv_file(
        "title,description,status,categories,due_date\n"
        f"Task,desc,{bad_status},Python,\n"
    )
    v = DataValidator()
    results = list(v.validate_task_csv(path))
    assert results == []
    assert v.errors[0]["field"] == "status"


def test_malformed_due_date_is_rejected(csv_file):
    path = csv_file(
        "title,description,status,categories,due_date\n"
        "Task,desc,todo,Python,not-a-date\n"
    )
    v = DataValidator()
    results = list(v.validate_task_csv(path))
    assert results == []
    assert v.errors[0]["field"] == "due_date"


def test_missing_due_date_is_valid(csv_file):
    path = csv_file(
        "title,description,status,categories,due_date\n" "Task,desc,todo,Python,\n"
    )
    v = DataValidator()
    results = list(v.validate_task_csv(path))
    assert len(results) == 1
    assert results[0]["due_date"] is None
    assert results[0]["due_date_parsed"] is None


def test_valid_due_date_is_parsed_once_and_reused(csv_file):
    path = csv_file(
        "title,description,status,categories,due_date\n"
        "Task,desc,todo,Python,2026-08-01\n"
    )
    v = DataValidator()
    results = list(v.validate_task_csv(path))
    assert results[0]["due_date"] == "2026-08-01"
    assert results[0]["due_date_parsed"].year == 2026
    assert results[0]["due_date_parsed"].month == 8
    assert results[0]["due_date_parsed"].day == 1


def test_categories_are_split_and_stripped(csv_file):
    path = csv_file(
        "title,description,status,categories,due_date\n"
        'Task,desc,todo,"Python, Backend ,  SQL",\n'
    )
    v = DataValidator()
    results = list(v.validate_task_csv(path))
    assert results[0]["categories"] == ["Python", "Backend", "SQL"]


def test_missing_categories_column_yields_empty_list(csv_file):
    path = csv_file("title,description,status,due_date\n" "Task,desc,todo,\n")
    v = DataValidator()
    results = list(v.validate_task_csv(path))
    assert results[0]["categories"] == []


def test_multiple_rows_mixed_valid_invalid(csv_file):
    path = csv_file(
        "title,description,status,categories,due_date\n"
        'Good One,desc,done,"Python,Backend",2026-08-01\n'
        ",Empty title test,todo,Error,2026-08-02\n"
        "Bad Status,desc,invalid_stat,Django,\n"
        'Good Two,desc,in_progress,"Django,SQL",2026-08-05\n'
    )
    v = DataValidator()
    results = list(v.validate_task_csv(path))
    assert len(results) == 2
    assert len(v.errors) == 2
    assert [r["title"] for r in results] == ["Good One", "Good Two"]


def test_errors_accumulate_across_multiple_calls_same_validator(csv_file):
    path1 = csv_file("title,description,status,categories,due_date\n,d,todo,c,\n")
    v = DataValidator()
    list(v.validate_task_csv(path1))
    assert len(v.errors) == 1
    # calling again on a second file appends rather than resetting
    path2 = csv_file("title,description,status,categories,due_date\n,d,todo,c,\n")
    list(v.validate_task_csv(path2))
    assert len(v.errors) == 2