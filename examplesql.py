import sqlite3

# Establish connection and cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
"""
#add only one tuple
cursor.execute("INSERT INTO events VALUES ('Buchel', 'Buchelcity', '2023.11.01')")
connection.commit()
result = cursor.fetchall()
# print(result)

# query all rows
cursor.execute("SELECT * FROM events WHERE date='2023.11.01'")
result = cursor.fetchall()
#print(result)

# query some rows
cursor.execute("SELECT band, city FROM events WHERE date='2023.11.01'")

#print(result)
# Inserting new rows
newrows = [('Lion', 'Liocity', '2023.12.01'),
           ('Eagle', 'Eaglecity', '2023.12.01')]

cursor.executemany("INSERT INTO events VALUES (?,?,?)", newrows)
connection.commit()

cursor.execute("SELECT * FROM events ")
result = cursor.fetchall()
print(result)
"""
# cursor.execute("DELETE FROM events ")
# connection.commit()
# result = cursor.fetchall()
# print(result)
#
# newrows = [('Lion', 'Liocity', '2023.12.01'),
#            ('Eagle', 'Eaglecity', '2023.12.01')]
#
# cursor.executemany("INSERT INTO events VALUES (?,?,?)", newrows)
connection.commit()
cursor.execute("SELECT * FROM events ")
result = cursor.fetchall()
print(result)