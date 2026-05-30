# Uber ETL Airflow Pipeline

## Project Overview

This project is an automated ETL (Extract, Transform, Load) pipeline built using Python, Pandas, MySQL, SQLAlchemy, and Apache Airflow.

The pipeline extracts Uber ride data from a CSV file, performs data transformation, and loads the processed data into a MySQL database. Apache Airflow is used to schedule and automate the workflow daily.

---

## Technologies Used

* Python
* Pandas
* MySQL
* SQLAlchemy
* Apache Airflow

---

## ETL Workflow

1. Extract data from CSV
2. Transform data using Pandas
3. Load transformed data into MySQL
4. Schedule workflow using Airflow DAG

---

## Airflow Scheduling

The ETL pipeline is scheduled using Apache Airflow with a daily schedule.

```python
schedule="@daily"
```

---

## Project Structure

```bash
uber-etl-airflow-pipeline/
│
├── dags/
├── scripts/
├── data/
├── logs/
└── .gitignore
```

---

## Features

* Automated ETL pipeline
* Daily workflow scheduling
* MySQL database integration
* Airflow DAG orchestration
* Data transformation using Pandas

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/neerugattikiran89-data/uber-etl-airflow-pipeline.git
```

### Activate Virtual Environment

```bash
source venv/bin/activate
```

### Run ETL Pipeline

```bash
python scripts/load.py
```

### Start Airflow Scheduler

```bash
airflow scheduler
```

### Start Airflow API Server

```bash
airflow api-server --port 8081
```

---

## Future Improvements

* API-based data extraction
* Incremental loading
* Docker integration
* Cloud deployment
* Data validation checks
