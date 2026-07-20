"""
try except practice
"""


class DataValidationError(Exception):
    """custom exception for bad data"""


def calculatingaverage(numbers_list):
    """Calculates the average of a list of numbers."""
    try:
        total = sum(numbers_list)
        count = len(numbers_list)

        if count == 0:
            raise DataValidationError("cannot calculate average of empty list")
        # Define the result here so the else block can use it
        result = total / count

    except TypeError:
        print("error:list contains non numeric values")
        return None

    except DataValidationError as e:
        print(f"validation error:{e}")
        return None

    else:
        print("calculation succesful")
        return result

    finally:
        print("executionfinished")
