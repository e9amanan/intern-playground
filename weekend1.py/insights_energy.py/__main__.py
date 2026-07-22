"""
Analyze hourly energy price data from a CSV file.
Computes daily averages, top price spikes, and identifies anomalies.
"""

import argparse
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from statistics import mean, stdev


class ValidationError(Exception):
    """Custom exception for validation errors."""


def parse_arguments():
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Analyze hourly energy price data", exit_on_error=False
    )
    # Changed --File to --file to match args.file usage in main()
    parser.add_argument("--file", required=True, help="CSV file path (required)")
    parser.add_argument(
        "--metric", default="price", help="Column name to analyze (default: 'price')"
    )
    parser.add_argument(
        "--top", type=int, default=10, help="Number of spikes to show (default: 10)"
    )
    return parser.parse_args()


def validate_inputs(file_path, top_n):
    """
    Validate the input file path and the top_n parameter.

    Args:
        file_path (str): Path to the input CSV file.
        top_n (int): Number of spikes to display.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValidationError: If the path is not a file.
        TypeError: If top_n is not an integer.
        ValueError: If top_n is not a positive integer.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    if not path.is_file():
        raise ValidationError(f"The path '{file_path}' exists but is not a file.")

    if not isinstance(top_n, int):
        raise TypeError(
            f"The 'top' argument must be an integer. Got: {type(top_n).__name__}"
        )
    if top_n <= 0:
        raise ValueError(f"The 'top' argument must be a positive integer. Got: {top_n}")


def load_and_clean_data(file_path, metric):
    """
    Load data from the CSV file and clean it.

    Args:
        file_path (str): Path to the input CSV file.
        metric (str): The column name to extract values from.

    Returns:
        list: A list of dictionaries containing parsed timestamps and values.

    Raises:
        ValidationError: If the CSV is empty, missing headers, or lacks valid data rows.
    """
    data = []

    with open(file_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        if not reader.fieldnames:
            raise ValidationError("The CSV file is empty or missing headers.")
        if metric not in reader.fieldnames:
            raise ValidationError(f"Metric column '{metric}' not found in CSV headers.")

        for line_num, row in enumerate(reader, start=2):
            try:
                raw_ts = row["timestamp"].replace("Z", "+00:00")
                ts = datetime.fromisoformat(raw_ts)
                val = float(row[metric])
                data.append({"timestamp": ts, "raw_ts": row["timestamp"], "value": val})
            except (ValueError, KeyError) as exc:
                print(f"Warning: Skipping invalid row {line_num}: {exc}")

    if not data:
        raise ValidationError("No valid data rows found in the CSV.")

    return data


def display_daily_averages(data):
    """
    Calculate and display the daily average prices.

    Args:
        data (list): Cleaned data containing timestamps and values.
    """
    daily_totals = defaultdict(list)
    for row in data:
        day_str = row["timestamp"].strftime("%y-%m-%d")
        daily_totals[day_str].append(row["value"])

    # FIXED: De-indented this block so it runs after data aggregation, not during every loop.
    print("Daily averages:")
    print(f"{'Date':<12} {'Avg Price'}")
    for day, values in sorted(daily_totals.items()):
        avg = mean(values)
        print(f"{day:<12} ${avg:.2f}")
    print()


def display_top_spikes(data, top_n):
    """
    Sort and display the top price spikes.

    Args:
        data (list): Cleaned data containing timestamps and values.
        top_n (int): Number of top spikes to display.
    """
    sorted_data = sorted(data, key=lambda x: x["value"], reverse=True)
    spikes = sorted_data[:top_n]

    print(f"Top {top_n} price spikes: ")
    for spike in spikes:
        print(f"{spike['raw_ts']:<21} ${spike['value']:.2f}")
    print()


def display_anomalies(data):
    """
    Detect and display anomalies using a z-score > 2 threshold.

    Args:
        data (list): Cleaned data containing timestamps and values.
    """
    values = [row["value"] for row in data]

    if len(values) < 2:
        print("Not enough data to calculate standard deviation for anomalies.\n")
        return

    data_mean = mean(values)
    data_std = stdev(values)

    if data_std == 0:
        print("Anomalies detected: 0 as no variance in data.\n")
        return

    anomaly_count = sum(1 for val in values if (abs(val - data_mean) / data_std) > 2)
    print(f"Anomalies detected: {anomaly_count} hour(s) (z-score > 2 threshold)\n")


def main():
    """Main execution function."""
    try:
        args = parse_arguments()

        validate_inputs(args.file, args.top)

        data = load_and_clean_data(args.file, args.metric)

        print()
        display_daily_averages(data)
        display_top_spikes(data, args.top)
        display_anomalies(data)

    except argparse.ArgumentError as exc:
        print(f"Command line error: {exc}")
    except (FileNotFoundError, TypeError, ValueError, ValidationError) as exc:
        print(f"Validation error: {exc}")
    except Exception as exc:  # pylint: disable=broad-exception-caught
        print(f"An unexpected error occurred: {exc}")


if __name__ == "__main__":
    main()
