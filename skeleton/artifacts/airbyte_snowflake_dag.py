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

sm_secretId_name = 'airflow/connections/airbyte_url'

default_args = {
    'owner': 'agilelab',
    'start_date': days_ago(1),
    'depends_on_past': False
}

def get_ab_conn_id(ds=None, **kwargs):
    ### Gets the secret airbyte from Secrets Manager
    hook = AwsBaseHook(client_type='secretsmanager')
    client = hook.get_client_type('secretsmanager')
    response = client.get_secret_value(SecretId=sm_secretId_name)
    ab_url = response["SecretString"] + "/api/v1"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    workspace_id = requests.post(f"{ab_url}/workspaces/list", headers=headers).json().get("workspaces")[0].get("workspaceId")
    payload = json.dumps({"workspaceId": workspace_id})
    connections = requests.post(f"{ab_url}/connections/list", headers=headers, data=payload).json().get("connections")
    for c in connections:
        if c.get("name") == "${{ values.connectionName }}":
            return c.get("connectionId")

### 'os.path.basename(__file__).replace(".py", "")' uses the file name secrets-manager.py for a DAG ID of secrets-manager
with DAG(
        dag_id=os.path.basename(__file__).replace(".py", ""),
        default_args=default_args,
        dagrun_timeout=timedelta(hours=2),
        start_date=days_ago(1),
        schedule_interval='${{ values.scheduleCron }}', 
        is_paused_upon_creation=False
) as dag:
    airbyte_conn_id = PythonOperator(
        task_id="get_ab_conn_id",
        python_callable=get_ab_conn_id,
    )
    sync_source_destination = AirbyteTriggerSyncOperator(
        task_id='airbyte_sync_source_dest_example',
        connection_id=airbyte_conn_id.output,
        airbyte_conn_id='airbyte',
        trigger_rule="none_failed",
    )
    snowflake_select = SnowflakeOperator(
        task_id="snowflake_select",
        sql="${{ values.destinationSql }}".split("/")[-1],
        snowflake_conn_id="snowflake",
        schema='public',
    )

    airbyte_conn_id >> sync_source_destination >> snowflake_select
