# ${{ values.name | dump }}

- [Overview](#overview)
- [Usage](#usage)

# Overview

Use this component to automatically create a DAG in an Airflow instance which helps in orchestrating the data flow through various components.

### What's a Workload?

Workload refers to any data processing step (ETL, job, transformation etc.) that is applied to data in a Data Product. Workloads can pull data from sources external to the Data Mesh or from an Output Port of a different Data Product or from Storage Areas inside the same Data Product, and persist it for further processing or serving.


### Apache Airflow

Apache Airflow is an open-source platform designed for orchestrating complex data pipelines. It allows users to programmatically author, schedule, and monitor workflows, providing a scalable and extensible framework for managing data processing tasks. Airflow enables the definition and visualization of workflows as Directed Acyclic Graphs (DAGs), simplifying the management of dependencies and data flow within complex systems.

Key features of Apache Airflow include:

- **Workflow Scalability and Modularity**: Airflow offers a highly scalable and modular architecture, supporting large-scale data processing through parallel execution of tasks across multiple worker nodes. Its modular design facilitates the development, testing, and maintenance of data pipelines by breaking them down into smaller, manageable tasks.
- **Dynamic and Extensible**: Airflow's dynamic and extensible nature allows for the easy extension of its functionality through custom operators and sensors, catering to specific business needs. It also supports dynamic task generation, enabling workflows to adapt to changing conditions or data.
- **Dependency Management and Task Scheduling**: Airflow provides robust capabilities for managing dependencies between tasks and scheduling tasks. Features like task retries, rescheduling, and backfilling enhance the reliability and flexibility of workflows.
- **Monitoring and Alerting**: The platform includes a built-in web-based user interface, the Airflow UI, which offers real-time insights into workflow statuses, task progress, logs, and alerts for failures or delays. This feature is crucial for maintaining the health and performance of data pipelines.

Learn more about it on the [official website](https://airflow.apache.org/docs/apache-airflow/stable/index.html).

# Usage

To get information about this component and how to use it, refer to this [document](./docs/index.md).