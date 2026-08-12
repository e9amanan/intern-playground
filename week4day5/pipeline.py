"""ETL pipeline: EXTRACT -> VALIDATE -> TRANSFORM -> LOAD for task CSV files."""

import json
import sqlite3
from datetime import datetime

from week4day2.database_practice import setup_database
from week4day2.validators import DataValidator


def enrich_task(task: dict, now: datetime = None) -> dict:
    """TRANSFORM: add category_count and is_overdue to a validated task dict."""
    now = now or datetime.now()
    task["category_count"] = len(task["categories"])
    due = task.pop("due_date_parsed", None)
    task["is_overdue"] = bool(due and due < now)
    return task


def load_to_sqlite(clean_data: list[dict], db_name: str) -> None:
    """LOAD (DB half): insert tasks + categories + junction rows."""
    with sqlite3.connect(db_name) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()

        category_cache = {}
        junction_rows = []

        for task in clean_data:
            cursor.execute(
                """
                INSERT INTO tasks (title, description, status, category_count, is_overdue)
                VALUES (?, ?, ?, ?, ?)
            """,
                (
                    task["title"],
                    task["description"],
                    task["status"],
                    task["category_count"],
                    int(task["is_overdue"]),
                ),
            )

            task_id = cursor.lastrowid

            for cat_name in task["categories"]:
                cat_id = category_cache.get(cat_name)
                if cat_id is None:
                    cursor.execute(
                        "INSERT OR IGNORE INTO categories (name) VALUES (?)",
                        (cat_name,),
                    )
                    cursor.execute(
                        "SELECT id FROM categories WHERE name = ?", (cat_name,)
                    )
                    cat_id = cursor.fetchone()[0]
                    category_cache[cat_name] = cat_id

                junction_rows.append((task_id, cat_id))

        cursor.executemany(
            """
            INSERT INTO tasks_categories (task_id, category_id)
            VALUES (?, ?)
        """,
            junction_rows,
        )


def load_to_json(
    clean_data: list[dict], json_path: str = "validated_tasks.json"
) -> None:
    """LOAD (file half): write validated+enriched records to disk as JSON."""
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(clean_data, f, indent=2, separators=(",", ":"))


def etl_pipeline(
    csv_path: str, db_name: str, json_path: str = "validated_tasks.json"
) -> None:
    """Run the full EXTRACT -> VALIDATE -> TRANSFORM -> LOAD flow for one CSV."""
    print("--- Starting ETL Pipeline ---")

    # 1. EXTRACT & VALIDATE
    print("Extracting and Validating data...")
    validator = DataValidator()
    clean_data = list(validator.validate_task_csv(csv_path))

    if validator.errors:
        print(f"Validation finished with {len(validator.errors)} errors:")
        for err in validator.errors:
            print(f"  Row {err['row']} | Field '{err['field']}': {err['error']}")

    print(f"Successfully extracted {len(clean_data)} valid records.")

    if not clean_data:
        print("No valid data to load. Exiting.")
        return

    # 2. TRANSFORM
    print("Enriching data with derived fields...")
    for task in clean_data:
        enrich_task(task)

    # 3. LOAD (Database & JSON)
    print("Loading to SQLite (with transactions)...")
    setup_database(db_name)
    load_to_json(clean_data, json_path)

    try:
        load_to_sqlite(clean_data, db_name)
        print("Successfully loaded data into SQLite database.")
    except Exception as e:
        print(f"CRITICAL ERROR during LOAD: {e}")
        print("Entire database transaction has been rolled back.")


if __name__ == "__main__":
    etl_pipeline("large_input.csv", "etl_target.db")
