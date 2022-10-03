import sqlite3

connection = sqlite3.connect("data.sl3", 5)
cur = connection.cursor()
#cur.execute("CREATE TABLE Temp_Date_3 (Id INTEGER NOT NULL PRIMARY KEY,Temperature TEXT, Date TEXT)")
cur.execute("INSERT INTO Temp_Date_3 (Id, Date, Temperature) VALUES ('7', '09.10.2022', '16°C')")

connection.commit()
connection.close()