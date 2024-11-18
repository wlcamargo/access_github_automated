from datetime import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

default_args = {
    "owner": "Wallace Camargo",
    "depends_on_past": False,
}

# Define the DAG using the @dag decorator
with DAG(
    dag_id="access-github-sparkanos",
    default_args=default_args,
    start_date=datetime(2024, 10, 31),  # Fixed start date
    schedule_interval="@hourly",
    catchup=False,  # Avoid running past tasks
    tags=["github", "access"],
) as dag:

    # Task to run the ingestion container
    run_access_github = DockerOperator(
        task_id="access-github-sparkanos",
        image="access-github-sparkanos",
        container_name="access-github",  # Ensure this is unique if running concurrently
        api_version="auto",
        auto_remove=True,
        command="python3 github-access-google.py",
        docker_url="tcp://docker-proxy:2375",
        network_mode="airflow_default",
        mount_tmp_dir=False,  # Disable mounting the temporary directory
    )

    # Define the task dependencies
    run_access_github
