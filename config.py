# config file for settings

import os

DB_FILE = "dashboard.db"

DATA_FOLDER = "data"
CSV_FILE = "data/incidents.csv"

OUTPUT_FOLDER = "output"

def setup_folders():
    """create the folders if they dont exist"""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
        print(f"Created {DATA_FOLDER} folder")
    
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"Created {OUTPUT_FOLDER} folder")
