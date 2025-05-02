import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="demo")
myCursor=mydb.cursor()

sql="delete from student where NAME='3'"
myCursor.execute(sql)
mydb.commit()
 
mydb.close()
