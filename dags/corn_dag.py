#A cron expression is a string of characters that specifies the 
#cron job schedule by defining exact times, dates, or recurring patterns
# cron jobs are used for scheduling
# we can use airflow instead of corn jobs for scheduling
# Minute: Hour: Day of the Month: Month: Day of the Week: 

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'muki',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id="dag_with_cron_expression_daily",
    start_date=datetime(2024, 2, 15),
    schedule_interval='0 0 * * *'
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo dag with cron expression!"
    )
    task1