# Customer Data Pipeline: ADLS Gen2 & Databricks Delta Tables

This project demonstrates how to load random customer data into Azure Data Lake Storage Gen2 (ADLS Gen2), connect it with Azure Databricks, and create managed Delta tables using various file formats. The workflow includes data validation and code optimization for scalable data engineering.

## Steps Overview

### Step 1: Load Sample Customers Data into ADLS Gen2
- Use the sample customer data files provided in the `data/` directory (`CSV`, `TSV`, `JSON`, `XML`, `XLSX`, `TXT`).
- Upload these files to your ADLS Gen2 storage account using Azure Portal, Azure Storage Explorer, or CLI.

### Step 2: Connect ADLS Gen2 with Databricks
- Configure Databricks to access your ADLS Gen2 account using service principal or account key.
- Mount the ADLS Gen2 container in Databricks for seamless data access.

### Step 3: Create Managed Delta Table and Load Data
- In Databricks, create a **managed Delta table** (not external) for customer data.
- Load data from ADLS Gen2 into the Delta table.

### Step 4: Use CTAS for AVRO, PARQUET, ORC & DELTA
- For file formats: **AVRO, PARQUET, ORC, DELTA**
    - Use **CTAS (CREATE TABLE AS SELECT)** to load data directly into Delta tables.
    - Example:
      ```sql
      CREATE TABLE customers_avro_delta
      USING DELTA
      AS SELECT * FROM parquet.'<adls_path>/customers_data.avro';
      ```

### Step 5: Temporary View for CSV, TSV, JSON, XML, XLSX, TXT
- For file formats: **CSV, TSV, JSON, XML, XLSX, TXT**
    1. **Create a Temporary View** in Databricks with the customer data schema.
    2. Load the data into the view.
    3. Use CTAS to create a Delta table from the Temporary View.
    - Example:
      ```python
      df = spark.read.format('csv').option('header', 'true').load('<adls_path>/customers_data.csv')
      df.createOrReplaceTempView('customers_csv_view')
      spark.sql('CREATE TABLE customers_csv_delta USING DELTA AS SELECT * FROM customers_csv_view')
      ```

## Data Validation
- After creating each Delta table, **validate** that it contains exactly **500 rows**.
- Implement a **generic validation function** to check row counts for all Delta tables:
  ```python
  def validate_delta_table_row_count(table_name, expected_count=500):
      count = spark.sql(f'SELECT COUNT(*) FROM {table_name}').collect()[0][0]
      assert count == expected_count, f"Table {table_name} has {count} rows, expected {expected_count}"
  ```

## Directory Structure
- `data/` : Sample customer data in various formats
- `Connect to ADLS Gen2.ipynb` : Example notebook for connecting to ADLS Gen2
- `*.png` : Screenshots and output samples
- `README.md` : This documentation

## Notes
- Use managed Delta tables (not external) for all data loads.
- Use CTAS for AVRO, PARQUET, ORC, DELTA; use Temporary Views for CSV, TSV, JSON, XML, XLSX, TXT.
- Validate row counts for data quality.
- Optimize code by using generic functions for validation and loading.

---

For detailed code samples, refer to the notebooks and scripts in this directory.
