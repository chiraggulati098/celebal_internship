## Data Lake File Processing and Loading Pipeline

This project automates the daily ingestion and transformation of three types of files from a data lake container into their respective database tables. The process is designed for truncate load operations and handles multiple files per type, differentiated by date in the filename.

### File Types and Processing Logic

1. **CUST_MSTR Files**
   - **Pattern:** `CUST_MSTR_YYYYMMDD.csv` (e.g., `CUST_MSTR_20191112.csv`, `CUST_MSTR_20191113.csv`)
   - **Processing:**
     - Extract the date from the filename.
     - Add a new column `Date` to each row, formatted as `YYYY-MM-DD` (e.g., `2019-11-12`).
     - Load the transformed data into the `CUST_MSTR` table.

2. **master_child_export Files**
   - **Pattern:** `master_child_export-YYYYMMDD.csv` (e.g., `master_child_export-20191112.csv`)
   - **Processing:**
     - Extract the date from the filename.
     - Add two new columns:
       - `Date` (formatted as `YYYY-MM-DD`, e.g., `2019-11-12`)
       - `DateKey` (formatted as `YYYYMMDD`, e.g., `20191112`)
     - Load the transformed data into the `master_child` table.

3. **H_ECOM_ORDER Files**
   - **Pattern:** `H_ECOM_ORDER.csv`
   - **Processing:**
     - Load the file as-is into the `H_ECOM_Orders` table (no transformation required).

### Daily Truncate Load
Each day, all files matching the above patterns are processed and loaded into their respective tables. The tables are truncated before loading to ensure only the latest data is present.

### Folder Structure
- All files are stored in the data lake container and fetched into their respective folders for processing.
- Screenshots and pipeline diagrams are available in the `images/` directory for reference.

### Screenshots
See the `images/` folder for UI previews, pipeline diagrams, and sample results:
- `adf-new-pipeline.png`: New pipeline setup
- `blob-uploaded-files.png`: Uploaded files in blob storage
- `data-flow.png`: Data flow diagram
- `dataset-cust-mstr.png`, `dataset-h-ecom-order.png`, `dataset-master-child.png`: Dataset configurations
- `final-pipeline.png`: Final pipeline overview
- `linked-service-datalake.png`, `linked-service-sql.png`: Linked service configurations

---
**Note:** This pipeline is designed for daily truncate loads. Ensure all files are present in the data lake before execution.
