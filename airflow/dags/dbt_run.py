from airflow.operators.python import PythonOperator
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from db.utils import generate_fake_sales
from db.main import generate_tables

default_args = {
    'owner': 'you',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dbt_run_dag',
    default_args=default_args,
    description='A simple DAG to run dbt transformations',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False
) as dag:
    initialize_db = PythonOperator(
        task_id="init_db",
        python_callable=generate_tables
    )

    seed_db = PythonOperator(
        task_id="seed_database",
        python_callable=generate_fake_sales
    )

    list_files = BashOperator(
        task_id='list_files',
        bash_command='cd /opt/airflow/project/analytics && ls -R'
    )

    run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='cd /opt/airflow/project/analytics && dbt run --profiles-dir /home/airflow/.dbt --profile DataStitcher'
    )
    initialize_db >> seed_db >> list_files >> run_dbt
