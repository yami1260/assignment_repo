from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(minutes=3),
    }

with DAG(
        dag_id='extract_and_load',
        schedule_interval="0 */1 * * *",
        start_date=datetime(2023, 8, 4),
        catchup=False) as dag:
    # write you extract and load airflow dag here
    # the dag should have three bash operators
    # migration >> extract >> load
    migration_task = BashOperator(
        task_id='migration',
        bash_command='python /opt/airflow/dags/migration.py',
        dag=dag
    )
    # Extract Task
    extract_task = BashOperator(
        task_id='extract',
        bash_command='python D:/Yamini/Task/home_assignment/dags/scripts/extract.py',
        dag=dag
    )
    # Load Task
    load_task = BashOperator(
        task_id='load',
        bash_command='python /opt/airflow/dags/load.py',
        dag=dag
    )

    # Set Task Dependencies
    #migration_task >> extract_task >> load_task
    extract_task >> load_task >> migration_task
