"""
Command Line Interface for time-series data analysis and anomaly detection.
"""

import argparse
import csv

from yourpkg import core
from yourpkg.exceptions import ValidationError, FileProcessingError


def _load_csv(file_path: str) -> list[dict]:
    """Extracted helper to handle file operations and error wrapping."""
    try:
        with open(file_path, "r", encoding="utf-8") as file_handle:
            reader = csv.DictReader(file_handle)
            return list(reader)
    except FileNotFoundError as exc:
        raise FileProcessingError(f"The file '{file_path}' was not found.") from exc
    except Exception as exc:
        raise FileProcessingError(f"Failed to read file: {exc}") from exc


def handle_analyze(args) -> int:
    """
    Handle the 'analyze' command to process and display CSV data.
    """
    try:
        # Refactored: Linear flow without nested try/except blocks
        raw_rows = _load_csv(args.file)
        clean_data = core.clean_data(raw_rows, args.metric)
        
        core.display_daily_averages(clean_data)
        core.display_top_spikes(clean_data, args.top)
        core.display_anomalies(clean_data)

        return 0

    except FileProcessingError as exc:
        raise SystemExit(f"File Error: {exc}") from exc
    except ValidationError as exc:
        raise SystemExit(f"Data Validation Error: {exc}") from exc
    except Exception as exc:
        raise SystemExit(f"Unexpected processing error: {exc}") from exc


def main(argv=None) -> int:
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        prog="yourpkg",
        description="A CLI for time-series data analysis and anomaly detection."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="Available commands"
    )

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Analyze time-series data from a CSV."
    )

    analyze_parser.add_argument(
        "--file", "-f",
        required=True,
        help="Path to the CSV file to analyze."
    )

    analyze_parser.add_argument(
        "--metric", "-m",
        required=True,
        help="The name of the metric column to extract (e.g., 'price')."
    )

    analyze_parser.add_argument(
        "--top", "-t",
        type=int,
        default=3,
        help="Number of top spikes to display (defaults to 3)."
    )
    
    analyze_parser.set_defaults(func=handle_analyze)

    args = parser.parse_args(argv)
    return args.func(args)