import sqlite3

connection = sqlite3.connect("akwarium.db")
cursor = connection.cursor()
rows = cursor.execute("SELECT name,species,tank_number FROM fish").fetchall()
rows2 = cursor.execute("SELECT name,species,tank_number FROM fish WHERE name = 'Nemo'").fetchall()
print(rows)
print(rows2)