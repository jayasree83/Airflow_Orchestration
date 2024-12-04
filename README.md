# Workflow Orchestration - Building End-to-End Data Pipeline and Analysis Using AWS

# Project Overview
The goal of this project is to build an end-to-end data pipeline that securely connects, manages, streamlines, and analyzes data generated from the Rapid API. The pipeline extracts data for a given location in JSON format, transforms it, and stores it in an AWS for further analysis. The entire workflow is orchestrated in Airflow which is set up in virtual environment on EC2 instance. This repository contains an Airflow Directed Acyclic Graph (DAG) designed to automate the process of fetching property data from the Rapid API, processing it, and loading it into Amazon S3 and Redshift for further analysis. The DAG defines an end-to-end workflow, starting from extracting data via API requests to performing checks and loading the data into AWS S3 and Redshift for analytical purposes.

![image](https://github.com/user-attachments/assets/2c26e33a-a44d-456c-99e2-1f0472ed45ab)

# Access Airflow 
Airflow is in a virtual environment on EC2 instance. Once airflow is installed, it gives user credentials to login to airflow.

![image](https://github.com/user-attachments/assets/9b9d445a-d95e-4950-9a02-a170d1720710)

Airflow can be launched with "instance-ipaddress":8080 (or a port that is configured in inbound rules)

![image](https://github.com/user-attachments/assets/5313922e-9e13-475e-a3f7-380c994b9458)


![image](https://github.com/user-attachments/assets/493c7d78-1576-4765-b735-c136eda0ab35)


# Folder Structure
![image](https://github.com/user-attachments/assets/5d1bd832-0799-4559-8b0d-d9457784d34f)

# DAG Overview
- Extract Data: Fetch property listing data from the Zillow API.
- Load Data to S3: Upload the extracted JSON data to an S3 bucket for storage.
- Check File Presence in S3: Ensure that the file has been successfully uploaded to S3.
- Transfer Data to Redshift: Load the data from S3 into an Amazon Redshift table for further querying and analysis.
The workflow is orchestrated by Apache Airflow, which provides a rich set of features for scheduling, monitoring, and managing the tasks involved in the data pipeline.

# Configuration
1. **API Configuration**
- The api_config.json file should contain your API key and host for the Rapid API. It will be used to authenticate API requests.
2. **IAM**
- IAM users, roles, policies must be defined and assigned properly between AWS services
3. **AWS S3**
- Ensure AWS credentials are configured on the machine or EC2 instance where this DAG is running. You can use the aws configure command or set up an IAM role with the necessary permissions.
4. **AWS Redshift**
- Ensure a Redshift cluster is set up and that the necessary AWS Redshift connection is configured in Airflow (conn_id_redshift).
5. **AWS EC2** 
- EC2 instance (**T2 Medium**) is required for setting up airflow. Other smaller instances do not support Airflow.
6. **AWS Lambda**
- All the Lambda functions in between need proper configurations and triggers set up. Pandas Layer might be needed explicitly that can be set up from Lambda configurations.
  
  ![image](https://github.com/user-attachments/assets/9fdc55e6-d2dd-48ef-aa2a-bbf11847f4b9)


# Task Dependencies
The tasks are connected using the >> operator to define their execution order:
![image](https://github.com/user-attachments/assets/1a4533f6-7787-40f8-81af-ec6f9692ae9b)

# Error Handling
Errors can occur frequently, while setting up the DAGs, even with slight a blank space during configurations.
![image](https://github.com/user-attachments/assets/bbe511b6-1c15-4fa6-9213-6d207be7d70d)

**Retry Logic**: The task retries have been disabled (retries=0) to prevent any automatic retries in case of failure.
**Notifications**: Email notifications will be sent in case of failure or retry (if configured).


  
