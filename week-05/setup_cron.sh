#!/bin/bash

# setup_cron.sh
# -------------------------------
# This script shows how to set up a cron job that runs the data pipeline
# every 12 hours using crontab.
# -------------------------------

# === CONFIGURATION ===
# Change these paths as per your environment

PYTHON_PATH="/Users/chigi/Developer/celebal_internship/venv/bin/python"
SCRIPT_PATH="/Users/chigi/Developer/celebal_internship/week-05/data_pipeline.py"

# === CRON EXPRESSION ===
# Runs at 00:00 and 12:00 every day
CRON_EXPRESSION="0 */12 * * *"

# === FINAL CRON JOB LINE ===
CRON_JOB="$CRON_EXPRESSION $PYTHON_PATH $SCRIPT_PATH >> $LOG_PATH 2>&1"

# === DISPLAY INSTRUCTIONS ===

echo "🔁 Add the following line to your crontab using 'crontab -e':"
echo ""
echo "$CRON_JOB"
echo ""
echo "✅ This will run your data pipeline every 12 hours (00:00 and 12:00)."
echo ""
echo "📌 Make sure the script has executable permissions and correct Python path."

# Optional: Ask user to copy it automatically
read -p "👉 Do you want to auto-add this to your crontab now? (y/n): " confirm

if [ "$confirm" = "y" ]; then
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    echo "✅ Cron job added."
else
    echo "❗ Skipped adding to crontab. You can do it manually using: crontab -e"
fi
