
# 🧩 ETL Pipeline: Excel to MySQL & PostgreSQL

## 📌 Project Overview

This ETL pipeline reads messy customer data from an Excel file, cleans and transforms it, splits it by country, and loads the cleaned records into MySQL and PostgreSQL databases. It also generates a detailed metadata JSON file with key statistics about the processing.

---

## 🧱 Tech Stack

- **Language:** Python
- **Libraries:** pandas, SQLAlchemy, openpyxl
- **Databases:** MySQL (USA), PostgreSQL (UK & India)
- **Logging:** Python's `logging` module
- **Metadata Output:** JSON format

---

## 🛠️ Features

- Extract from Excel (`.xlsx`)
- Data cleaning & transformation:
  - Remove nulls & duplicates
  - Standardize date format
  - Strip whitespaces
  - Normalize case
  - Clean country values
- Split by country: USA, UK, India
- Load into:
  - MySQL → `customer_us_db`
  - PostgreSQL → `customer_global_db`
- Metadata generation:
  - Total records
  - Records per country
  - Timestamp
  - Column types & sample values
- Logging to `logs/etl.log`

---

## 📂 Folder Structure

```
etl_pipeline/
│
├── raw-data/
│   └── messy_customers_data.xlsx
├── final_data/
│   ├── country_usa.csv
│   ├── country_uk.csv
│   └── country_india.csv
├── logs/
│   └── etl.log
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── metadata.py
├── sql/
│   └── db_schemas.sql
│
├── config/
│   └── db_config.py
│   └── logging_config.py
├── test_file/
│   └── test.ipynb
│
├── main.py
├── requirements.txt
├── metadata.json
```

---

## 🚀 How to Run

### 1. 🔧 Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. 🛠️ Configure DB Credentials

Edit `config/db_config.py`:
```python
# MySQL (for USA)
username, password, host, database

# PostgreSQL (for UK & India)
username, password, host, database
```

### 3. 🏗️ Set Up Databases

Run the provided `db_schemas.sql` file in your MySQL and PostgreSQL terminals to create the required databases and tables.

---

### 4. ▶️ Run the ETL Pipeline

```bash
python main.py
```

---

## 📦 Deliverables

1. ✅ **Cleaned CSV files** inside the `final_data/` directory.
2. ✅ **Python scripts** used for ETL (`etl/`, `main.py`, `config/`).
3. ✅ **MySQL and PostgreSQL schemas** in `db_schemas.sql`.
4. ✅ **Metadata** in structured `metadata.json`.
5. ✅ **README file** describing how to run the script and prerequisites.
6. ✅ **Logs** in `logs/etl.log` showing all steps and errors (if any).

---

## 📬 Author

Built by Umair (Data Engineer Intern) 💼  
Feel free to reach out for improvements or feedback!
