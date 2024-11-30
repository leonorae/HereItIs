#!/usr/bin/python3
"""
This script connects to the database and prints all data from
the Artist, Venue, and Event tables.

Author: HereItIs Group
Date: 2024-11-12
"""

import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect("postgresql://mohammed_db_user:UmSc7JQQWVM3IqL8sbwxtGBI8I4cINRV@dpg-csj5d6btq21c73d9b840-a.oregon-postgres.render.com/mohammed_db")
print("Database Connection Successful")
cur = conn.cursor()

# Define a function to fetch and print all records from a specified table
def print_table_data(table_name):
    print(f"\nAll data in {table_name} table:")
    try:
        cur.execute(f'SELECT * FROM {table_name};')
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"An error occurred while retrieving data from {table_name}: {e}")

# Print all data in each table
tables = ['Artist', 'Venue', 'Event']
for table in tables:
    print_table_data(table)

# Close the cursor and connection
cur.close()
conn.close()