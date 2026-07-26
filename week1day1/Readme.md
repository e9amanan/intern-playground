# Backup Script

A simple script to create daily, compressed (.tar.gz) archives of a folder.

## Usage
./backup_logs.sh <source_dir> <archive_prefix> <retain_count>

* source_dir:     The folder to back up.
* archive_prefix: The name prefix (e.g., 'my-app').
* retain_count:   Placeholder for rotation logic (must be an integer >= 1).

## Example
./backup_logs.sh ./data project-backup 5

Saves to: `./archives/project-backup-YYYY-MM-DD.tar.gz`

## Features
* **Safe:** Won't overwrite existing backups from the same day.
* **Robust:** Automatically cleans up partial files if the backup fails.