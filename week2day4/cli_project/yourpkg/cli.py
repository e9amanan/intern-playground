"""
Command Line Interface for time-series data analysis and anomaly detection.
"""

import argparse
import csv

from yourpkg import core
from yourpkg.exceptions import FileProcessingError, ValidationError


def handle_analyze(args) -> int:
    """
    Handle the 'analyze' command to process and display CSV data.

    Args:
        args: Parsed command-line arguments containing file path, metric, and top count.

    Returns:
        int: Exit status code (0 for success).

    Raises:
        SystemExit: On validation, file processing, or unexpected errors.
    """
    try:
        try:
            with open(args.file, "r", encoding="utf-8") as file_handle:
                reader = csv.DictReader(file_handle)
                raw_rows = list(reader)
        except FileNotFoundError as exc:
            # Added 'from exc' to satisfy pylint W0707 (exception chaining)
            raise FileProcessingError(f"The file '{args.file}' was not found.") from exc
        except Exception as exc:  # pylint: disable=broad-exception-caught
            raise FileProcessingError(f"Failed to read file: {exc}") from exc

        clean_data = core.clean_data(raw_rows, args.metric)
        core.display_daily_averages(clean_data)
        core.display_top_spikes(clean_data, args.top)
        core.display_anomalies(clean_data)

        return 0

    except FileProcessingError as exc:
        raise SystemExit(f"File Error: {exc}") from exc
    except ValidationError as exc:
        raise SystemExit(f"Data Validation Error: {exc}") from exc
    except Exception as exc:  # pylint: disable=broad-exception-caught
        raise SystemExit(f"Unexpected processing error: {exc}") from exc


def main(argv=None) -> int:
    """
    Main entry point for the CLI.

    Args:
        argv (list, optional): List of command-line arguments. Defaults to None.

    Returns:
        int: Exit status code.
    """
    parser = argparse.ArgumentParser(
        prog="yourpkg",
        description="A CLI for time-series data analysis and anomaly detection.",
    )

    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands"
    )

    analyze_parser = subparsers.add_parser(
        "analyze", help="Analyze time-series data from a CSV."
    )

    analyze_parser.add_argument(
        "--file", "-f", required=True, help="Path to the CSV file to analyze."
    )

    analyze_parser.add_argument(
        "--metric",
        "-m",
        required=True,
        help="The name of the metric column to extract (e.g., 'price').",
    )

    # FIXED: Changed 'analyze-parser' to 'analyze_parser'
    analyze_parser.add_argument(
        "--top",
        "-t",
        type=int,
        default=3,
        help="Number of top spikes to display (defaults to 3).",
    )

    analyze_parser.set_defaults(func=handle_analyze)

    args = parser.parse_args(argv)
    return args.func(args)
