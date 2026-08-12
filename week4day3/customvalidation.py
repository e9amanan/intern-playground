import argparse
from pathlib import Path


def validate_existing_file(filepath_str: str) -> Path:
    """
    Validator function for argparse.

    """
    path = Path(filepath_str)

    if not path.exists():
        raise argparse.ArgumentTypeError(
            f"File not found: '{filepath_str}'. Please check the path and try again."
        )

    if not path.is_file():
        raise argparse.ArgumentTypeError(
            f"Expected a file, but '{filepath_str}' is a directory."
        )

    return path


parser = argparse.ArgumentParser()
parser.add_argument(
    "--file", type=validate_existing_file, help="Path to the source dataset."
)
