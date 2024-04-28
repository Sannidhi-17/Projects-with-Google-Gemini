import sqlite3

## connect to sqlite
connection = sqlite3.connect("student.db")

## create a cursor
cursor = connection.cursor()

## create tables
table_info = """
Create table STUDENT(NAME VARCHAR(32), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

## insert some records
cursor.execute(''' Insert into STUDENT values('Sannidhi', 'Data Science', 'A', 90)''')
cursor.execute(''' Insert Into STUDENT values('manan' , 'Mechanical', 'C', 75)''')

## Display all the records
print("The inserted records are")
data = cursor.execute("Select * from STUDENT")

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()
