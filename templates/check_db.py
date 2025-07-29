import sqlite3

# Connect to the database file
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Read all rows from the URL table
c.execute("SELECT * FROM urls")
rows = c.fetchall()

# Print each row
for row in rows:
    print(row)

conn.close()
