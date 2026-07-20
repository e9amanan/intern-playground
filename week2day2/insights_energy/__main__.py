"""
Module providing the command-line interface for analyzing hourly energy price data.
"""

import argparse

from .io_utils import read_csv, write_json, write_csv
from .core import clean_data, display_daily_averages, display_top_spikes, display_anomalies
from .exceptions import FileProcessingError, ValidationError


def parse_arguments() -> argparse.Namespace:
    """Parse and return command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Analyze hourly energy price data",
        exit_on_error=False
    )
    parser.add_argument("--file", required=True, help="CSV file path (required)")
    parser.add_argument(
        "--metric", 
        default="price", 
        help="Column name to analyze (default: 'price')"
    )
    parser.add_argument(
        "--top", 
        type=int, 
        default=10, 
        help="Number of spikes to show (default: 10)"
    )
    parser.add_argument(
        "--export", 
        choices=['json', 'csv'], 
        help="Export cleaned data to json or csv"
    )

    return parser.parse_args()


def validate_top_argument(top_n: int) -> None:
    """Validate that the 'top' argument is a positive integer."""
    if not isinstance(top_n, int):
        raise TypeError(f"The 'top' argument must be an integer. Got: {type(top_n).__name__}")
    if top_n <= 0:
        raise ValueError(f"The 'top' argument must be a positive integer. Got: {top_n}")


def main() -> None:
    """Main entry point for the CLI application."""
    try:
        args = parse_arguments()
        validate_top_argument(args.top)

        raw_rows = read_csv(args.file, required_column=args.metric)
        data = clean_data(raw_rows, args.metric)

        print()
        display_daily_averages(data)
        display_top_spikes(data, args.top)
        display_anomalies(data)

        if args.export:
            export_data = [{"timestamp": r["raw_ts"], "value": r["value"]} for r in data]

            if args.export == 'json':
                out_file = "cleaned_data.json"
                write_json(out_file, export_data)
                print(f"Data successfully exported to {out_file}")

            elif args.export == 'csv':
                out_file = "cleaned_data.csv"
                write_csv(out_file, export_data, fieldnames=["timestamp", "value"])
                print(f"Data successfully exported to {out_file}")

    except argparse.ArgumentError as e:
        print(f"Command line error: {e}")
        return
    except FileProcessingError as e:
        print(f"File system error: {e}")
        return
    except (TypeError, ValueError, ValidationError) as e:
        print(f"Validation error: {e}")
        return
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")
        return


if __name__ == "__main__":
    main()