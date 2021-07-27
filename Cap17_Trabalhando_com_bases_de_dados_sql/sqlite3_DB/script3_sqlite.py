# importing the module
import sqlite3
  
# connect withe the myTable database
conn = sqlite3.connect("myTable.db")
  
# cursor object
cur = conn.cursor()
  

# CRUD - UPDATE
cur.execute("UPDATE emp SET lname = 'Reis Classo' where staff_number='1' ") 
conn.commit()


# CRUD - RETRIEVING
cur.execute("SELECT * FROM emp") 

registers = cur.fetchall() 

for person in registers:
    print(person)