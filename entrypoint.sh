#!/bin/sh
set -e

# Ensure working dir
cd /app

echo "Running DB initialization (SQLite)..."
# Run the init script to create tables if they do not exist
python -m database.__init__db || true

# Exec the main process (passed as CMD)
exec "$@"
