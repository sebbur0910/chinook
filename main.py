# Try some initial DB commands
import sqlite3

# Select the employees
conn = sqlite3.connect("chinook.db")
cursor = conn.cursor()
query = "SELECT FirstName, LastName, Title FROM employees"
cursor.execute(query)
employees = cursor.fetchall()
conn.close()

# Print out the first employee
print(employees[0])
