import psycopg2
import csv
from tabulate import tabulate

conn = psycopg2.connect(dbname="seconddb",
    user="neondb_owner",
    password="npg_qsSHdPejW1i5",
    host="ep-sparkling-rain-a4aj55uv-pooler.us-east-1.aws.neon.tech")
cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        user_id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        surname VARCHAR(255) NOT NULL, 
        phone VARCHAR(255) NOT NULL UNIQUE
    )
""")

# ILIKE-safe query columns
valid_columns = ["name", "surname", "phone"]

def insert_data():
    print('Type "csv" or "con" to choose option between uploading csv file or typing from console: ')
    method = input().lower()
    if method == "con":
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        cur.execute("CALL insert_or_update_user(%s, %s, %s);", (name, surname, phone))
    elif method == "csv":
        filepath = input("Enter a file path with proper extension: ")
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                cur.execute("CALL insert_or_update_user(%s, %s, %s);", tuple(row))
    conn.commit()

def update_data():
    column = input('Type the name of the column that you want to change (name/surname/phone): ').lower()
    if column not in valid_columns:
        print("Invalid column.")
        return
    value = input(f"Enter {column} that you want to change: ")
    new_value = input(f"Enter the new {column}: ")
    cur.execute(f"UPDATE phonebook SET {column} = %s WHERE {column} = %s", (new_value, value))
    conn.commit()

def delete_data():
    identifier = input('Type first name or phone number to delete: ')
    cur.execute("CALL delete_user(%s);", (identifier,))
    conn.commit()

def query_data():
    column = input("Search by column (name/surname/phone): ").lower()
    if column not in valid_columns:
        print("Invalid column.")
        return
    value = input(f"Search pattern for {column}: ")
    cur.execute(f"SELECT * FROM phonebook WHERE {column} ILIKE %s;", ('%' + value + '%',))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))

def display_data():
    cur.execute("SELECT * FROM phonebook;")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

def paginate_data():
    limit = int(input("Enter limit (number of rows): "))
    offset = int(input("Enter offset (starting from 0): "))
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

while True:
    print("""
    List of the commands:
    1. Type "i" or "I" to INSERT data.
    2. Type "u" or "U" to UPDATE data.
    3. Type "q" or "Q" to QUERY data.
    4. Type "d" or "D" to DELETE data.
    5. Type "s" or "S" to SHOW all data.
    6. Type "p" or "P" to PAGINATE through data.
    7. Type "f" or "F" to FINISH the program.
    """)

    command = input().lower()

    if command == "i":
        insert_data()
    elif command == "u":
        update_data()
    elif command == "d":
        delete_data()
    elif command == "q":
        query_data()
    elif command == "s":
        display_data()
    elif command == "p":
        paginate_data()
    elif command == "f":
        break

cur.close()
conn.close()