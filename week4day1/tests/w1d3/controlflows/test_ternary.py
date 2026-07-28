import pytest

from week1day3.controlflows.ternary import process_user_data


@pytest.mark.parametrize(
    "user_input, is_admin, expected",
    [
        ("", True, "no data"),
        (None, False, "no data"),
        ("admin_payload", True, " processing 13 for super user "),
        ("hello", False, " processing 5 for regular user "),
    ],
)
def test_process_user_data(user_input, is_admin, expected):
    """Test the ternary operator assigning roles based on the boolean flag."""
    assert process_user_data(user_input, is_admin) == expected
