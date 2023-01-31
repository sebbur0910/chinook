import sqlite3
conn = sqlite3.connect("chinook.db")
cursor = conn.cursor()

get_question_1 = """
SELECT FirstName, LastName, address
FROM CUSTOMERS
"""
cursor.execute(get_question_1)
question_1 = cursor.fetchall()

get_question_2 = """
SELECT tracks.Name
FROM tracks JOIN media_types mt on tracks.MediaTypeId = mt.MediaTypeId
WHERE mt.Name LIKE "Protected AAC audio file"
"""
cursor.execute(get_question_2)
question_2 = cursor.fetchall()

get_question_3 = """
SELECT employees.FirstName, employees.LastName
FROM employees JOIN employees em on employees.ReportsTo = em.EmployeeId
WHERE em.LastName LIKE "Edwards" AND em.FirstName LIKE "Nancy"
"""
cursor.execute(get_question_3)
question_3 = cursor.fetchall()

question_4 = """
INSERT INTO media_types (Name) values ("Windows Media Audio"), ("FLAC audio file")

"""
cursor.execute(question_4)
conn.commit()

conn.close()