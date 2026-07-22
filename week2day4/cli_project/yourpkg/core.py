"""
Core algorithmic business logic for time-series data analysis.
Handles data cleaning, aggregation, spike detection, and anomaly detection.
"""

from collections import defaultdict
from datetime import datetime
from statistics import mean, stdev

from .exceptions import ValidationError


def clean_data(raw_rows: list[dict], metric: str) -> list[dict]:
    """
    Parse timestamps and extract the specified metric from raw rows.

    Args:
        raw_rows (list[dict]): The raw data rows from the CSV.
        metric (str): The column name to extract as the value.

    Returns:
        list[dict]: A list of cleaned data dictionaries.

    Raises:
        ValidationError: If no valid data rows are found in the dataset.
    """
    data = []
    for line_num, row in enumerate(raw_rows, start=2):
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


def display_daily_averages(data: list[dict]) -> None:
    """
    Calculate and print the daily average for the metric.

    Args:
        data (list[dict]): The cleaned data containing timestamps and values.
    """
    daily_totals = defaultdict(list)
    for row in data:
        day_str = row["timestamp"].strftime("%y-%m-%d")
        daily_totals[day_str].append(row["value"])

    print("Daily averages:")

    # FIXED: Moved the colon outside the string so f-string alignment actually works
    print(f"{'Date':<12} {'Avg Price'}")

    for day, values in sorted(daily_totals.items()):
        avg = mean(values)
        print(f"{day:<12} ${avg:.2f}")
    print()


def display_top_spikes(data: list[dict], top_n: int) -> None:
    """
    Find and print the highest values (spikes) in the data.

    Args:
        data (list[dict]): The cleaned data containing timestamps and values.
        top_n (int): The number of top spikes to display.
    """
    sorted_data = sorted(data, key=lambda x: x["value"], reverse=True)
    spikes = sorted_data[:top_n]

    print(f"Top {top_n} price spikes:")
    for spike in spikes:
        print(f"{spike['raw_ts']:<21} ${spike['value']:.2f}")
    print()


def display_anomalies(data: list[dict]) -> None:
    """
    Detect and print the number of anomalies using a z-score threshold > 2.

    Args:
        data (list[dict]): The cleaned data containing timestamps and values.
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
