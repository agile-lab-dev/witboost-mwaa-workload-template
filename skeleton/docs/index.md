## Component Basic Information

| Field Name       | Value                     |
|:-----------------|:--------------------------|
| **Name**         | ${{ values.name }}        |
| **Description**  | ${{ values.description }} |
| **Domain**       | ${{ values.domain }}      |
| **Data Product** | ${{ values.dataproduct }} |
| **Identifier**   | ${{ values.identifier }}  |
| **Depends On**   | ${{ values.dependsOn }}   |


## Airflow Infrastructure Details

| Field Name          | Value                      |
|:--------------------|:---------------------------|
| **Cron Expression** | ${{ values.scheduleCron }} |
| **Dag name**        | ${{ values.dagName }}      |