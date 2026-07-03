counter = 0

def increment():
    """What happens here? How to modify global counter?"""
    counter += 1  # this will throw an error as we need to mention global counter in the function itself rn python will consider this local that doesnt exist

def outer():
    x = "outer"
    def inner():
        x = "inner"
        return x     #inner will return python will consider the local variable first acc to the LEGB rule
    return inner()  # What gets returned?