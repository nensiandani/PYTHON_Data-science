import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="demo")
mycursor=mydb.cursor()
sql="CREATE TABLE login(username VARCHAR(20)NOT NULL,password CHAR(20))"
mycursor.execute(sql)
mydb.close()

