import sqlite3
con=sqlite3.connect("database.db")
cursor=con.cursor()
q1= "SELECT * from seller2"
cursor.execute(q1)
result = cursor.fetchall()
print(result)
con.close()