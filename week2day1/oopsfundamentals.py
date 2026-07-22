"""
Module demonstrating Object-Oriented Programming (OOP) fundamentals.
"""


class Person:
    """A simple class representing a person."""

    species = "homo sapiens"  # Class attribute

    def __init__(self, first_name: str, last_name: str, age: int):
        # Instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self._age = age  # "Private" attribute convention

    @property
    def full_name(self) -> str:
        """Computed property that dynamically combines first and last names."""

        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, name: str):
        parts = name.split(" ")
        if len(parts) < 2:
            raise ValueError("You must provide both a first name and a last name.")

        self.first_name = parts[0]
        self.last_name = " ".join(parts[1:])

    # --- Dunder Methods ---

    def __repr__(self) -> str:
        """Official string representation for debugging."""
        return f"Person(full_name='{self.full_name}', age={self._age})"

    def __str__(self) -> str:
        """Informal string representation for end-users."""

        return f"{self.full_name}, {self._age} years old"

    def __eq__(self, other: object) -> bool:
        """Defines how two Person instances are compared using '=='."""
        if not isinstance(other, Person):
            return NotImplemented

        return self.full_name == other.full_name and self._age == other._age


if __name__ == "__main__":

    p1 = Person("Jane", "Doe", 30)
    p2 = Person("Jane", "Doe", 30)

    print(repr(p1))
    print(p1)
    print(f"Are they equal? {p1 == p2}")

    p1.full_name = "Ada Lovelace"
    print(f"Updated first name: {p1.first_name}")
