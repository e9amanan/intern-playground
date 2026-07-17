import csv
import json
from pathlib import Path
from .exceptions import DataLoadError

def load_data(file_path: Path) -> list[dict]:
    """Loads CSV or JSON data based on file extension."""
    if not file_path.exists():
        raise DataLoadError(f"file not found: {file_path}")
        
    ext = file_path.suffix.lower()
    
    try:
        if ext == ".csv":
            with file_path.open("r", encoding="utf-8") as f:
                return list(csv.DictReader(f))
        elif ext == ".json":
            with file_path.open("r", encoding="utf-8") as f:
                return json.load(f)
        else:
            raise DataLoadError(f"Unsupported format '{ext}'. Use .csv or .json")
    except json.JSONDecodeError as e:
        raise DataLoadError(f"Malformed JSON in {file_path}: {e}")
    except Exception as e:
        raise DataLoadError(f"Failed to read file: {e}")