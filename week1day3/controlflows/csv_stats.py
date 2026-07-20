"""
CSV stats script (simple CLI)
Output: row count, numeric column summary (min/max/mean), and top-N rows.
"""

import argparse
import csv
import sys
from pathlib import Path


def load_csv(file_path: str) -> list[dict[str, str]]:
    """Loads a CSV file and returns a list of dictionaries representing the rows."""

    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with path.open(mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def summarize_numeric(rows: list[dict[str, str]], column: str) -> dict[str, float]:
    """Calculates min, max, and mean for a specific numeric column."""
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
    """Returns the top N rows sorted descending by the specified column."""

    def get_sort_key(row: dict[str, str]) -> float:
        try:
            return float(row.get(column, 0))
        except (ValueError, TypeError):
            return float("-inf")

    sorted_rows = sorted(rows, key=get_sort_key, reverse=True)
    return sorted_rows[:n]


def main():
    """Parses CLI arguments and executes the CSV analysis workflow."""
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
