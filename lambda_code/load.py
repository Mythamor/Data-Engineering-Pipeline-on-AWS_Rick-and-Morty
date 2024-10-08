import os
import json
import boto3
import pandas as pd
import numpy as np
import pymysql.cursors
import s3_file_operations as s3_ops
from dotenv import load_dotenv


load_dotenv(override=True)

# Define environmental variables
"""
HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
PORT = os.getenv("PORT")

bucket_name = os.getenv("BUCKET")
"""
# AWS Bucket
bucket_name="rick-and-morty-de"


def create_database():
    # Read transformed data from S3
    print("Reading transformed data from S3...")
    characters_df = s3_ops.read_csv_from_s3(bucket_name, 'Rick&Morty/Transformed/Character.csv')
    episodes_df = s3_ops.read_csv_from_s3(bucket_name, 'Rick&Morty/Transformed/Episode.csv')
    appearance_df = s3_ops.read_csv_from_s3(bucket_name, 'Rick&Morty/Transformed/Appearance.csv')
    location_df = s3_ops.read_csv_from_s3(bucket_name, 'Rick&Morty/Transformed/Location.csv')

    # Check if data is loaded successfully
    if characters_df is None or episodes_df is None or location_df is None:
        print("Error in loading data from S3")
        return {
            'statusCode': 500,
            'body': json.dumps('Error in loading data from S3')
        }

    print("Data loaded successfully from S3")

    # SQL to drop the table if it exists
    drop_table = "DROP TABLE IF EXISTS Characters, Episodes, Location, Appearance CASCADE"
    
    # SQL create table scripts
    create_character_table = """
        CREATE TABLE IF NOT EXISTS Characters (
            id INT NOT NULL PRIMARY KEY,
            name VARCHAR(255),
            status VARCHAR(255),
            species VARCHAR(255),
            type VARCHAR(255),
            gender VARCHAR(255),
            origin_id VARCHAR(255),
            location_id VARCHAR(255),
            image VARCHAR(255),
            url VARCHAR(255),
            created VARCHAR(255)
        ) ENGINE=INNODB;
    """

    create_episode_table = """
        CREATE TABLE IF NOT EXISTS Episodes (
            id INT NOT NULL PRIMARY KEY,
            name VARCHAR(255),
            air_date VARCHAR(255),
            episode VARCHAR(255),
            url VARCHAR(255),
            created VARCHAR(255)
        ) ENGINE=INNODB;
    """

    create_appearance_table = """
        CREATE TABLE IF NOT EXISTS Appearance (
            id INT NOT NULL PRIMARY KEY,
            episode_id INT,
            character_id INT
        ) ENGINE=INNODB;
    """

    create_location_table = """
        CREATE TABLE IF NOT EXISTS Location (
            id INT NOT NULL PRIMARY KEY,
            name VARCHAR(255),
            type VARCHAR(255),
            dimension VARCHAR(255),
            url VARCHAR(255),
            created VARCHAR(255)
        ) ENGINE=INNODB;
    """

    try:
        conn = pymysql.connect(host=HOST,
                               user=USER,
                               password=PASSWORD,
                               port=16148,
                               database=DATABASE,
                               cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        
        # Drop table if exists
        print("Dropping table if exists ...")
        cursor.execute(drop_table)
        print("Table dropped (if it existed)")
        

        # Create tables
        cursor.execute(create_character_table)
        cursor.execute(create_episode_table)
        cursor.execute(create_appearance_table)
        cursor.execute(create_location_table)

        # Insert data into Character_Table
        insert_data(cursor, conn, characters_df, "Characters")

        # Insert data into Episode_Table
        insert_data(cursor, conn, episodes_df, "Episodes")

        # Insert data into Appearance_Table
        insert_data(cursor, conn, appearance_df, "Appearance")

        # Insert data into Location_Table
        insert_data(cursor, conn, location_df, "Location")

        print("Data insertion completed successfully")

    except Exception as e:
        print("Exception: ", e)
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }

    return {
        'statusCode': 200,
        'body': json.dumps('Data transformation and upload successful')
    }
    
def get_table_columns(cursor, table_name):
        cursor.execute(f"SHOW COLUMNS FROM {table_name};")
        columns = [column['Field'] for column in cursor.fetchall()]
        return columns


def insert_data(cursor, conn, df, table_name):
    # Replace NaN values with None explicitly
    df = df.replace({np.nan: None})
    
    # Filter DataFrame columns to match the table schema
    table_columns = get_table_columns(cursor, table_name)  # You need to define this function
    df = df[table_columns]  # Keep only columns that exist in the table
    
    column_names = list(df.columns)
    for i, row in df.iterrows():
        placeholders = ','.join(['%s'] * len(column_names))
        sql_insert = f"INSERT INTO {table_name} ({','.join(column_names)}) VALUES ({placeholders});"
        data = tuple(row[column] for column in column_names)
        cursor.execute(sql_insert, data)
        conn.commit()



# Call the function to create the database
create_database()
