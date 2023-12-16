import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# Get the value of the AIRFLOW_HOME environment variable
AIRFLOW_HOME = os.getenv('AIRFLOW_HOME')
cwd = os.path.join(AIRFLOW_HOME, 'dbt_project')

with DAG(
        dag_id='transform',
        schedule_interval="0 */1 * * *",
        start_date=datetime(2023, 8, 4),
        catchup=False) as dag:

    transform = BashOperator(
        task_id='transform',
        bash_command='dbt build',
        cwd=cwd,
        env=os.environ.copy(),
        dag=dag
    )

transform
