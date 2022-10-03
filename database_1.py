import sqlite3

connection = sqlite3.connect("data.sl3", 5)
cur = connection.cursor()
#cur.execute("CREATE TABLE temperature (Temperature TEXT)")
cur.execute("INSERT INTO temperature (Temperature) VALUES ('аа')")

connection.commit()
connection.close()