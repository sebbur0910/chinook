# Try some initial DB commands
import sqlite3

# Select the employees
conn = sqlite3.connect("chinook.db")
cursor = conn.cursor()
query = "SELECT FirstName, LastName, Title FROM employees"
cursor.execute(query)
employee_1 = cursor.fetchone()
employees_2_3 = cursor.fetchmany(2)
employees_rest = cursor.fetchall()

# Print out employees
print(employee_1)
print(employees_2_3)
print(employees_rest)

# Insert a new genre
query = 'INSERT INTO genres (Name) values ("Funk");'
cursor.execute(query)
# Before a change is written to the database, it must be committed
#conn.commit()

# Close the connection at the end
conn.close()
