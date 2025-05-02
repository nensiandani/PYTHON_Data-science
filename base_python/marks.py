import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="demo")
myCursor=mydb.cursor()

sql="insert into emp(name,marks) values(%s,%s)"
val=[("nensi","94"),("yashi","50"),("anandi","86")]


myCursor.executemany(sql,val)
mydb.commit()

print(myCursor.rowcount,"deltis inserted")
mydb.close()
