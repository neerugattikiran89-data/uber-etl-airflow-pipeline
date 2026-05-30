from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'scripts')
    )
)

from load import run_pipeline

default_args = {
    "owner": "kiran",
    "start_date": datetime(2026, 5, 29),
}

with DAG(
    dag_id="uber_etl_pipeline",
    default_args=default_args,
    schedule="@daily",
    catchup=False,
) as dag:

    run_etl_task = PythonOperator(
        task_id="run_etl_task",
        python_callable=run_pipeline
    )

    run_etl_task
