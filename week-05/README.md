# Week-05 Data Pipeline Project

## Overview
This project demonstrates a robust data pipeline that automates the extraction, transformation, and loading (ETL) of data between relational databases and multiple file formats. It also showcases automation using both scheduled and event-based triggers.
## Project Structure

- `data_pipeline.py`: Core logic for extracting data from a source database and exporting it to CSV, Parquet, and Avro formats. Also handles copying data between databases (full and selective replication).
- `event_trigger.py`: Implements event-based triggers to automate pipeline execution in response to dynamic events (e.g., file arrival, database changes).
- `setup_cron.sh`: Shell script to configure schedule-based triggers (cron jobs) for regular, automated pipeline runs.
- `outputs/`: Directory containing sample output files in different formats:
    - `film.csv`: Data exported in CSV format.
    - `film.parquet`: Data exported in Parquet format.
    - `film.avro`: Data exported in Avro format.

## Features

### 1. Copy Data from Database to CSV, Parquet, and Avro
- Extracts data from a relational database.
- Exports data to:
  - **CSV**: For broad compatibility and easy sharing.
  - **Parquet**: For efficient analytics and columnar storage.
  - **Avro**: For schema evolution and compact serialization.
- Supports downstream use cases like reporting, warehousing, and distributed processing.

### 2. Automate Pipeline with Schedule and Event Triggers
- **Schedule-based triggers**: Use `setup_cron.sh` to run the pipeline at regular intervals (e.g., daily, hourly).
- **Event-based triggers**: Use `event_trigger.py` to execute the pipeline in response to specific events (e.g., new file arrival, database update).
- Ensures timely and automated data movement for both batch and real-time scenarios.

### 3. Copy All Tables from One Database to Another
- Dynamically identifies all tables in the source database.
- Copies both schema and data to the destination database.
- Useful for full database replication, backup, migration, or environment synchronization.

### 4. Copy Selective Tables and Columns
- Allows selection of specific tables and columns for transfer.
- Supports compliance, reduces data volume, and enables targeted data migration.

## Usage

1. **Configure Database Connections**: Update connection details in `data_pipeline.py` as needed.
2. **Run the Pipeline Manually**:
   ```bash
   python data_pipeline.py
   ```
3. **Set Up Scheduled Runs**:
   - Edit and run `setup_cron.sh` to schedule regular pipeline execution.
4. **Enable Event Triggers**:
   - Use `event_trigger.py` to listen for and respond to relevant events.
5. **Check Outputs**:
   - Exported files will appear in the `outputs/` directory.

## Requirements
- Python 3.12
- Required libraries: `pandas`, `pyarrow`, `fastavro`, `sqlalchemy`

## Example Output
- `outputs/film.csv`: CSV export
- `outputs/film.parquet`: Parquet export
- `outputs/film.avro`: Avro export
