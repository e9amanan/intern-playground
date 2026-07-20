"""
Module for defining the Person class.
"""

class Person:
    """A class representing a person with a name and age."""

    def __init__(self, name: str, age: int):
        """Initializes a new Person instance."""
        self.name = name
        self.age = age

    def introduce(self) -> str:
        """Returns a string introducing the person."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    def is_adult(self) -> bool:
        """Checks if the person is an adult (18 or older)."""
        return self.age >= 18


if __name__ == "__main__":
    # This block only runs if the script is executed directly
    PERSON_INSTANCE = Person("Alice", 25)
    print(PERSON_INSTANCE.introduce())
    print(PERSON_INSTANCE.is_adult())