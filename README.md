# MWAA workload for our Data Product

The following are the steps that we need to follow in order to work with MWAA Workflow:

## Creating a MWAA Workload

2. To create this workload, we go again to the Builder and in the **Create** section, we choose the MWAA Workload by going into Workloads subsection of the "Create" section and then select **"Workload Airflow MWAA Template"** from the available options.

   <img src="./images/MWAAonBuilder.png">

3. After clicking **"Choose"** button, we will be directed "Create a New Component" page. There are 3 sections within this page:

   ### 1. Component Basic Information

      In this section, you are expected to fill in some details which will be essential in order to create the workflow.

      - Name: Name which is used for display purposes. Default Name is provided if you don't have any idea what to fill in the first place (Required).
      - Fully Qualified Name: Human-readable name that identifies the Fully Qualified Name (Optional).
      - Description: Detailed information as to why this workload is created in first place and what is its intended usage (Required).
      - Domain: Select the Domain of the Data Product for which this workload is getting associated (Required).
      - Data Product: Select the appropriate Data Product for which this workload is getting associated (Required).
      - Identifier: A unique **uneditable** identifier for the entity inside the domain. It is expected to be a sequence of [a-zA-Z] letters separated by any of [-_] symbols (Required).
      - Data Product Development Group: This will be the group of developers who possess access to the Data Product Repositories. Since we are selecting the Data Product to which this workload will be associated, the appropriate value will be prefilled which is uneditable (Required).
      - Depends On: If you want your workload to depend on other components from a Data Product, you can choose this option (Optional).
      - Reads From: This is filled only for DataPipeline workloads, and it represents the list of output ports or external systems that is reading (Optional).

      After filling in all fields with appropriate fields, your page should look like the one shown below. Click on the **"Next Step"** button to move to next section.

      <img src="./images/MWAABasicInfo.png">

   ### 2. Airflow Infrastructure Details

      In this section, you are expected to fill in details pertaining to Airflow.

      - Source S3 Dag Location: Specify the name of the source bucket (Required).
      - Destination S3 Dag Location: Specify the name of the destination bucket (Required).
      - Cron expression defining schedule: Time (UTC) at which the Job will trigger (Optional).
      - Source Dag Path: Path to the source dag like path/to/the/file (Optional).
      - Destination Dag Path: Path to the destination dag like path/to/the/file (Optional).
      - Destination of the Snowflake SQL File: It will be put in the destination bucket on the location you specify like path/to/the/file (Optional).
      - Name of the Airbyte Connection: Insert the name of the Airbyte connection you created (Optional).
      
      After filling in all fields with appropriate fields, your page should look like the one shown below. Click on the **"Next Step"** button to move to next section.

      <img src="./images/MWAAInfraDetails.png">

   ### 3. Choose a Location
      In this section, you are expected to fill in details pertaining to the location of the Workload.

      - Host: The host where the repository will be created. By default is `gitlab.com` (Required).
      - User / Group: A group or a user that the repository belongs to, e.g. 'group/sub-group/sub-sub-group' or 'name.surname'. There are two ways of creating a new component. One way of creating it is by making a monorepo (in that way you will never change the field 'Repository' and it will always be a repository containing your data product, and you will only need to change the root directory). The second way of creating a new component is by doing it always in another repository (in that case the root directory will always be '.' and you will always change the repository field) (Required).
      - Repository: Name of the repository (Required).
      - Root Directory: Path that will be used as the repository root for this Data Product. By default, the value would be **"."**.
      
      After filling in all fields with appropriate fields, your page should look like the one shown below. Click on the **"Next Step"** button to move to next section.

      <img src="./images/ChooseLocationMWAA.png">

4. In the **"Review and Create"** section, all the previously filled data would be present through which we can cross-check the information once again. If you are satisfied, then proceed to create a Data Product by clicking on **"Create"** button present in the bottom-right of the section. Otherwise, you can go back to the previous sections by clicking on **"Back"** button.

<img src="./images/ReviewMWAA.png">

After clicking on "Create" button, the process of creating a Data Product will be initiated which would be done in 3 phases (Fetching Skeleton+Template, Publish and Register). If there aren't any errors in entering the information, all the 3 phases will be successful and will give you the links to the newly created Repository and the component in the Catalog.

5. After the previous steps are completed, Workload is created and attached to the corresponding Data Product in the **"Workloads"** section which is shown below:

<img src="./images/CreatedMWAAinDP.png">

6. When you click on the name of the workload, you would be able to see the details of the workload that is created.

<img src="./images/CreatedMWAA.png">