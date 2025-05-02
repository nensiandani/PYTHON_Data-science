import mysql.connector
import matplotlib.pyplot as plt

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="demo")
myCursor=mydb.cursor()

myCursor.execute("select *from emp")

result=myCursor.fetchall


name=[]
marks=[]
 
for i in myCursor:
    name.append(i[0])
    marks.append(i[1])
    
print("name of student=",name)
print("city of student=",marks)

plt.bar(name,marks)
plt.title("student details")
plt.xlabel("name of student")
plt.ylabel("marks of student")
plt.show()