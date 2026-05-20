# importer module for loading csv data

import pandas as pd
import os
from database import *

# the pathm for thje csv file 
CSV_FILE = "data/incidents.csv"

def import_csv_data():
    print(f"\nLoading data from {CSV_FILE}...")

    if not os.path.exists(CSV_FILE):
        print(f"Error: File {CSV_FILE} not found!")
        print("Make sure the data folder exists and has the csv file")
        return False

    try:
        df = pd.read_csv(CSV_FILE)
        print(f"Found {len(df)} rows in the csv file")

        # drop rows with missing values so the insert dosent break
        df = df.dropna()

        # clean the text columns a bit
        df['category'] = df['category'].str.strip().str.title()
        df['status'] = df['status'].str.strip().str.title()
        df['priority'] = df['priority'].str.strip().str.title()

        data_list = []
        for index, row in df.iterrows():
            data_list.append((
                int(row['id']),
                str(row['date']),
                str(row['category']),
                str(row['status']),
                str(row['priority']),
                str(row['description'])
            ))

        print("Clearing old data from database...")
        clear_table()

        print("Inserting new data...")
        if insert_many_incidents(data_list):
            print(f"Successfully imported {len(data_list)} incidents!")
            return True
        else:
            print("Error inserting data into database")
            return False

    except Exception as e:
        print(f"Error importing data: {e}")
        return False


