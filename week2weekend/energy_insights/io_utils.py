"""Utility functions for loading energy data from files."""

import csv
import json
from pathlib import Path

from .exceptions import DataLoadError


def load_data(file_path: Path) -> list[dict]:
    """Loads CSV or JSON data based on file extension."""
    if not file_path.exists():
        raise DataLoadError(f"File not found: {file_path}")

    ext = file_path.suffix.lower()

    try:
        if ext == ".csv":
            with file_path.open("r", encoding="utf-8") as file_handle:
                return list(csv.DictReader(file_handle))

        if ext == ".json":
            with file_path.open("r", encoding="utf-8") as file_handle:
                return json.load(file_handle)

        raise DataLoadError(f"Unsupported format '{ext}'. Use .csv or .json")

    except json.JSONDecodeError as exc:
        raise DataLoadError(f"Malformed JSON in {file_path}: {exc}") from exc
    except Exception as exc:  # pylint: disable=broad-exception-caught
        raise DataLoadError(f"Failed to read file: {exc}") from exc
