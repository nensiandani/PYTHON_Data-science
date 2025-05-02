import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="demo")
myCursor=mydb.cursor()

sql="update student set NAME='yashi' where NO='2'"
myCursor.execute(sql)
mydb.commit()
 
mydb.close()
