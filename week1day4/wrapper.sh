#!/usr/bin/env bash
set -euo pipefail
usage(){
    echo "Usage: $0 [-h|--help] <input_csv>"
    exit 0
}
if[["${1:-}" == "-h" || "${1:-}" == "--help"]]; then
    usage
fi

if[[-z "${1:-}" ]];then
    echo "error:missing required argument." >&2
    usage
fi

python -m energy_insights "$1"

