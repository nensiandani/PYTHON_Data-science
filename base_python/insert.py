import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="demo")
myCursor=mydb.cursor()

sql="insert into student(NO,NAME,CITY) values(%s,%s,%s)"
val=[("1","nensi","latipar"),("2","yashi","manavder"),("3","anandi","rajkot")]

myCursor.executemany(sql,val)
mydb.commit()

print(myCursor.rowcount,"deltis inserted")
mydb.close()
