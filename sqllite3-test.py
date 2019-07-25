import sqlite3

conn =  sqlite3.connect('mycompany.db')
curObj = conn.cursor()

#Create TABLE only once not every time
curObj.execute("CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT, postion TEXT)")
conn.commit()

curObj.execute("INSERT INTO employees VALUES(1,'Mike', 75000, 'Python', 'Software Developer')")
conn.commit()  #commit is neceassary when ur modifiing anything in the db

#the ? and tuple method helps to prevent SQL injection attacks.
curObj.execute("INSERT INTO employees VALUES(?,?,?,?,?)",(1,'Jake',50000,'JS','Tester'))
conn.commit()

curObj.execute("SELECT * FROM employees")
results = curObj.fetchall()
print(results)		#will give a list of all records aka [ (1,'Mike', 75000, 'Python', 'Software Developer') , (1,'Jake',50000,'JS','Tester')]


curObj.execute("SELECT name FROM employees WHERE salary > 50000")
results = curObj.fetchall()
print(results)   # [ ('Mike') ]



curObj.execute("DELETE FROM employees")
curObj.commit()    #deletes all records from table employees

curObj.execute("DELETE FROM employees WHERE name=?", ("Jake"))
conn.commit()



curObj.close()
conn.close()
