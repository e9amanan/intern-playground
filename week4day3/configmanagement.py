import argparse
import json
import os
from typing import Any, Dict


def resolve_configuration(cli_args: argparse.Namespace) -> Dict[str, Any]:
    # 4. Hardcoded Defaults
    config: Dict[str, Any] = {
        "db_name": "etl_target.db",
        "output_dir": "./output",
        "batch_size": 100,
    }

    # 3. Config File (JSON)
    if cli_args.config and os.path.exists(cli_args.config):
        with open(cli_args.config, "r", encoding="utf-8") as f:
            file_config = json.load(f)
            config.update(file_config)  # Overrides defaults

    # 2. Environment Variables
    if "ETL_DB_NAME" in os.environ:
        config["db_name"] = os.environ["ETL_DB_NAME"]
    if "ETL_OUTPUT_DIR" in os.environ:
        config["output_dir"] = os.environ["ETL_OUTPUT_DIR"]

    # 1. CLI Flags (Highest Precedence)
    if getattr(cli_args, "output", None):
        config["output_dir"] = cli_args.output

    return config
