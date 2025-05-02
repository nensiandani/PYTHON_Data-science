import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",database="demo")
print(conn)
print("succafully conection")
conn.close()