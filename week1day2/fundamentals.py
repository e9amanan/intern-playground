from collections import namedtuple

# Strings
TEXT = "python"
print(TEXT[0:3])
print(TEXT[3:])
print(TEXT[:3])
print(TEXT[::-1])
print(TEXT[::2])
print(TEXT[::2])

AGE = 25
NAME = "alice"
print(f"my name is {NAME} and in 5 years i will be {AGE+5}")

SENTENCE = "lets learn python today"
WORDS = SENTENCE.split(" ")
print(WORDS)

YO = SENTENCE.split("e")
print(YO)

# Pylint fix: Uppercase for global constants
CSV_STRING = ",".join(WORDS)
print(CSV_STRING)

MESSY = " hello world  how are you   "
CLEAN = MESSY.strip()
print(CLEAN)

# Lists
NUMBERS = [1, 2, 3, 4, 5]

DOUBLES = [n * 2 for n in NUMBERS]
print(DOUBLES)

EVENS = [n * 2 for n in NUMBERS if n % 2 == 0]
print(EVENS)

print(NUMBERS[0:2])

NUMBERS.append([3, 4])
print(NUMBERS)

NUMBERS.extend([3, 4])
print(NUMBERS)

NUMS = [5, 1.9]

NEW_NUMS = sorted(NUMS)
print(NEW_NUMS)
print(NUMS)

NUMS.sort()
print(NUMS)

# Tuples
LOCATION = (40.7128, -74.0060)
LAT, LON = LOCATION
print(f"latitude of location is {LAT}")

# Pylint fix: PascalCase for namedtuple classes
Color = namedtuple("Color", ["red", "green", "blue"])
PURE_RED = Color(red=255, green=0, blue=0)
print(PURE_RED.red)

# Dictionaries
EMPLOYEE = {"name": "sarah", "age": 28, "department": "engineering"}

EMPLOYEE["salary"] = 9000
EMPLOYEE["age"] = 25

EMP_LOCATION = EMPLOYEE.get("location")
print(EMP_LOCATION)

# Pylint fix: Iterate dictionary directly
for key in EMPLOYEE:
    print(key)

for value in EMPLOYEE.values():
    print(value)

for key, value in EMPLOYEE.items():
    print(f"employees {key} is {value}")

SQUARE_NUMBERS = [1, 2, 3, 4]
SQUARES = {num: num * num for num in SQUARE_NUMBERS}
print(SQUARES)

# Sets
# Pylint fix: Remove duplicate values from set literal
UNIQUE_NUMBERS = {1, 2, 3, 4}
print(UNIQUE_NUMBERS)

EMPTY_SET = set()

ALLOWED_USERS_LIST = ["alice", "bob", "charlie"]
ALLOWED_USERS_SET = {"alice", "bob", "charlie"}

# Pylint fix: Uppercase for global constants
USER = "bob"
if USER in ALLOWED_USERS_SET:
    print(f"{USER} is allowed in!")

FRONTEND = {"Alice", "Bob", "Charlie"}
BACKEND = {"Charlie", "David", "Eve"}

ALL_DEVS = FRONTEND | BACKEND
print(ALL_DEVS)

FULLSTACK = FRONTEND & BACKEND
print(FULLSTACK)

PURE_FRONTEND = FRONTEND - BACKEND
print(PURE_FRONTEND)

SPECIALISTS = FRONTEND ^ BACKEND
print(SPECIALISTS)
