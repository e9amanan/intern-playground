"""
Create backup script

    Create scripts/backup_logs.sh that:
        Archives a given directory to ./archives/<name>-YYYY-MM-DD.tar.gz.
        Keeps only the last N archives (argument), deletes older ones.
        Prints a summary of created and deleted archives.
    Make executable: chmod +x scripts/backup_logs.sh.
    Use sample logs directory: intern_training/data/sample_logs/.

"""
#!/usr/bin/env bash
set -euo pipefail

# 1. Argument validation
if [[ $# -ne 2 ]]; then
    echo "Error: expected 2 arguments, got $#" >&2
    echo "Usage: $0 <source_dir> <archive_name>" >&2
    exit 1
fi

TARGET_DIR="$1"
ARCHIVE_NAME_PREFIX="$2"
ARCHIVE_BASE_DIR="./archives"

if [[ ! -d "$TARGET_DIR" ]]; then
    echo "Error: source directory '$TARGET_DIR' does not exist" >&2
    exit 1
fi


# 2. Ensure the archives directory exists
mkdir -p "$ARCHIVE_BASE_DIR"

# 3. Create the backup file name with today's date
TIMESTAMP=$(date +"%F")
ARCHIVE_NAME="${ARCHIVE_NAME_PREFIX}-${TIMESTAMP}.tar.gz"
DEST_ARCHIVE_PATH="${ARCHIVE_BASE_DIR}/${ARCHIVE_NAME}"

# Guard against overwriting a backup made earlier today
if [[ -e "$DEST_ARCHIVE_PATH" ]]; then
    echo "Error: archive '$DEST_ARCHIVE_PATH' already exists" >&2
    exit 1
fi

# 4. Create the compressed tar archive file
PARENT_DIR="$(dirname "$TARGET_DIR")"
LEAF_DIR="$(basename "$TARGET_DIR")"

if ! tar -czf "$DEST_ARCHIVE_PATH" -C "$PARENT_DIR" "$LEAF_DIR"; then
    echo "Error: failed to create archive" >&2
    rm -f "$DEST_ARCHIVE_PATH"
    exit 1
fi

# --- SUMMARY BLOCK ---
echo "========================================="
echo "         BACKUP PROCESS SUMMARY          "
echo "========================================="
echo "Target Directory : $TARGET_DIR"
echo "Created Archive  : ${ARCHIVE_NAME}"
echo "Saved To Path    : ${DEST_ARCHIVE_PATH}"
echo "========================================="