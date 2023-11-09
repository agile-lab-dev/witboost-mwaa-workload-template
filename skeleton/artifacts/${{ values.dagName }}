from airflow.utils.dates import days_ago
from datetime import timedelta
import os

dag_name = os.path.basename(__file__).replace(".py", "")

schedule_cron = "${{ values.scheduleCron }}"  # The custom cron expression you want to use
component_identifier = "${{ values.identifier }}"

default_args = {
    'owner': 'agilelab',
    'start_date': days_ago(1),
    'depends_on_past': False
}

# Add your custom functions here

# 'os.path.basename(__file__).replace(".py", "")' uses the file name secrets-manager.py for a DAG ID of secrets-manager
with DAG(
        dag_id=dag_name,
        default_args=default_args,
        dagrun_timeout=timedelta(hours=2),
        start_date=days_ago(1),
        schedule_interval=schedule_cron,
        is_paused_upon_creation=False
) as dag:
    # Add your dag Operators here
    ...
