import mysql.connector
mydb=mysql.connector.connect(
    user="root",
    password="mysqlshathik",
    host="localhost",
    database="learning"
    )
cursor=mydb.cursor()
A=input("Enter Your Name ")
B=input("Enter your department ")
m1=int(input("Enter mark1 "))
m2=int(input("Enter mark2 "))
m3=int(input("Enter mark3 "))
m4=int(input("Enter mark4 "))
m5=int(input("Enter mark5 "))
total=(m1+m2+m3+m4+m5)
avg=(total/5)
if avg<=100 and avg>=90:
    grade="S"
elif avg<90 and avg>=80:
    grade="A"
elif avg<80 and avg>=70:
    grade="B"
elif avg<70 and avg>=60:
    grade="C"
else:
    grade="D"

cursor.execute("CREATE TABLE student (studentid int PRIMARY key AUTO_INCREMENT not null,Name varchar(20) not null, Department varchar(20) not null,mark1 int not null, mark2 int not null, mark3 int not null, mark4 int not null,mark5 int not null, totalmark int not null, average int not null, grade varchar(5))")


s="INSERT INTO student(Name, Department, mark1, mark2, mark3, mark4, mark5, totalmark, average, grade) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
b1=(A,B,m1,m2,m3,m4,m5,total,avg,grade)
cursor.execute(s,b1)
mydb.commit()
