# Python code to demonstrate table creation and 
# insertions with SQL

import sqlite3

# connecting to the database 
connection = sqlite3.connect("myTable.db")

# cursor 
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE emp ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(30), 
lname VARCHAR(50), 
gender CHAR(1), 
birth DATE,
job VARCHAR(100));"""
  
# execute the statement
crsr.execute(sql_command)

# SQL command to insert the data in the table

sql_command = """INSERT INTO emp VALUES (1, "Fabio", "Classo", "M", "1974-11-25", "Software Engineer");"""
crsr.execute(sql_command)


# insert more data in the table
sql_command = """INSERT INTO emp VALUES (2, "Michael", "Joseph Jackson", "M", "1959-08-29", "Pro Basketball Player");"""
crsr.execute(sql_command)

sql_command = """INSERT INTO emp VALUES (3, "Donald", " John Trump", "M", "1946-06-14", "USA President");"""
crsr.execute(sql_command)

sql_command = """INSERT INTO emp VALUES (4, "Michael", "Jeffrey Jordan", "M", "1963-02-17", "Musician");"""
crsr.execute(sql_command)
  

# To save the changes in the files. Never skip this. 
# If we skip this, nothing will be saved in the database.
connection.commit()
  
# close the connection
connection.close()



# https://www.geeksforgeeks.org/sql-using-python/