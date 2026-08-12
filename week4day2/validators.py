# validators.py
import csv
import json
from datetime import datetime


class DataValidator:
    def __init__(self):
        self.errors = []

    def log_error(self, row_idx, field, message):
        self.errors.append({"row": row_idx, "field": field, "error": message})

    def validate_task_csv(self, file_path):
        valid_data = []
        with open(file_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for idx, row in enumerate(reader, start=1):
                row_valid = True

                # Title Validation
                if not row.get("title") or not row["title"].strip():
                    self.log_error(idx, "title", "Title cannot be empty")
                    row_valid = False

                # Status Validation
                valid_statuses = ["todo", "in_progress", "done"]
                if row.get("status") not in valid_statuses:
                    self.log_error(
                        idx, "status", f"Status must be one of {valid_statuses}"
                    )
                    row_valid = False

                # Date Validation (if present)
                if row.get("due_date"):
                    try:
                        datetime.strptime(row["due_date"], "%Y-%m-%d")
                    except ValueError:
                        self.log_error(idx, "due_date", "Format must be YYYY-MM-DD")
                        row_valid = False

                if row_valid:
                    valid_data.append(
                        {
                            "title": row["title"].strip(),
                            "description": row.get("description", "").strip(),
                            "status": row["status"],
                            "categories": [
                                c.strip()
                                for c in row.get("categories", "").split(",")
                                if c.strip()
                            ],
                        }
                    )
        return valid_data
