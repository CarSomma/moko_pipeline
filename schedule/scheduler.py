from airflow import DAG
from airflow.providers.docker.operators import docker
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 15),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'schedule_container_startup',
    default_args=default_args,
    description='A DAG to schedule the startup of a Docker container',
    schedule=timedelta(minutes=5),  # Adjust the schedule interval as needed
)

start_container = docker.DockerOperator(
    task_id='start_container',
    image='mock-pipeline-eljob_service:latest',  # Replace with your Docker image
    command='/bin/bash -c "docker start eljob"',  # Command to start the container
    dag=dag,
)

start_container
