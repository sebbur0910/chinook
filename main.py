# Try some initial DB commands
import sqlite3

# Select the employees
conn = sqlite3.connect("chinook.db")
cursor = conn.cursor()
query = "SELECT FirstName, LastName, Title FROM employees"
cursor.execute(query)
employees = cursor.fetchall()


# Print out the first employee
print(employees[0])

# Insert a new genre
query = 'INSERT INTO genres (Name) values ("Funk");'
cursor.execute(query)
# Before a change is written to the database, it must be committed
conn.commit()


# Close the connection at the end
conn.close()

