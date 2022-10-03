import sqlite3

connection = sqlite3.connect("sqlite.db")
cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS temperaturation (
    data INTEGER
    degrees INTEGER
    
    )""")


connection.commit()
connection.close()