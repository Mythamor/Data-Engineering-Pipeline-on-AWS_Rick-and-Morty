# Data-Engineering-Pipeline-on-AWS: Rick-and-Morty-API

This project is a data engineering pipeline that extracts data from the Rick and Morty API https://rickandmortyapi.com/api/.

## Overview

In this Masterclass, we utilized data engineering skills to build an analytics workload on the AWS Cloud platform. The project involved extracting data from the Rick and Morty series API, transforming it, and modeling it to load into a data warehouse. This data was modeled based on the ERD diagram provided. Although we used MySQL in this illustration, the concepts are applicable to any database system.


## Endpoints

The pipeline interacts with the following Rick and Morty API endpoints:

1. **Characters**: https://rickandmortyapi.com/api/character
   - Contains information about characters in the Rick and Morty universe.
3. **Episodes**:   https://rickandmortyapi.com/api/episode
   - Contains details about episodes, including their titles, air dates, and characters involved.
5. **Locations**:  https://rickandmortyapi.com/api/location
   - Provides data on various Rick and Morty universe locations, including their type and dimension.


## Learning Objectives

1. Design a sample real-world data platform on AWS.
2. Create an architecture diagram.
3. Ingest data from a REST API using Python in AWS Lambda.
4. Stage data using AWS Simple Storage Service (S3).
5. Build a MySQL-based data warehouse using Aiven.
6. Schedule jobs using AWS EventBridge.
7. Query the modeled data in the warehouse.

## Workload Requirements

1. **Data Ingestion in Near Real-Time:** Utilize AWS Lambda for lightweight compute tasks to run Python scripts.
2. **Data Staging:** Store data using AWS S3.
3. **Data Warehousing:** Load the data into a MySQL database hosted on Aiven.
4. **Data Visualization:** Visualize the data as needed.
5. **Automation:** Connect and automate all stages using AWS EventBridge.
6. **Data Querying:** Use SQL client applications to run queries and answer analytics questions.


## Data Ingestion

### A. Working with AWS Lambda

We extracted Rick & Morty data from an open-source API using AWS Lambda for ETL processes.

1. **Set Up AWS Lambda:**
    - Go to the AWS Management Console and search for AWS Lambda, ensuring you're in the ***Ireland Region (eu-west-1)***.
    - Create a new Lambda Function with the following settings:
        - Author From Scratch
        - Runtime: **Python 3.12**
        - Architecture: **x86_64**
        - Execution Role: ***Create a new role with basic Lambda permissions***

2. **Add Python Libraries:**
    - To use Pandas for data wrangling, add a Layer:
        - Scroll to the Layers section and click **Add a Layer**.
        - Choose **AWS Layer**.
        - Select **AWSSDKPandas-Python311** from the drop-down and choose the latest version.

3. **Configure Lambda:**
    - Create a Python file named ***s3_file_operations.py*** in the Lambda project folder. You can find the script under the **utils** folder in this repository.
    - Increase the Timeout Limit in the ***Configuration*** section to 15 minutes.
    - Attach the ***AmazonS3FullAccess*** policy to the Lambda execution role.

### B. Creating an S3 Bucket

1. **Set Up S3 Bucket:**
    - Navigate to AWS S3 in the AWS Management Console.
    - Create a new bucket with a unique name (e.g., ***de-masterclass-XX***).
    - Disable ACLs, turn off ***Block all Public Access*** (not recommended), enable Versioning, and set Encryption to ***Server-side encryption with Amazon S3 managed keys (SSE-S3)***.
    - Create a folder named **Rick&Morty** within the bucket.

### C. Creating an Aiven MySQL Database

1. **Set Up Aiven MySQL Database:**
    - Navigate to the Aiven console and create a new MySQL service.
    - Choose the latest version and select an appropriate plan.
    - Configure settings such as the database name (`rick_and_morty`), username (`admin`), and password.
    - Note the endpoint address for connecting Lambda functions to the database.

2. **Configure Database Access:**
    - Ensure that your Lambda function can access the Aiven MySQL database by configuring the necessary security settings.

### D. Connecting Everything Together

We created three Lambda functions for the ETL process:

1. **Extraction Lambda Function:**
    - Extracts data from the Rick and Morty API and saves it to the S3 bucket.
    - Refer to `Rick_and_Morty_Extraction.py` for implementation.

2. **Transformation Lambda Function:**
    - Reads raw data from S3, applies transformations, and saves it back to S3.
    - Refer to `Rick_and_Morty_Transformation.py` for implementation.

3. **Loading Lambda Function:**
    - Reads transformed data from S3 and loads it into the Aiven MySQL database.
    - Refer to `Rick_and_Morty_Loading.py` for implementation.

### Testing the Pipeline

1. **Test the Extraction Lambda Function:** Ensure it extracts data from the API and saves it to S3.
2. **Test the Transformation Lambda Function:** Ensure it transforms and saves data correctly.
3. **Test the Loading Lambda Function:** Ensure it loads transformed data into the Aiven MySQL database.


## Prerequisites

- **Python 3.x**
- **AWS CLI configured with appropriate S3 access**
- **Python packages**: `requests`, `pandas`, `boto3`, `tqdm`, `sqlalchemy`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Mythamor/rick-and-morty-pipeline.git
   cd rick-and-morty-pipeline
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure your AWS credentials for S3 access:

   ```bash
   aws configure
   ```

## Usage

1. **Run the Pipeline**:
   - Execute the main script to start the data extraction, transformation, and loading process:

     ```bash
     python main.py
     ```

2. **Monitor Progress**:
   - The script provides real-time feedback via a progress bar, showing the extraction status of each page of data from the API.

3. **Check Output**:
   - After completion, the CSV files will be available in your specified S3 bucket, organized by endpoint.

## Future Enhancements

- **Automation**: Set up the pipeline to run on a schedule using AWS Lambda or an EC2 instance.
- **Data Validation**: Implement additional checks to validate data consistency before loading.
- **Enhanced Transformation**: Add more complex data transformations, such as aggregations and derived metrics.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Mithamo Beth
