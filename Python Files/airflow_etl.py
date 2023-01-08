from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from main import spotify_capstone

my_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['airflow@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
my_dag = DAG(
    'spotify_dag',
    default_args = my_args,
    description= 'Spotify ETL',
    schedule= '* * * * *'
)


run_etl = PythonOperator(
    task_id='spotify_capstone',
    python_callable= spotify_capstone,
    dag=my_dag
)
run_etl