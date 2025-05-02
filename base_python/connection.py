import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="demo")

if con.is_connected():
    print("connection successful")
else:
    print("not connection")
con.close()