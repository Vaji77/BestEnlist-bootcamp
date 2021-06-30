# Creating a DB with doctor ID & patients visited
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123"
)
print(mydb)

dbse = mydb.cursor()
dbse.execute("CREATE DATABASE Doctor")
dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
  print(entry)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="Doctor"
)

dbse = mydb.cursor()
dbse.execute("CREATE TABLE Doctors(dr_name VARCHAR(255),dr_id VARCHAR(255), Patient_visited VARCHAR(255))")
dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for i in dbse:
  print(i)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="Doctor"
)

dbse = mydb.cursor()

sql = "INSERT INTO Doctors (dr_name,dr_id , Patient_visited) VALUES (%s,%s,%s)"
val = [
    ('Jay', 'D1', '10'),
    ('Raj', 'D2', '3'),
    ('Mahadev', 'D3', '0'),
    ('Noora', 'D4', '8'),
    ('Sarah', 'D5', '0'),
    ('Rachith', 'D6', '8'),
    ('Sahid', 'D7', '0'),
    ('Neha', 'D8', '20'),
    ('Benny', 'D9', '6'),
    ('Lekshmi', 'D10', '2'),
    ('Sonam', 'D11', '11'),
    ('Krish', 'D12', '9'),
    ('Sidharth', 'D13', '0'),
    ('Punya', 'D14', '4'),
    ('Ravi', 'D15', '0'),
    ('Sreedevi', 'D16', '9')
]

dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, "Record Inserted in Doctor Table")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="Doctor"
)
mycursor = mydb.cursor()
print("Rows Entered:")
mycursor.execute("SELECT * FROM Doctors")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



# Getting the doctor(s) who have more than 5 patients visited
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="Doctor"
)
mycursor = mydb.cursor()
print("Doctors with more than 5 visited patients:")
mycursor.execute("SELECT dr_name FROM Doctors where Patient_visited > 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



# Getting the doctor(s) with no patients visit
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="My_sqlprofile@123",
    database="Doctor"
)

mycursor = mydb.cursor()
print("Doctors with no patient visits:")
mycursor.execute("SELECT dr_name FROM Doctors where Patient_visited = 0")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)