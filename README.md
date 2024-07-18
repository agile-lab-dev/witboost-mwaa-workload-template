<p align="center">
    <a href="https://www.witboost.com/">
        <img src="docs/img/witboost_logo.svg" alt="witboost" width=600>
    </a>
</p>

Designed by [Agile Lab](https://www.agilelab.it/), Witboost is a versatile platform that addresses a wide range of sophisticated data engineering challenges. It enables businesses to discover, enhance, and productize their data, fostering the creation of automated data platforms that adhere to the highest standards of data governance. Want to know more about witboost? Check it out [here](https://witboost.com/platform) or [contact us!](https://witboost.com/contact-us)

This repository is part of our [Starter Kit](https://github.com/agile-lab-dev/witboost-starter-kit) meant to showcase witboost's integration capabilities and provide a "batteries-included" product.


# Airflow Workload Template

- [Overview](#overview)
- [Usage](#usage)

# Overview

Use this template to automatically create a DAG in an Airflow instance which helps in orchestrating the data flow through various other components. The component from this template must be created last since it will depend on some components that had already been created.

Refer to the [witboost Starter Kit repository](https://github.com/agile-lab-dev/witboost-starter-kit) for information on the Specific Provisioner that can be used to deploy components created with this template.


### What's a Template?

A Template is a tool that helps create components inside a Data Mesh. Templates help establish a standard across the organization. This standard leads to easier understanding, management and maintenance of components. Templates provide a predefined structure so that developers don't have to start from scratch each time, which leads to faster development and allows them to focus on other aspects, such as testing and business logic.

For more information, please refer to the [official documentation](https://docs.witboost.agilelab.it/docs/p1_user/p6_advanced/p6_1_templates/#getting-started).


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

To get information on how to use this template, refer to this [document](./docs/index.md).

### Component Testing

To verify the component before deploying it along with the Data Product, the component needs to be tested against a CUE Policy defined for an [Airflow Workload](./policies/airflow.cue). This policy needs to be defined inside the **Governance** section of the Witboost Platform.

For more information, please refer to the [official documentation](https://docs.witboost.agilelab.it/docs/p1_user/p5_managing_policies/p5_1_overview).


## License

This project is available under the [Apache License, Version 2.0](https://opensource.org/licenses/Apache-2.0); see [LICENSE](LICENSE) for full details.

## About us

<p align="center">
    <a href="https://www.agilelab.it">
        <img src="docs/img/agilelab_logo.svg" alt="Agile Lab" width=600>
    </a>
</p>

Agile Lab creates value for its Clients in data-intensive environments through customizable solutions to establish performance driven processes, sustainable architectures, and automated platforms driven by data governance best practices.

Since 2014 we have implemented 100+ successful Elite Data Engineering initiatives and used that experience to create Witboost: a technology-agnostic, modular platform, that empowers modern enterprises to discover, elevate and productize their data both in traditional environments and on fully compliant Data mesh architectures.

[Contact us](https://www.agilelab.it/contacts) or follow us on:
- [LinkedIn](https://www.linkedin.com/company/agile-lab/)
- [Instagram](https://www.instagram.com/agilelab_official/)
- [YouTube](https://www.youtube.com/channel/UCTWdhr7_4JmZIpZFhMdLzAA)
- [Twitter](https://twitter.com/agile__lab)