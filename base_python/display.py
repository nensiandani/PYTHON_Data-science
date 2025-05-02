import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="demo")
myCursor=mydb.cursor()

myCursor.execute("select *from student")
result=myCursor.fetchall()

for row in result:
    print(row)
    print("\n")
 

