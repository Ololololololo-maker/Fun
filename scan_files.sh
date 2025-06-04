#!/bin/bash

# Script: scan_files.sh
# Description: Scan directories for files matching a pattern.
# Usage: ./scan_files.sh [directory] [pattern]
# Example: ./scan_files.sh /var log

# Set defaults if no arguments supplied
SEARCH_DIR="${1:-.}"
PATTERN="${2:-*}"

if [ ! -d "$SEARCH_DIR" ]; then
    echo "Error: '$SEARCH_DIR' is not a valid directory" >&2
    exit 1
fi

# Use find to locate files matching the pattern
find "$SEARCH_DIR" -type f -name "$PATTERN"
