import sqlite3

##Connect to sqlite
connection = sqlite3.connect("student.db")

##Create a curosr object to insert record ,create table, retrieve
cursor = connection.cursor()

##create the table
table_info ="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);


"""
cursor.execute(table_info)

## Insert Some more records

cursor.execute('''Insert Into STUDENT values('Krish','Science','A','90')''')
cursor.execute('''Insert Into STUDENT values('Adam','Science','B','')''')
cursor.execute('''Insert Into STUDENT values('Sam','Science','C','86')''')
cursor.execute('''Insert Into STUDENT values('Vicky','Dev','D','50')''')
cursor.execute('''Insert Into STUDENT values('Dan','Algebra','A','40')''')

##Display all the records
print("The inserted records are")

data = cursor.execute("""Select * From STUDENT""")
for row in data:
    print(row)

connection.commit()
connection.close()