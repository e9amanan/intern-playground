"""
Command Line Interface for the energy_insights package.
Provides subcommands to summarize data, find spikes, and detect anomalies.
"""

import argparse
from pathlib import Path

from energy_insights.core import EnergySeries
from energy_insights.exceptions import DataLoadError, ValidationError
from energy_insights.io_utils import load_data
from week2weekend.energy_insights.core import EnergySeries
from week2weekend.energy_insights.exceptions import DataLoadError, ValidationError
from week2weekend.energy_insights.io_utils import load_data


def _get_series(args: argparse.Namespace) -> EnergySeries:
    """
    Helper function to load data and initialize an EnergySeries object.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.

    Returns:
        EnergySeries: An initialized EnergySeries object.
    """
    raw_data = load_data(Path(args.file))
    return EnergySeries(raw_data, args.metric)


def handle_summary(args: argparse.Namespace) -> int:
    """
    Handle the 'summary' subcommand.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.

    Returns:
        int: Exit status code (0 for success).
    """
    try:
        series = _get_series(args)
        stats = series.summary()
        print(f"Row count: {stats['count']}")
        print(f"Min: {stats['min']:.2f}")
        print(f"Max: {stats['max']:.2f}")
        print(f"Mean: {stats['mean']:.2f}")
        return 0
    except (DataLoadError, ValidationError) as exc:
        # Pylint requires 'from exc' when raising a new exception inside an except block
        raise SystemExit(f"Error: {exc}") from exc


def handle_spikes(args: argparse.Namespace) -> int:
    """
    Handle the 'spikes' subcommand.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.

    Returns:
        int: Exit status code (0 for success).
    """
    try:
        series = _get_series(args)
        spikes = series.top_spikes(args.top)
        print(f"Top {args.top} price spikes:")
        for spike in spikes:
            print(f"  {spike['raw_ts']:<21} ${spike['value']:.2f}")
        return 0
    except (DataLoadError, ValidationError) as exc:
        raise SystemExit(f"Error: {exc}") from exc


def handle_anomalies(args: argparse.Namespace) -> int:
    """
    Handle the 'anomalies' subcommand.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.

    Returns:
        int: Exit status code (0 for success).
    """
    try:
        series = _get_series(args)
        anomalies = series.anomalies()
        print(f"Anomalies detected: {len(anomalies)} hour(s) (z-score > 2 threshold)")
        return 0
    except (DataLoadError, ValidationError) as exc:
        raise SystemExit(f"Error: {exc}") from exc


def main(argv: list[str] | None = None) -> int:
    """
    Main entry point for the CLI.

    Args:
        argv (list[str] | None, optional): List of command-line arguments. Defaults to None.

    Returns:
        int: Exit status code.
    """
    parser = argparse.ArgumentParser(
        prog="energy_insights", description="CLI tool for hourly energy price analysis."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "--file", required=True, help="Path to CSV/JSON data file."
    )
    parent_parser.add_argument(
        "--metric", required=True, help="Column name to analyze."
    )

    summary_p = subparsers.add_parser(
        "summary", parents=[parent_parser], help="View dataset stats."
    )
    summary_p.set_defaults(func=handle_summary)

    spikes_p = subparsers.add_parser(
        "spikes", parents=[parent_parser], help="View highest values."
    )
    spikes_p.add_argument(
        "--top", type=int, default=5, help="Number of spikes (default: 5)."
    )
    spikes_p.set_defaults(func=handle_spikes)

    anomalies_p = subparsers.add_parser(
        "anomalies", parents=[parent_parser], help="Detect outliers."
    )
    anomalies_p.set_defaults(func=handle_anomalies)

    args = parser.parse_args(argv)
    return args.func(args)
