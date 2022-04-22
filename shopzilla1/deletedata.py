import sqlite3
con=sqlite3.connect("database.db")
cursor=con.cursor()
q1= "delete from kart where userId=1"
cursor.execute(q1)
con.commit()