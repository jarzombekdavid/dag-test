
from datetime import datetime

from airflow.models import DAG
from airflow.operators.dummy import DummyOperator

DEFAULT_DATE = datetime(2016, 1, 1)

default_args = {
    "owner": "airflow",
    "start_date": DEFAULT_DATE,
}

with DAG(dag_id="this_should_show_up", default_args=default_args, schedule_interval='@once') as dag:
    task_a = DummyOperator(task_id="test_task_a")