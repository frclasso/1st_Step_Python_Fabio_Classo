# Python code to demonstrate SQL to fetch data.
  
# importing the module
import sqlite3
  
# connect withe the myTable database
conn = sqlite3.connect("myTable.db")
  
# cursor object
cur = conn.cursor()
  
# execute the command to fetch all the data from the table emp
cur.execute("SELECT * FROM emp") 
  
# CRUD - RETRIEVING
registers = cur.fetchall() 
print()
print(registers)
print()

for person in registers:
    print(person)

# https://www.geeksforgeeks.org/sql-using-python/