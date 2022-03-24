from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1), # time in UTC + 0  
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'http_url_request_read',
    default_args=default_args,
    description='assignment',
    schedule_interval="@daily",  # here we can change periodicity of the application 
)

t1 = BashOperator(
  task_id='odd_api',
  bash_command='python3 ~/scripts/assignment.py',
   dag=dag,
)

t1
