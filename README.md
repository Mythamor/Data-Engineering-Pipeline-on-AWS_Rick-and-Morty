# Data-Engineering-Pipeline-on-AWS: Rick-and-Morty-API

This project is a data engineering pipeline that extracts data from the Rick and Morty API https://rickandmortyapi.com/api/, processes it, and loads the results into individual CSV files. These files are then stored in an AWS S3 bucket for further analysis or use.

## Features

- **Data Extraction**: Extract data from three Rick and Morty API endpoints: Characters, Episodes, and Locations.
- **Data Transformation**: Clean and structure the data to ensure consistency and usability.
- **Data Loading**: Save the transformed data as individual CSV files and upload them to an S3 bucket on AWS.

## Endpoints

The pipeline interacts with the following Rick and Morty API endpoints:

1. **Characters**: https://rickandmortyapi.com/api/character
                   Contains information about characters in the Rick and Morty universe.
3. **Episodes**:   https://rickandmortyapi.com/api/episode
                   Contains details about episodes, including their titles, air dates, and characters involved.
5. **Locations**:  https://rickandmortyapi.com/api/location
                   Provides data on various Rick and Morty universe locations, including their type and dimension.

## Pipeline Overview

1. **Data Extraction**:
   - Fetch data from each API endpoint using Python requests.
   - Paginate through all available data to ensure completeness.
  
2. **Data Transformation**:
   - Process and clean the data to handle missing values, normalize data formats, and extract useful information (e.g., episode numbers, location IDs).
   - Structure the data into well-defined columns suitable for analysis.
  
3. **Data Loading**:
   - Save the transformed data as CSV files.
   - Upload each CSV file to a designated S3 bucket on AWS.

## Prerequisites

- **Python 3.x**
- **AWS CLI configured with appropriate S3 access**
- **Python packages**: `requests`, `pandas`, `boto3`, `tqdm`, `sqlalchemy`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/rick-and-morty-pipeline.git
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
