# Parameters
def power(base, exponent=2):
    return base**exponent


print(power(3, 3))
print(power(exponent=3, base=3))


def create_profile(name, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Extra positional args: {args}")
    print(f"Extra keyword args: {kwargs}")


create_profile("Alice", 25, "Engineer", location="NYC", active=True)


# Return Values
def get_min_max(numbers):
    return min(numbers), max(numbers)


lowest, highest = get_min_max([10, 20, 5, 40])
print(lowest)
print(highest)

# SCOPE LEGB
GLOBAL_MESSAGE = "Global X"
BUILTIN_OVERRIDE_MESSAGE = "Wait, I just overwrote the built-in len function!"


def outer_function():
    enclosing_msg = "Enclosing X"
    print(enclosing_msg)  # Now the variable is used

    def inner_function():
        local_msg = "Local X"
        print(local_msg)
        print(GLOBAL_MESSAGE)  # Demonstrating global scope access

    inner_function()


outer_function()


# Type Hints
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."
