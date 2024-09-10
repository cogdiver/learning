"""
DAG for dynamically generating tasks based on the files present in a directory and keeping a log of historical files.
This DAG demonstrates the concept of dynamic task generation in Airflow, which allows you to create new tasks without 
modifying the DAG code, simply by adding or removing files from the directory. 

Key characteristics:
- **Dynamic Task Creation**: New tasks are created automatically when new files are added to the specified directory.
  This means that the number of tasks can vary without changing the DAG definition itself. However, Airflow requires
  a DAG re-parsing to detect these changes.
  
- **Handling Historical Logs**: A record of previously processed files is kept to avoid losing access to logs and task 
  execution history for files that are no longer present in the directory. This is managed by writing a history of 
  processed files into a text file and marking these historical tasks with `TriggerRule.ALL_SKIPPED` to ensure they 
  appear in the Airflow UI but are skipped during execution.
  
- **Challenges**: 
  - If tasks are created or removed dynamically, they won't show up in the UI unless handled carefully. Logs for tasks
    associated with deleted files could be lost unless we maintain this history.
  - Tasks cannot be grouped into different `TaskGroups` or assigned different operators, as this would cause Airflow to
    consider them as different tasks, thus losing access to the logs of previous executions.
  - If the dynamic task generation function is too heavy, it may slow down DAG parsing, as the function will run every
    time the DAG is refreshed or modified in the Airflow UI.
    
Recommendation:
- For larger task sets or more complex workflows, consider using a separate DAG to handle historical records and prevent 
  performance degradation over time.
"""
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago
from airflow.utils.task_group import TaskGroup
from airflow.utils.trigger_rule import TriggerRule
from datetime import timedelta
import os

BASE_DATA = "dags/data"

# Function to get the list of current and historical files
def get_data_sources():
    history_file = "dags/historical_execution.txt"

    # Read historical files
    with open(history_file, "r") as f:
        history = f.read().splitlines()

    # Actual files in the directory
    now = os.listdir(BASE_DATA)

    # Combine the historical and current files, avoiding duplicates
    combined_files = set(history).union(set(now))
    previous = combined_files - set(now)

    # Update the history file with the combined list of files
    with open(history_file, "w") as file:
        file.write("\n".join(combined_files) + "\n")

    # Return the previous (historical) files and the current ones
    return previous, now

# Function to process each file by removing it from the directory
def process_data(source):
    os.remove(f"{BASE_DATA}/{source}")
    print(f"Processing data from {source}")

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG with its schedule and configuration
with DAG(
    'dynamic_task_generation_dag',
    default_args=default_args,
    description='An example of dynamic task generation in Airflow',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
) as dag:

    # EmptyOperator used as the starting point of the DAG
    start = EmptyOperator(task_id='start')

    # Get the list of historical and current files
    history, actual = get_data_sources()

    # TaskGroup for processing both historical and current files
    with TaskGroup("processing") as processing:
        
        # Tasks for historical files (marked as skipped using TriggerRule.ALL_SKIPPED)
        for source in history:
            task = PythonOperator(
                task_id=f'process_{source}',
                python_callable=lambda: None,  # Does nothing, but logs are kept
                trigger_rule=TriggerRule.ALL_SKIPPED  # Skips execution but keeps it visible
            )
            start >> task # Set task dependency

        # Tasks for current files (actual processing)
        for source in actual:
            task = PythonOperator(
                task_id=f'process_{source}',
                python_callable=process_data,  # Actual file processing
                op_kwargs={'source': source},  # Passing file name as an argument
            )
            start >> task # Set task dependency

    # EmptyOperator used as the ending point of the DAG
    end = EmptyOperator(task_id='end')
    processing >> end # Set task dependency
