"""
Package your CLI

    Create energy_insights/ package and move CSV logic into it.
    Add __main__.py so it runs with python -m energy_insights --help.
"""

import argparse
import csv
import sys


def main():
    """Main entry point for the CLI to parse arguments and load the CSV."""
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to the target CSV file")
    args = parser.parse_args()

    try:
        with open(args.file, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            print(f"Loaded {len(rows)} rows.")
    except FileNotFoundError:
        print(f"error:file '{args.file}' not found")
        sys.exit(1)


if __name__ == "__main__":
    main()
