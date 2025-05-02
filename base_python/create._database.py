import mysql.connector

database=mysql.connector.connect(host="localhost",user="root",passwd="")
CursorObject=database.cursor()
CursorObject.execute("CREATE DATABASE demo") 