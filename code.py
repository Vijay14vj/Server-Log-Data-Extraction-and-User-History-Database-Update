# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 18:03:22 2025

@author: vijay
"""

import re
import sqlite3
import pymongo
import pandas as pd
from datetime import datetime

#file path
LOG_FILE = "mbox.txt"
MONGO_URI = "mongodb://localhost:27017/"
SQLITE_DB = "user_history.db"

#extract email address and dates
def extract_email_dates(log_file):
    email_pattern = re.compile(r'From\s+(\S+@\S+)\s+(\w{3}\s\d{1,2}\s\d{4}\s\d{2}:\d{2}:\d{2})')
    extracted_data = []

    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:
            match = email_pattern.search(line)
            if match:
                email, date_str = match.groups()
                date_obj = datetime.strptime(date_str, "%b %d %Y %H:%M:%S")
                extracted_data.append({"email": email, "date": date_obj.strftime("%Y-%m-%d %H:%M:%S")})

    return extracted_data

# Extract data from log file
email_data = extract_email_dates(LOG_FILE)
print(f"Extracted {len(email_data)} records.")


#store in mongodb

def store_in_mongodb(data, db_name="log_data", collection_name="user_history"):
    client = pymongo.MongoClient(MONGO_URI)
    db = client[db_name]
    collection = db[collection_name]
    collection.insert_many(data)
    print(f"Inserted {len(data)} records into MongoDB.")

# Store extracted data in MongoDB
store_in_mongodb(email_data)

#load data into mongodb to SQLite
def load_to_sqlite(mongo_db="log_data", mongo_collection="user_history"):
    client = pymongo.MongoClient(MONGO_URI)
    db = client[mongo_db]
    collection = db[mongo_collection]

    records = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB’s _id
    df = pd.DataFrame(records)

    conn = sqlite3.connect(SQLITE_DB)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        date TEXT NOT NULL
    )
    """)

    df.to_sql("user_history", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

    print(f"Loaded {len(df)} records into SQLite.")

# Transfer data to SQLite
load_to_sqlite()

#run sql queries on SQLite

def run_queries():
    conn = sqlite3.connect(SQLITE_DB)
    cursor = conn.cursor()

    queries = {
        "Unique Emails": "SELECT DISTINCT email FROM user_history;",
        "Emails per Day": "SELECT date(date) AS day, COUNT(email) AS email_count FROM user_history GROUP BY day;",
        "First and Last Email Dates": """
            SELECT email, MIN(date) AS first_email, MAX(date) AS last_email 
            FROM user_history 
            GROUP BY email;
        """,
        "Emails by Domain": """
            SELECT SUBSTR(email, INSTR(email, '@')+1) AS domain, COUNT(email) 
            FROM user_history 
            GROUP BY domain;
        """
    }

    for desc, query in queries.items():
        print(f"\n{desc}:")
        for row in cursor.execute(query):
            print(row)

    conn.close()

# Execute Queries
run_queries()

#execute

if __name__ == "__main__":
    email_data = extract_email_dates(LOG_FILE)
    store_in_mongodb(email_data)
    load_to_sqlite()
    run_queries()


