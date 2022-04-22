from flask import *
import sqlite3

app = Flask(__name__)
def getLoginDetails():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        if 'email' not in session:
            loggedIn = False
            firstName = ''
            noOfItems = 0
        else:
            loggedIn = True
            cur.execute("SELECT userId, firstName FROM users WHERE email = ?", (session['email'], ))
            userId, firstName = cur.fetchone()
            cur.execute("SELECT count(productId) FROM kart WHERE userId = ?", (userId, ))
            noOfItems = cur.fetchone()[0]
    conn.close()
    return (loggedIn, firstName, noOfItems)




@app.route("/")
def home():
    loggedIn, firstName, noOfItems = getLoginDetails()
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT productId, name1, price1, description1, image1, stock1 FROM featured')
        itemData = cur.fetchall()


        cur.execute('SELECT categoryId, name FROM categories')
        categoryData = cur.fetchall()

    return render_template('home.html',itemData =itemData,loggedIn=loggedIn, firstName=firstName, noOfItems=noOfItems,categoryData=categoryData)


if __name__ == '__main__':
    app.run(debug=True)