#!/usr/bin/env python3
"""
Professional CLI Tool for ETL Pipeline (Refactored from Day 2 monolithic script).
Supports subcommands: validate, transform, load, report.
"""

import argparse
import json
import logging
import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

try:
    from week4day2.database_practice import setup_database
    from week4day2.validators import DataValidator
except ImportError:
    # Fallback mocks so script can be tested independently if modules are missing
    class DataValidator:
        def __init__(self):
            self.errors = []

        def validate_task_csv(self, path):
            return [
                {
                    "title": "Setup Django",
                    "description": "Initial config",
                    "status": "done",
                    "categories": ["Python", "Backend"],
                    "due_date": "2026-08-01",
                },
                {
                    "title": "Database Models",
                    "description": "Write ORM classes",
                    "status": "in_progress",
                    "categories": ["Django", "SQL"],
                    "due_date": "2026-08-05",
                },
            ]

    def setup_database(db_name):
        with sqlite3.connect(db_name) as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS categories (id INTEGER PRIMARY KEY, name TEXT UNIQUE);"
            )
            conn.execute(
                "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT, description TEXT, status TEXT, category_count INTEGER, is_overdue INTEGER);"
            )
            conn.execute(
                "CREATE TABLE IF NOT EXISTS tasks_categories (task_id INTEGER, category_id INTEGER, PRIMARY KEY(task_id, category_id));"
            )


# LOGGING CONFIGURATION


def setup_logging(verbosity: int) -> logging.Logger:
    """
    Configures structured logging levels based on --verbose flags:
    verbosity 0 (default) -> WARNING (30)
    verbosity 1 (-v)      -> INFO (20)
    verbosity 2+ (-vv)    -> DEBUG (10)
    """
    level_mapping = {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG}
    log_level = level_mapping.get(verbosity, logging.DEBUG)

    log_format = "[%(asctime)s] [%(levelname)-8s] [%(name)s]: %(message)s"

    logging.basicConfig(
        level=log_level,
        format=log_format,
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True,  # Overrides any existing logger configs
    )
    return logging.getLogger("ETL_CLI")


# 1. CUSTOM ARGPARSE VALIDATORS


def validate_file_exists(filepath: str) -> str:
    """Ensures input file exists before running pipeline logic."""
    if not os.path.exists(filepath):
        raise argparse.ArgumentTypeError(f"File not found: '{filepath}'")
    if not os.path.isfile(filepath):
        raise argparse.ArgumentTypeError(f"Not a regular file: '{filepath}'")
    return filepath


# 2. SUBCOMMAND HANDLERS


def run_validate(
    args: argparse.Namespace, config: Dict[str, Any], logger: logging.Logger
) -> int:
    """Subcommand: pipeline validate <file>"""
    logger.info("Starting schema validation for input: %s", args.file)

    validator = DataValidator()
    clean_data = validator.validate_task_csv(args.file)

    if validator.errors:
        logger.warning(
            "Validation completed with %d schema errors", len(validator.errors)
        )
        for err in validator.errors:
            logger.warning(
                "Row %s | Field '%s': %s",
                err.get("row"),
                err.get("field"),
                err.get("error"),
            )
        if args.strict:
            logger.error("Strict mode enabled: Aborting pipeline due to schema errors.")
            return 1

    logger.info("Successfully extracted %d valid records.", len(clean_data))
    return 0


