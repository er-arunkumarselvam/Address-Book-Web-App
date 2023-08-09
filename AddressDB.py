import sqlite3
connection = sqlite3.connect("addressbook.db")
print("Database opened successfully")
cursor = connection.cursor()
#delete
cursor.execute('''DROP TABLE Address;''')
connection.execute("create table Address (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, address TEXT NOT NULL, city TEXT NOT NULL, pincode TEXT NOT NULL, mobile TEXT NOT NULL, email TEXT UNIQUE NOT NULL)")
print("Table created successfully")
connection.close()   