import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="demo")
mycursor=mydb.cursor()
sql="CREATE TABLE STUDENT(NO INT  NOT NULL,NAME VARCHAR(20)NOT NULL,CITY CHAR(20))"
mycursor.execute(sql)
mydb.close()

