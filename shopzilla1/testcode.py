import sqlite3

# Open database


def parse(data):
    ans = []
    i = 0
    while i < len(data):
        curr = []
        for j in range(7):
            if i >= len(data):
                break
            curr.append(data[i])
            i += 1
        ans.append(curr)
    return ans

categoryId =1
with sqlite3.connect('database.db') as conn:
    cur = conn.cursor()
    cur.execute(
        "SELECT products.productId, products.name, products.price, products.image, categories.name FROM products, categories WHERE products.categoryId = categories.categoryId AND categories.categoryId = ?",
        (categoryId,))
    data = cur.fetchall()
conn.close()
categoryName = data[0][4]
data = parse(data)

print(data)