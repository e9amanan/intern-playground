import argparse
import sys


def run_validate(args):
    print(f"Validating file: {args.file} (Strict mode: {args.strict})")
    return 0


def run_transform(args):
    print(f"Transforming file: {args.file} with batch size {args.batch_size}")
    return 0


def run_load(args):
    print(f"Loading {args.file} into table: {args.table}")
    return 0


def main():

    parser = argparse.ArgumentParser(description="ETL Pipeline CLI Tool")

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable debug logs"
    )

    # Create the Subparser Co
    subparsers = parser.add_subparsers(
        dest="command",  # Stores which word the user typed ('validate', 'load', etc.)
        required=True,
        title="Subcommands",
    )

    #  validate
    val_parser = subparsers.add_parser("validate", help="Check dataset schema")
    val_parser.add_argument("file", help="CSV file to validate")
    val_parser.add_argument(
        "--strict", action="store_true", help="Fail on minor warnings"
    )
    val_parser.set_defaults(func=run_validate)

    # transform
    trans_parser = subparsers.add_parser("transform", help="Clean and transform data")
    trans_parser.add_argument("file", help="CSV file to transform")
    trans_parser.add_argument(
        "--batch-size", type=int, default=100, help="Rows per batch"
    )
    trans_parser.set_defaults(func=run_transform)

    # load
    load_parser = subparsers.add_parser("load", help="Load data into database")
    load_parser.add_argument("file", help="CSV file to load")
    load_parser.add_argument("--table", required=True, help="Target DB table name")
    load_parser.set_defaults(func=run_load)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
