import os
from datetime import datetime

from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

DEFAULT_DATE = datetime(2016, 1, 1)

default_args = {
    "owner": "airflow",
    "start_date": DEFAULT_DATE,
}

def print_envs():
    print(os.getenv('AWS_DEFAULT_REGION'))

with DAG(dag_id="this_should_show_up", default_args=default_args, schedule_interval='@once') as dag:
    task_a = PythonOperator(
        task_id="test_task_a",
        callable=print_envs
        )