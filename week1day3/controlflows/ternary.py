"""
ternary operator practice
"""


def process_user_data(user_input, is_admin):
    """Processes the length of user input and assigns a role."""
    if not user_input:
        return "no data"

    role = "super user" if is_admin else "regular user"

    return f" processing {len(user_input)} for {role} "
