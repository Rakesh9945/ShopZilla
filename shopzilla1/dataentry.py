import sqlite3
con=sqlite3.connect("database.db")
cursor=con.cursor()
q1='''INSERT INTO order_ack1(userId)  VALUES(1)'''
cursor.execute(q1)
con.commit()