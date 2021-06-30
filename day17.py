# Creating a connection for DB and printing the version
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123"
)

print(mydb)
import sys

cur = mydb.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("DBMS Version :", str(data))

# Creating multiple tables & inserting data
dbse = mydb.cursor()
dbse.execute("SHOW DATABASES")
for i in dbse:
    print(i)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="mydatabase"
)
dbse = mydb.cursor()
dbse.execute("CREATE TABLE customers (Employee_name VARCHAR(255), Employee_dep VARCHAR(255), Employee_id VARCHAR(255))")
dbse = mydb.cursor()
dbse.execute("SHOW TABLES")
for k in dbse:
    print(k)

dbse = mydb.cursor()

dbse.execute("CREATE TABLE Office (emp_name VARCHAR(255), Employee_id VARCHAR(255) ,EMP_ADDRESS VARCHAR(255))")

dbse = mydb.cursor()
dbse.execute("CREATE TABLE Student (rollno INT(24) , STUD_NAME VARCHAR(255) , MARK INT(3))")

dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for j in dbse:
    print(j)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="mydatabase"
)

dbse = mydb.cursor()
sql = "INSERT INTO customers(Employee_name, Employee_dep,Employee_id) VALUES (%s,%s,%s)"
val = ("ABC", "D1", "100")
dbse.execute(sql, val)
mydb.commit()

print(dbse.rowcount, "Record Inserted in customer Table")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="mydatabase"
)

dbse = mydb.cursor()
sql = "INSERT INTO Office (emp_name, Employee_id ,EMP_ADDRESS) VALUES (%s,%s,%s)"
val = ("Jay", "101", "xyz")
dbse.execute(sql, val)
mydb.commit()

print(dbse.rowcount, "Record Inserted in Office Table")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="mydatabase"
)

dbse = mydb.cursor()
sql = "INSERT INTO Student (rollno, STUD_NAME ,MARK) VALUES (%s,%s,%s)"
val = ("60", "Poh", "96")
dbse.execute(sql, val)
mydb.commit()

print(dbse.rowcount, "Record Inserted in Student table")

# Creating a employee table and reading all the employee name in the table using for loop
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="mydatabase"
)
dbse = mydb.cursor()
dbse.execute("CREATE TABLE Employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="mydatabase"
)

dbse = mydb.cursor()
sql = "INSERT INTO Employee (id, name ,address) VALUES (%s,%s,%s)"
val = [
    ('1', 'A', 'QWE 4'),
    ('2', 'B', 'ASD 57'),
    ('3', 'C', 'KLM 881'),
    ('4', 'D', 'MNO 345'),
    ('5', 'E', 'XYZ 22'),
]
dbse.executemany(sql, val)
mydb.commit()

print(dbse.rowcount, "Record Inserted in Employee table")

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="mydatabase"
)

dbse = mydb.cursor()
dbse.execute("SELECT * FROM Employee")

result = dbse.fetchall()
for x in result:
    print(x)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="mydatabase"
)

dbse = mydb.cursor()
dbse.execute("SELECT name FROM Employee")

result = dbse.fetchall()
for x in result:
    print(x)
