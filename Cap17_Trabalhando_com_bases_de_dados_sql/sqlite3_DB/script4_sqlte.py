# importing the module
import sqlite3
  
# connect withe the myTable database
conn = sqlite3.connect("myTable.db")
  
# cursor object
cur = conn.cursor()
  

# CRUD - DELETE
cur.execute("DELETE from emp where staff_number='2' ") 
conn.commit()


# CRUD - RETRIEVING
cur.execute("SELECT * FROM emp") 

registers = cur.fetchall() 

for person in registers:
    print(person)