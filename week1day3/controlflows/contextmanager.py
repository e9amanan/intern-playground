"""
practice of context manager in python
"""

with open("data.csv", "w") as file:
    file.write("id,name\n1,Test")


class TimerContext:
    import time

    def __enter__(self):
        self.start_time = self.time.time()
        print("Timer started...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        duration = self.time.time() - self.start_time
        print(f"Timer stopped. Block took {duration:.4f} seconds.")


with TimerContext():
    sum([x * x for x in range(1000000)])
