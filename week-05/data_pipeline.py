"""
data_pipeline.py

A single-file pipeline to:
- Export data from local PostgreSQL to CSV, Parquet, and Avro
- Copy all tables between databases
- Copy selective tables/columns
"""

import os
import pandas as pd
from sqlalchemy import create_engine
from fastavro import writer, parse_schema
from datetime import datetime

# CONFIGURATION
SOURCE_DB = "postgresql://postgres:password@localhost:5432/dvdrental"
DEST_DB   = "postgresql://postgres:password@localhost:5432/dvdrental_copy"
EXPORT_TABLE = "film"  
OUTPUT_DIR = "outputs"
SELECTIVE_TABLES = {
    "customer": ["customer_id", "first_name", "last_name", "email"],
    "rental": ["rental_id", "rental_date", "inventory_id", "customer_id"]
}

# Setup output directory
os.makedirs(OUTPUT_DIR, exist_ok=True)

def connect_to_db(uri):
    return create_engine(uri)

def export_to_file_formats(df, name):
    df.to_csv(f"{OUTPUT_DIR}/{name}.csv", index=False)
    df.to_parquet(f"{OUTPUT_DIR}/{name}.parquet", index=False)
    
    schema = {
        "type": "record",
        "name": f"{name}_record",
        "fields": [{"name": col, "type": "string"} for col in df.columns]
    }
    parsed_schema = parse_schema(schema)
    with open(f"{OUTPUT_DIR}/{name}.avro", "wb") as out:
        writer(out, parsed_schema, df.astype(str).to_dict("records"))
    print(f"Exported '{name}' to CSV, Parquet, and Avro.")

def copy_all_tables(src_engine, dest_engine):
    tables = pd.read_sql("""
        SELECT table_name FROM information_schema.tables 
        WHERE table_schema = 'public' AND table_type='BASE TABLE'
    """, src_engine)

    for table in tables["table_name"]:
        df = pd.read_sql(f"SELECT * FROM {table}", src_engine)
        df.to_sql(table, dest_engine, if_exists="replace", index=False)
        print(f"Copied table: {table}")

def copy_selective_tables(src_engine, dest_engine):
    for table, cols in SELECTIVE_TABLES.items():
        col_str = ", ".join(cols)
        df = pd.read_sql(f"SELECT {col_str} FROM {table}", src_engine)
        df.to_sql(table, dest_engine, if_exists="replace", index=False)
        print(f"Copied selective columns from table: {table}")

def main():
    print("Starting Data Pipeline...\n")
    
    src_engine = connect_to_db(SOURCE_DB)
    dest_engine = connect_to_db(DEST_DB)

    df = pd.read_sql(f"SELECT * FROM {EXPORT_TABLE}", src_engine)
    export_to_file_formats(df, EXPORT_TABLE)
    copy_all_tables(src_engine, dest_engine)
    copy_selective_tables(src_engine, dest_engine)

    print("\n----- Pipeline completed -----")

if __name__ == "__main__":
    main()
