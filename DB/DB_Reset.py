#!/usr/bin/python3
"""
This module deletes all data inside the tables but keep the tables.

Author: HereItIs Group
Date: 2024-11-12

"""

import psycopg2

# Database connection setup
DB_URL = "postgresql://mohammed_db_user:UmSc7JQQWVM3IqL8sbwxtGBI8I4cINRV@dpg-csj5d6btq21c73d9b840-a.oregon-postgres.render.com/mohammed_db"


def get_db_connection():
    conn = psycopg2.connect(DB_URL)
    return conn

def reset_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        # Truncate tables to delete all data but keep table structures
        cur.execute("TRUNCATE TABLE Event, Venue, Artist RESTART IDENTITY CASCADE;")
        conn.commit()
        print("All tables reset successfully; data has been cleared and primary keys reset.")
    except Exception as e:
        conn.rollback()
        print("An error occurred while resetting tables:", e)
    finally:
        cur.close()
        conn.close()

# Call the function to reset the tables
reset_tables()
