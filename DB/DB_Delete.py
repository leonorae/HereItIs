#!/usr/bin/python3
"""
This module deletes the tables in the database.

Author: HereItIs Group
Date: 2024-11-12

"""

import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect("postgresql://mohammed_db_user:UmSc7JQQWVM3IqL8sbwxtGBI8I4cINRV@dpg-csj5d6btq21c73d9b840-a.oregon-postgres.render.com/mohammed_db")
print("Database Connection Successful")
cur = conn.cursor()

# Drop tables if they exist
tables = ['Event', 'Venue', 'Artist']
for table in tables:
    cur.execute(f"DROP TABLE IF EXISTS {table} CASCADE;")
    print(f"Table '{table}' has been dropped.")

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
print("All tables deleted successfully.")
