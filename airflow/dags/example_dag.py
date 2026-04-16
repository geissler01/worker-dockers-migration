from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import socket
import time

def check_worker():
    print(socket.gethostname())
    time.sleep(15)

with DAG('check_3_2', start_date=datetime(2024,1,1), schedule=None) as dag:
    for i in range(1, 4):
        PythonOperator(task_id=f'worker_{i}', python_callable=check_worker)