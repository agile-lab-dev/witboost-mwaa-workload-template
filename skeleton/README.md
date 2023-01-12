# MWAA workload for our Data Product

MWAA is one of the main components of the Data Product. It will orchestrate the data flow through different components, so this component must be created last. It will depend on some components that should have already been created in the previous steps.

The following are the steps that we need to follow in order to work with the MWAA workload.

## Creating a MWAA Workload

### Prerequisites

A Data Product should already exist in order to attach the new components to it.
The components **Airbyte Workload**, **Snowflake Output Port**, and the **Snowflake SQL Workload** (if used) should exist in the Data Product.

1. To create this workload, we go again to the Builder and in the **Create** section, we choose the MWAA Workload by going into Workloads subsection of the "Create" section and then select **"Workload Airflow MWAA Template"** from the available options.

2. After clicking **"Choose"** button, we will be directed "Create a New Component" page. There are 3 sections within this page:

### 1. Component Basic Information

In this section, you are expected to fill in some details which will be essential in order to create the workflow.

- Name: Name which is used for display purposes. Default Name is provided if you don't have any idea what to fill in the first place (Required).
- Fully Qualified Name: Human-readable name that identifies the Fully Qualified Name (Optional).
- Description: Detailed information as to why this workload is created in first place and what is its intended usage (Required).
- Domain: Select the Domain of the Data Product for which this workload is getting associated (Required).
- Data Product: Select the appropriate Data Product for which this workload is getting associated (Required).
- Identifier: A unique **uneditable** identifier for the entity inside the domain. It is expected to be a sequence of [a-zA-Z] letters separated by any of [-_] symbols (Required).
- Data Product Development Group: This will be the group of developers who possess access to the Data Product Repositories. Since we are selecting the Data Product to which this workload will be associated, the appropriate value will be prefilled which is uneditable (Required).
- Depends On: If you want your workload to depend on other components from the Data Product, you can choose this option.

   > In the case of the MWAA operator, you should add here the **Snowflake Output Port, the Airbyte Component, and the SQL Workload Component if existent** present on the Data Product in order for the orchestrator to execute only when these components are in place
   

*Example:*

| Field name              | Example value                                                                                                                                                                                                                   |
|:------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Name**                | Airflow Orchestration                                                                                                                                                                                                           |
| **Description**         | Orchestrator                                                                                                                                                                                                                    |
| **Domain**              | domain:healthcare                                                                                                                                                                                                               |
| **Data Product**        | system:healthcare.vaccinationsdp.0                                                                                                                                                                                              |
| ***Identifier***        | Will look something like this: *healthcare.vaccinationsdp.0.airflow-orchestration*                                                                                                                                              |
| ***Development Group*** | Might look something like this: *group:datameshplatform* Depends on the Data Product development group                                                                                                                          | 
| **Depends On**          | urn:dmb:cmp:healthcare:vaccinationsdp:0:airbyte-vaccinations-ingestion, urn:dmb:cmp:healthcare:vaccinationsdp:0:snowflake-vaccinations-sql-workload, urn:dmb:cmp:healthcare:vaccinationsdp:0:snowflake-vaccionation-output-port |

After filling in all fields with appropriate fields, your page should look like the one shown below. Click on the **"Next Step"** button to move to next section.

### 2. Airflow Infrastructure Details

In this section, you are expected to fill in details pertaining to Airflow.

- Cron expression defining schedule: Time (UTC) at which the Job will trigger (Required).
- Dag File Name: Name of the Dag File (Required).

*Example:*

| Field name          | Example value            |
|:--------------------|:-------------------------|
| **Cron expression** | 5 5 * * *                |
| **Dag name**        | airbyte_snowflake_dag.py |

After filling all fields with the appropriate values, your page should look like the one shown below. Click on the **"Next Step"** button to move to next section.


### 3. Choose a Location

In this section, you are expected to fill in details pertaining to the location of the Workload.

- Host: The host where the repository will be created. By default, is `gitlab.com` (Required).
- User / Group: A group or a user that the repository belongs to, e.g. 'group/sub-group/sub-sub-group' or 'name.surname'. There are two ways of creating a new component. One way of creating it is by making a monorepo (in that way you will never change the field 'Repository' and it will always be a repository containing your data product, and you will only need to change the root directory). The second way of creating a new component is by doing it always in another repository (in that case the root directory will always be '.' and you will always change the repository field) (Required).
- Repository: Name of the repository (Required).
- Root Directory: Path that will be used as the repository root for this Data Product. By default, the value would be **"."**.

*Example:*

| Field name        | Example value                                  |
|:------------------|:-----------------------------------------------|
| ***Host***        | gitlab.com                                     |
| **User/Group**    | MyCompany/mesh.repository/sandbox/vaccinations |
| **Repository**    | VaccinationsMWAAComponent                      |
| **RootDirectory** | .                                              |

After filling in all fields with appropriate fields, your page should look like the one shown below. Click on the **"Next Step"** button to move to next section.


In the **"Review and Create"** section, all the previously filled data would be present through which we can cross-check the information once again. If you are satisfied, then proceed to create a Data Product by clicking on **"Create"** button present in the bottom-right of the section. Otherwise, you can go back to the previous sections by clicking on **"Back"** button.

After clicking on "Create" button, the process of creating a Data Product will be initiated which would be done in 3 phases (Fetching Skeleton+Template, Publish and Register). If there aren't any errors in entering the information, all the 3 phases will be successful and will give you the links to the newly created Repository and the component in the Catalog.

