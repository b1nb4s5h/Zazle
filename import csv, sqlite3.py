# Import required modules
import csv
import sqlite3
import os
import sys
import os.path

# Connecting to the geeks database
connection = sqlite3.connect('tlds.db')

# Creating a cursor object to execute
# SQL queries on a database table
cursor = connection.cursor()

# Table Definition
create_table = '''CREATE TABLE tld(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				tld TEXT NULL);
				'''

# Creating the table into our
# database
cursor.execute(create_table)

# Opening the person-records.csv file

file = open('tlds.csv')

# Reading the contents of the
# person-records.csv file
contents = csv.reader(file)

# SQL query to insert data into the
# person table
insert_records = "INSERT INTO tld (tld) VALUES(?)"

# Importing the contents of the file
# into our person table
cursor.executemany(insert_records, contents)



# Committing the changes
connection.commit()

# closing the database connection
connection.close()
