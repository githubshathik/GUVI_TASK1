#Advance programming and Master data science
#Task Submission
#Name:Mohamed Shathik
#Batch:D10(B)
#Dept:Data Science
#mail id:mohamedshafa17@gmail.com

import mysql.connector
from mysql.connector import Error
import sys
def sql_connection():
    try:
        mydb=mysql.connector.connect(user="root",password="mysqlshathik",host="localhost",database="learning")
        return mydb
    except Error:
        print(Error)
def sql_insert(mydb,A,B,m1,m2,m3,m4,m5,total,avg,grade):
    try:
        cursor=mydb.cursor()
        s="""INSERT INTO student(
        Name, Department, mark1, mark2, mark3, mark4, mark5, totalmark, average, grade) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        b1=(A,B,m1,m2,m3,m4,m5,total,avg,grade)
        cursor.execute(s,b1)
        mydb.commit()
        print("Details Added")
    except Error as e:
        print(e)
def gradeper(avg):
    if avg<=100 and avg>=90:
        return "S"
    elif avg<90 and avg>=80:
        return "A"
    elif avg<80 and avg>=70:
        return "B"
    elif avg<70 and avg>=60:
        return "C"
    else:
        return "D"
print("""Please Enter Below Your Selection With Number
1. add new student
2. get student
3. get all student
4. edit a student
5. delete a student
6. exit
""")
choice=int(input("enter your choice :- "))
if choice==6 or choice<1 or choice>6:
    print("You select the exit option")
    sys.exit()

elif choice==1:
    A=input("Enter Your Name:- ")
    B=input("Enter your department:-  ")
    m1=int(input("Enter mark1:-  "))
    m2=int(input("Enter mark2:-  "))
    m3=int(input("Enter mark3:-  "))
    m4=int(input("Enter mark4:- "))
    m5=int(input("Enter mark5:-  "))
    total=(m1+m2+m3+m4+m5)
    avg=(total/5)
    grade=gradeper(avg)
    mydb=sql_connection()
    sql_insert(mydb,A,B,m1,m2,m3,m4,m5,total,avg,grade)
else:
    print("Exit")