def run_transform(
    args: argparse.Namespace, config: Dict[str, Any], logger: logging.Logger
) -> int:
    """Subcommand: pipeline transform <file>"""
    logger.info("Validating and transforming dataset: %s", args.file)
    validator = DataValidator()
    clean_data = validator.validate_task_csv(args.file)

    if not clean_data:
        logger.error("No valid data extracted. Transformation aborted.")
        return 1

    logger.debug(
        "Enriching records with derived fields (category_count, is_overdue)..."
    )
    for task in clean_data:
        # Business rules from your Day 2 script
        task["category_count"] = len(task["categories"])
        task["is_overdue"] = False
        if task.get("due_date"):
            try:
                due = datetime.strptime(task["due_date"], "%Y-%m-%d")
                if due < datetime.now():
                    task["is_overdue"] = True
            except ValueError:
                logger.debug(
                    "Invalid date format for due_date: %s", task.get("due_date")
                )

    output_dir = Path(config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / "transformed_tasks.json"

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(clean_data, f, indent=4)

    logger.info(
        "Transformation complete. Wrote %d records to %s", len(clean_data), out_file
    )
    return 0


def run_load(
    args: argparse.Namespace, config: Dict[str, Any], logger: logging.Logger
) -> int:
    """Subcommand: pipeline load <file> --db <name>"""
    logger.info("Starting load subcommand for file: %s", args.file)

    # Run validation and transformation first
    validator = DataValidator()
    clean_data = validator.validate_task_csv(args.file)
    if not clean_data:
        logger.error("No valid records available to load. Aborting.")
        return 1

    # Apply transformations before loading
    for task in clean_data:
        task["category_count"] = len(task["categories"])
        task["is_overdue"] = False
        if task.get("due_date"):
            try:
                due = datetime.strptime(task["due_date"], "%Y-%m-%d")
                if due < datetime.now():
                    task["is_overdue"] = True
            except ValueError:
                pass

    db_name = args.db if args.db else config["db_name"]
    logger.info("Initializing SQLite destination: %s", db_name)
    setup_database(db_name)

    output_dir = Path(config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "validated_tasks.json"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(clean_data, f, indent=4)
    logger.debug("Saved JSON copy to %s", json_path)

    try:
        with sqlite3.connect(db_name) as conn:
            conn.execute("PRAGMA foreign_keys = ON")
            cursor = conn.cursor()

            for task in clean_data:
                cursor.execute(
                    """
                    INSERT INTO tasks (title, description, status, category_count, is_overdue) 
                    VALUES (?, ?, ?, ?, ?)
                """,
                    (
                        task["title"],
                        task["description"],
                        task["status"],
                        task["category_count"],
                        int(task["is_overdue"]),
                    ),
                )

                task_id = cursor.lastrowid

                for cat_name in task["categories"]:
                    cursor.execute(
                        "INSERT OR IGNORE INTO categories (name) VALUES (?)",
                        (cat_name,),
                    )
                    cursor.execute(
                        "SELECT id FROM categories WHERE name = ?", (cat_name,)
                    )
                    cat_id = cursor.fetchone()[0]
                    cursor.execute(
                        """
                        INSERT INTO tasks_categories (task_id, category_id) 
                        VALUES (?, ?)
                    """,
                        (task_id, cat_id),
                    )

        logger.info(
            "Successfully loaded data into SQLite database without constraint violations."
        )
        return 0
    except Exception as exc:
        logger.critical(
            "CRITICAL ERROR during LOAD: %s", exc, exc_info=args.verbose >= 2
        )
        logger.critical(
            "Entire database transaction has been automatically rolled back."
        )
        return 1


def run_report(
    args: argparse.Namespace, config: Dict[str, Any], logger: logging.Logger
) -> int:
    """Subcommand: pipeline report --db <name>"""
    db_name = args.db if args.db else config["db_name"]
    if not os.path.exists(db_name):
        logger.error("Database file '%s' does not exist. Run 'load' first.", db_name)
        return 1

    logger.info("Generating ETL execution summary from SQLite: %s", db_name)
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM tasks;")
            total_tasks = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM categories;")
            total_cats = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM tasks WHERE is_overdue = 1;")
            overdue_tasks = cursor.fetchone()[0]

            print("\n======================= ETL REPORT =======================")
            print(f"Database Source:      {db_name}")
            print(f"Total Tasks Loaded:   {total_tasks}")
            print(f"Total Categories:     {total_cats}")
            print(f"Overdue Tasks:        {overdue_tasks}")
            print("==========================================================\n")
        return 0
    except Exception as exc:
        logger.error("Failed to generate report: %s", exc)
        return 1


# 3. CLI PARSER BUILDER


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Professional ETL Pipeline CLI (Extractor, Transformer, Loader).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Top-Level / Global Flags
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        help="Path to JSON configuration file.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase log verbosity (-v for INFO, -vv for DEBUG).",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Override global output directory path.",
    )

    # Subcommands
    subparsers = parser.add_subparsers(
        dest="command",
        title="Available Subcommands",
        required=True,
        metavar="<command>",
    )

    # --- Subcommand: validate ---
    val_parser = subparsers.add_parser("validate", help="Validate CSV dataset schema.")
    val_parser.add_argument(
        "file", type=validate_file_exists, help="Path to input CSV file."
    )
    val_parser.add_argument(
        "--strict", action="store_true", help="Abort pipeline on schema warnings."
    )
    val_parser.set_defaults(func=run_validate)

    # --- Subcommand: transform ---
    trans_parser = subparsers.add_parser(
        "transform", help="Enrich dataset with derived fields."
    )
    trans_parser.add_argument(
        "file", type=validate_file_exists, help="Path to input CSV file."
    )
    trans_parser.set_defaults(func=run_transform)

    # --- Subcommand: load ---
    load_parser = subparsers.add_parser(
        "load", help="Load transformed data into SQLite."
    )
    load_parser.add_argument(
        "file", type=validate_file_exists, help="Path to input CSV file."
    )
    load_parser.add_argument(
        "--db", type=str, help="Target SQLite database filename override."
    )
    load_parser.set_defaults(func=run_load)

    # --- Subcommand: report ---
    rep_parser = subparsers.add_parser(
        "report", help="Generate statistics report from DB."
    )
    rep_parser.add_argument(
        "--db", type=str, help="Target SQLite database filename to report on."
    )
    rep_parser.set_defaults(func=run_report)

    return parser


# 4. ENTRY POINT


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    # Setup Logging & Configuration Hierarchy
    logger = setup_logging(args.verbose)

    # Precedence: CLI > ENV > CONFIG > DEFAULTS
    config = {
        "db_name": "etl_target.db",
        "output_dir": "./output",
    }
    if args.config and os.path.exists(args.config):
        with open(args.config, "r", encoding="utf-8") as f:
            config.update(json.load(f))
    if "ETL_DB_NAME" in os.environ:
        config["db_name"] = os.environ["ETL_DB_NAME"]
    if args.output:
        config["output_dir"] = args.output

    try:
        exit_code: int = args.func(args, config, logger)
        return exit_code
    except Exception as exc:
        logger.critical(
            "Fatal unhandled pipeline exception: %s", exc, exc_info=args.verbose >= 2
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
