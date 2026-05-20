# database stuff for sqlite

import sqlite3

DB_NAME = "dashboard.db"

def get_connection():
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def setup_database():
    # makes the table if it isnt already there
    conn = get_connection()
    if conn is None:
        return False

    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            status TEXT NOT NULL,
            priority TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("Database setup complete")
    return True

def insert_incident(data):
    conn = get_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO incidents (id, date, category, status, priority, description) VALUES (?, ?, ?, ?, ?, ?)", data)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error inserting incident: {e}")
        return False

def insert_many_incidents(data_list):
    conn = get_connection()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO incidents (id, date, category, status, priority, description) VALUES (?, ?, ?, ?, ?, ?)", data_list)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error inserting incidents: {e}")
        return False

def clear_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM incidents")
    conn.commit()
    conn.close()
    print("Table cleared")

def run_query(query, params=()):
    conn = get_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        print(f"Error running query: {e}")
        return []

def get_count():
    result = run_query("SELECT COUNT(*) FROM incidents")
    if result:
        return result[0][0]
    return 0

