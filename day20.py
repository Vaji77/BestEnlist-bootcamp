import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="My_sqlprofile@123",
)

mycursor = mydb.cursor()
print(mydb)

dbse = mydb.cursor()

dbse.execute("CREATE DATABASE Employee_Mangement")
dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
    print(entry)



# Creating an Employee Table with employee name,employee ID & Salary
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="My_sqlprofile@123",
  database="employee_mangement"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE Employee (emp_id INT , EMP_NAME VARCHAR(255),EMP_SALARY DOUBLE )")

dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)

dbse = mydb.cursor()

dbse.execute("SHOW COLUMNS FROM Employee")

for value in dbse:
  print(value)

dbse = mydb.cursor()

sql = "INSERT INTO Employee (emp_id , EMP_NAME , EMP_SALARY) VALUES (%s,%s,%s)"
val = [
    ('1', 'ANU', '45000'),
    ('2', 'ADHI', '10000'),
    ('3', 'BADHRA', '75000'),
    ('4', 'CARL', '80000'),
    ('5', 'GAUTHAM', '40000'),
    ('6', 'HARISH', '70000'),
    ('7', 'ISHA', '60000'),
    ('8', 'JHONY', '85000'),
    ('9', 'KAVITHA', '30000'),
    ('10', 'LAVANYA', '25000'),
    ('11', 'MANAV', '50000'),
    ('12', 'NEHA', '90000'),
    ('13', 'PREM', '25000'),
    ('14', 'RAJESH', '30000'),
    ('15', 'SAVITHA', '50000')

]

dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, "was inserted.")




# Query to get the maximum and minimum salary from employees table
mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM Employee where EMP_SALARY = (select max(EMP_SALARY) from Employee)")

myresult = mycursor.fetchall()
print("Maximum Salary:")
for x in myresult:
    print(x)

mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select min(EMP_SALARY) from Employee)")

myresult = mycursor.fetchall()
print("Minimum Salary:")
for x in myresult:
    print(x)




# Query to get the number of employees working with the company
mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(*) from Employee")

myresult = mycursor.fetchall()
print("Number of Employees:")
for x in myresult:
    print(x)



# Query to get the first 3 characters of first name from employees table
mycursor = mydb.cursor()

mycursor.execute("SELECT SUBSTRING(EMP_NAME,1,3) FROM Employee")

myresult = mycursor.fetchall()
print("First 3 letters of name:")
for x in myresult:
    print(x)