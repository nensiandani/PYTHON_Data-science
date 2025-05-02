import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="demo")
myCursor=mydb.cursor()

sql="insert into student(NO,NAME,CITY) values(%s,%s,%s)"
val=[("1","nensi","latipar"),("2","yashi","manavder"),("3","anandi","rajkot")]
myCursor.executemany(sql,val)
print(myCursor.rowcount,"deltis inserted")
mydb.commit()

sql="update student set NAME='ankita' where NO='2'"
myCursor.execute(sql)
print(myCursor.rowcount,"deltis update")
mydb.commit()

sql="delete from student where NAME='ankita'"
myCursor.execute(sql)
print(myCursor.rowcount,"deltis delete")
mydb.commit()


myCursor.execute("select *from student")
result=myCursor.fetchall()

for row in result:
    print(row)
    print("\n")


mydb.close()
