"""
CSV stats script (simple CLI)

    Create tools/csv_stats.py with basic CLI args: --file <path>, --top <n>, --metric <name>.
    Output: row count, numeric column summary (min/max/mean), and top-N rows by the selected column.
    Use argparse for simple argument parsing (no subcommands, logging, or config - just basics).
    Use pathlib for file handling.
    Use sample input: intern_training/data/energy/hourly_prices.csv with --metric price.
    Note: This is a simple introduction to argparse; Week 2 Day 4 adds subcommands and packaging, and Week 4 Day 3 covers professional CLI design (config management, logging, mutually exclusive groups).
    Function specs
        load_csv(file_path: str) -> list[dict[str, str]]
            Input: path to CSV
            Output: list of rows as dicts (string values)
        summarize_numeric(rows: list[dict[str, str]], column: str) -> dict[str, float]
            Input: rows and a numeric column name
            Output: { "min": float, "max": float, "mean": float }
        top_n(rows: list[dict[str, str]], column: str, n: int) -> list[dict[str, str]]
            Input: rows, numeric column, number N
            Output: top N rows sorted descending by the column

"""

"""import argparse
import csv
import sys
from pathlib import Path


def load_csv(file_path: str) -> list[dict[str, str]]:
    
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        print(f"Error: The file '{file_path}' does not exist.")
        sys.exit(1)

    try:
        with path.open(mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        sys.exit(1)


def summarize_numeric(rows: list[dict[str, str]], column: str) -> dict[str, float]:
   
    if not rows:
        return {"min": 0.0, "max": 0.0, "mean": 0.0}

    if column not in rows[0]:
        print(f"Error: Column '{column}' not found in the CSV.")
        sys.exit(1)

    numeric_values = []
    for i, row in enumerate(rows):
        val = row.get(column)
        if not val:
            continue
        try:
            numeric_values.append(float(val))
        except ValueError:
            print(f"Warning: Non-numeric value '{val}' found in row {i+1}. Skipping.")

    if not numeric_values:
        print(f"Error: No valid numeric data found in column '{column}'.")
        sys.exit(1)

    return {
        "min": min(numeric_values),
        "max": max(numeric_values),
        "mean": sum(numeric_values) / len(numeric_values),
    }


def top_n(rows: list[dict[str, str]], column: str, n: int) -> list[dict[str, str]]:
    

    def get_sort_key(row: dict[str, str]) -> float:
        try:
            return float(row.get(column, 0))
        except ValueError:
            return float("-inf")

    sorted_rows = sorted(rows, key=get_sort_key, reverse=True)
    return sorted_rows[:n]


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a CSV file and output statistics."
    )
    parser.add_argument("--file", type=str, required=True, help="Path to the CSV file")
    parser.add_argument(
        "--top", type=int, default=5, help="Number of top rows to display"
    )
    parser.add_argument(
        "--metric", type=str, required=True, help="Numeric column to analyze"
    )

    args = parser.parse_args()

    rows = load_csv(args.file)
    print(f"\nSuccessfully loaded {len(rows)} rows from '{args.file}'.\n")

    stats = summarize_numeric(rows, args.metric)
    print(f"--- Summary for '{args.metric}' ---")
    print(f"Min:  {stats['min']:.2f}")
    print(f"Max:  {stats['max']:.2f}")
    print(f"Mean: {stats['mean']:.2f}\n")

    print(f"--- Top {args.top} by '{args.metric}' ---")
    top_rows = top_n(rows, args.metric, args.top)
    for i, row in enumerate(top_rows, 1):
        print(f"{i}. {row}")


if __name__ == "__main__":
    main()
"""

import argparse
import csv
import sys
from pathlib import Path

def load_csv(file_path: str) -> list[dict[str, str]]:
   
    path = Path(file_path)

    
    if not path.is_file():
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    
    with path.open(mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def summarize_numeric(rows: list[dict[str, str]], column: str) -> dict[str, float]:
    
    if not rows:
        return {"min": 0.0, "max": 0.0, "mean": 0.0}

   
    if column not in rows[0]:
        raise KeyError(f"Column '{column}' not found in the CSV.")

    numeric_values = []
    for row in rows:
        val = row.get(column)
        if not val:
            continue
        try:
            numeric_values.append(float(val))
        except ValueError:
            continue 

    
    if not numeric_values:
        raise ValueError(f"No valid numeric data found in column '{column}'.")

    return {
        "min": min(numeric_values),
        "max": max(numeric_values),
        "mean": sum(numeric_values) / len(numeric_values),
    }

def top_n(rows: list[dict[str, str]], column: str, n: int) -> list[dict[str, str]]:
   
    def get_sort_key(row: dict[str, str]) -> float:
        try:
            return float(row.get(column, 0))
        except (ValueError, TypeError):
            return float("-inf")

    sorted_rows = sorted(rows, key=get_sort_key, reverse=True)
    return sorted_rows[:n]

def main():
    parser = argparse.ArgumentParser(description="Analyze a CSV file and output statistics.")
    parser.add_argument("--file", type=str, required=True, help="Path to the CSV file")
    parser.add_argument("--top", type=int, default=5, help="Number of top rows to display")
    parser.add_argument("--metric", type=str, required=True, help="Numeric column to analyze")

    args = parser.parse_args()

    
    try:
        rows = load_csv(args.file)
        print(f"\nSuccessfully loaded {len(rows)} rows from '{args.file}'.\n")

        stats = summarize_numeric(rows, args.metric)
        print(f"--- Summary for '{args.metric}' ---")
        print(f"Min:  {stats['min']:.2f}")
        print(f"Max:  {stats['max']:.2f}")
        print(f"Mean: {stats['mean']:.2f}\n")

        print(f"--- Top {args.top} by '{args.metric}' ---")
        top_rows = top_n(rows, args.metric, args.top)
        for i, row in enumerate(top_rows, 1):
            print(f"{i}. {row}")

    except (FileNotFoundError, KeyError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


