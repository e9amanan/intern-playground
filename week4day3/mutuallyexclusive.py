import argparse

parser = argparse.ArgumentParser(description="ETL Tool with Mutually Exclusive Flags")


log_group = parser.add_mutually_exclusive_group(required=False)


log_group.add_argument(
    "-v", "--verbose",
    action="store_true",
    help="Enable detailed debug logging."
)

log_group.add_argument(
    "-q", "--quiet",
    action="store_true",
    help="Suppress all standard console output."
)

args = parser.parse_args()