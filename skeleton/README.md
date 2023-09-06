# ${{ values.name | dump }}

- [Overview](#overview)
- [Usage](#usage)

# Overview

Use this component to automatically create a DAG in an Amazon MWAA (Managed Workflows for Apache Airflow) instance which helps in orchestrating the data flow through various components.

### What's a Workload?

Workload refers to any data processing step (ETL, job, transformation etc.) that is applied to data in a Data Product. Workloads can pull data from sources external to the Data Mesh or from an Output Port of a different Data Product or from Storage Areas inside the same Data Product, and persist it for further processing or serving.


### MWAA

Amazon Managed Workflows for Apache Airflow (MWAA) is an AWS service that allows users to orchestrate their workflows using Airflow Directed Acyclic Graphs (DAGs) written in Python without having to manage the Airflow infrastructure themselves.

Key features of Amazon MWAA include:

- Managed Service: Amazon MWAA manages the work involved in setting up Airflow, from provisioning the infrastructure capacity (server instances and storage) to installing the software and providing simplified user management and authorization through AWS Identity and Access Management (IAM) and Single Sign-On (SSO).
- Integration with AWS Services: Amazon MWAA is a workflow environment that allows data engineers and data scientists to build workflows using other AWS, on-premise, and other cloud services. Workflows in Amazon MWAA can interact with various AWS services like S3, EMR, Athena, SageMaker, etc.
- Security: Amazon MWAA uses AWS KMS to ensure your data is secure at rest. By default, Amazon MWAA uses AWS managed AWS KMS keys, but you can configure your environment to use your own customer-managed AWS KMS key.
- Autoscaling: Amazon MWAA configures an environment to run hundreds of tasks in parallel and workers concurrently. As tasks are queued, Amazon MWAA adds workers to meet demand, up to and until it reaches the number you define in Maximum worker count. This autoscaling mechanism will continue running the additional workers, until there are no more tasks to run. When there are no more tasks running, or tasks in the queue, Amazon MWAA disposes of the workers and scales back down to a single worker.

Learn more about it on the [official website](https://aws.amazon.com/managed-workflows-for-apache-airflow/).

# Usage

To get information about this component and how to use it, refer to this [document](./docs/index.md).