### 4. Component manual customization

At this point the component should be correctly initialised and the related repository created. By default, the MWAA python DAG file does not contain any operators, since we don't know in advance what operators the user will need to perform the needed interaction with the other components.

In particular, to cover our use-case we need to add some functions to our python DAG file: a custom function to retrieve the Airbyte connection id by its name using the Airbyte API and 3 dag operators. These operators will have the following functions:

* The first one is related to the use of the custom function
* The second one is needed to trigger the Airbyte connection once we get its id
* The third one is needed to trigger a Snowflake SQL workload created earlier with the corresponding template.

The final python DAG needed to cover our use-case will look like the following code snippet. Copy only the sections that differ from the original skeleton (see below the snippet) in order to have the same structure but with all the new values and functions.

```python
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

# TEMPLATE VALUES
# This values will be already prefilled in the skeleton, don't modify them
schedule_cron = ...
component_identifier = ...
default_args = {
    'owner': 'agilelab',
    'start_date': days_ago(1),
    'depends_on_past': False
}

# CUSTOM VALUES - copy them below the template values and fill them
airbyte_conn_name = ... # This should be the name you gave to the connection when creating the Airbyte component
sql_filename = ... # This should be the file name you used in the Snowflake SQL workload and the one present in that component 
data_product_name = component_identifier.rsplit(".", 1)[0] # Keep this as-is
sm_secretId_name = "airflow/connections/airbyte" # Keep this as-is


# CUSTOM FUNCTION - copy it
def get_airbyte_conn_id(ds=None, **kwargs):
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
        if c.get("name") == f"{data_product_name}.{airbyte_conn_name}":
            return c.get("connectionId")

# DAG
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
    # Copy this content into the skeleton DAG
    airbyte_conn_id = PythonOperator(
        task_id="get_airbyte_conn_id",
        python_callable=get_airbyte_conn_id,
    )
    sync_source_destination = AirbyteTriggerSyncOperator(
        task_id='airbyte_sync_source_dest_example',
        connection_id=airbyte_conn_id.output,
        airbyte_conn_id="airbyte",
        trigger_rule="none_failed",
    )
    snowflake_select = SnowflakeOperator(
        task_id="snowflake_select",
        sql=f"{data_product_name}.{sql_filename}",
        snowflake_conn_id="snowflake",
        schema='public',
    )

    airbyte_conn_id >> sync_source_destination >> snowflake_select
# end with
```

Let's dive a bit on what this script does and what to copy into the skeleton: 


This section is already present and prefilled in the original template and includes values that are retrieved from the form. So leave it there in the original skeleton.

```python
# TEMPLATE VALUES
# This values will be already prefilled in the skeleton, don't modify them
schedule_cron = ...
component_identifier = ...
default_args = {
   'owner': 'agilelab',
   'start_date': days_ago(1),
   'depends_on_past': False
} 
```

This section will specify some values that are necessary to each step of this pipeline. This includes custom values like the Airbyte connection name and the SQL filename related to the components you created previously (Remember we asked you to keep them?). Other values are present like the calculation of the Data Product name and the path to the secret connection string to Airbyte in the Secrets Manager. Fill the first two with your values and leave the other as-is.

```python
# CUSTOM VALUES - copy them below the template values and fill them
airbyte_conn_name = ... # This should be the name you gave to the connection when creating the Airbyte component
sql_filename = ... # This should be the file name you used in the Snowflake SQL workload and the one present in that component 
data_product_name = component_identifier.rsplit(".", 1)[0] # Keep this as-is
sm_secretId_name = "airflow/connections/airbyte" # Keep this as-is
```

This section defines a function to retrieve the Airbyte Connection ID based on the Connection Name you added before. This is to reduce the hassle of accessing the Airbyte environment to retrieve this ID by yourself.

```python
# CUSTOM FUNCTION - copy it
def get_airbyte_conn_id(ds=None, **kwargs):
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
      if c.get("name") == f"{data_product_name}.{airbyte_conn_name}":
            return c.get("connectionId")
```

These are the actual steps of the pipeline. As you can see we first get the connection id, then we call the Airbyte Job to ingest the data and transfer it to the Snowflake table we provided in the Airbyte component. Finally, we are invoking a Snowflake Operator to execute our SQL script we defined previously. You should copy them inside the `with DAG(...) as dag:` and leave the DAG creation as-is.

```python
   ### Add your dag Operators here
   # Copy this content into the skeleton DAG
   airbyte_conn_id = PythonOperator(
      task_id="get_airbyte_conn_id",
      python_callable=get_airbyte_conn_id,
   )
   sync_source_destination = AirbyteTriggerSyncOperator(
      task_id='airbyte_sync_source_dest_example',
      connection_id=airbyte_conn_id.output,
      airbyte_conn_id="airbyte",
      trigger_rule="none_failed",
   )
   snowflake_select = SnowflakeOperator(
      task_id="snowflake_select",
      sql=f"{data_product_name}.{sql_filename}",
      snowflake_conn_id="snowflake",
      schema='public',
   )

   airbyte_conn_id >> sync_source_destination >> snowflake_select
```

After copying the sections `CUSTOM VALUES`, `CUSTOM FUNCTION` and the dag Operators, you're good to go. Commit the changes in order to trigger the update of the corresponding python file that will be put inside the AWS S3 bucket.

Since the MWAA component as we have seen is based on a generic template, you are free to customize the DAG file in order to perform all the operations needed (e.g. to trigger multiple Snowflake SQL workloads, multiple Airbyte connection, etc.)