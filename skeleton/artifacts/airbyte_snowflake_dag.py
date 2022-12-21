from airflow import DAG, settings, secrets
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.providers.amazon.aws.hooks.base_aws import AwsBaseHook
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from datetime import timedelta
import os
import requests
import json

schedule_cron = "${{ values.scheduleCron }}" # The custom cron expression you want to use
component_identifier = "${{ values.identifier }}"

default_args = {
    'owner': 'agilelab',
    'start_date': days_ago(1),
    'depends_on_past': False
}

### Add your custom functions here

### 'os.path.basename(__file__).replace(".py", "")' uses the file name secrets-manager.py for a DAG ID of secrets-manager
with DAG(
        dag_id=os.path.basename(__file__).replace(".py", ""),
        default_args=default_args,
        dagrun_timeout=timedelta(hours=2),
        start_date=days_ago(1),
        schedule_interval=schedule_cron, 
        is_paused_upon_creation=False
) as dag:
    ### Add your dag Operators here
    ...