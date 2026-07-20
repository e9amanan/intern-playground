"""
practice of context manager in python
"""

import time

with open("data.csv", "w", encoding="utf-8") as file:
    file.write("id,name\n1,Test")


class TimerContext:
    """A context manager to measure execution time of a code block."""

    def __init__(self):
        self.start_time = 0.0

    def __enter__(self):
        self.start_time = time.time()
        print("Timer started...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        duration = time.time() - self.start_time
        print(f"Timer stopped. Block took {duration:.4f} seconds.")


with TimerContext():

    sum(x * x for x in range(1000000))
