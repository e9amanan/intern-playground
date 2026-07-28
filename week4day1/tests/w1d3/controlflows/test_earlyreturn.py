import pytest

from week1day3.controlflows.earlyreturn import process_upload_clean


@pytest.mark.parametrize(
    "file_data, expected",
    [
        ("", "No data"),  # Empty string (falsy)
        (None, "No data"),  # None (falsy)
        ("document.txt", "Not a CSV"),  # Wrong extension
        ("report.csv", "Processed successfully"),  # Happy path
    ],
)
def test_process_upload_clean(file_data, expected):
    """Test early return logic based on file types and empty data."""
    assert process_upload_clean(file_data) == expected
