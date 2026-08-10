
#!/usr/bin/env python3
"""
Demonstration of Graceful Error Handling and Exit Codes.
"""

import argparse
import logging
import sys


def run_dummy_task(args: argparse.Namespace) -> int:
    """Simulates opening a file to test our error handling."""
    # This will trigger FileNotFoundError if the file doesn't exist on disk!
    with open(args.file, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"Successfully read {len(content)} characters from {args.file}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Creates a simple parser to test error handling."""
    parser = argparse.ArgumentParser(description="Error Handling Demo CLI")
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print full traceback on error instead of short message.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: test
    test_parser = subparsers.add_parser("test", help="Test file reading error handling")
    test_parser.add_argument("file", help="Path to a file to read")
    test_parser.set_defaults(func=run_dummy_task)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        # Run the subcommand
        return args.func(args)

    except FileNotFoundError as exc:
        # Clean, user-friendly error message — no scary red stack trace!
        print(f"Error: Could not find file -> {exc.filename}", file=sys.stderr)
        return 1

    except Exception as exc:
        # Catch any unexpected crashes
        if args.verbose:
            # If user passed -v, show them the full developer traceback
            logging.exception("Fatal pipeline exception occurred:")
        else:
            # Normal users just get a neat 1-line error sentence
            print(
                f"Fatal Error: {exc}. (Run with -v for full stack trace)",
                file=sys.stderr,
            )
        return 1


if __name__ == "__main__":
    sys.exit(main())