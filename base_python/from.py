import tkinter
import mysql.connector

# Create a connection to MySQL
database = mysql.connector.connect(host="localhost", user="root", passwd="")
CursorObject = database.cursor()

# Create the database if it doesn't exist
CursorObject.execute("CREATE DATABASE IF NOT EXISTS cute")

# Close the initial connection
database.close()

# Reconnect to the 'cute' database
conn = mysql.connector.connect(host="localhost", user="root", database="cute")
CursorObject = conn.cursor()  # Create a new cursor for this connection
print(conn)
print("Successfully connected")

# Create the employe table if it doesn't already exist
CursorObject.execute("""
CREATE TABLE IF NOT EXISTS employe(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    age INT,
    gender VARCHAR(10),
    email VARCHAR(30),
    mobile VARCHAR(10)
)
""")

# Registration function for inserting user data into the table
def registration():
    name = e1.get()
    age = e2.get()
    gender = e3.get()
    email = e4.get()
    mobile = e5.get()

    # Using a parameterized query to insert data
    sql = "INSERT INTO employe (name, age, gender, email, mobile) VALUES (%s, %s, %s, %s, %s)"
    val = (name, age, gender, email, mobile)
    CursorObject.execute(sql, val)
    conn.commit()
    print("Data inserted successfully")
  
    # Using a parameterized query to update data
    #sql = "UPDATE employe SET name='anandi' WHERE no='1'"
    #CursorObject.execute(sql)
    #conn.commit()
    #print("Data inserted successfully")

     # Using a parameterized query to delete data
     #sql="delete from employe where name='3'"
     #CursorObject.execute(sql)


CursorObject.execute("select *from employe")
result=CursorObject.fetchall()

for row in result:
    print(row)
    print("\n")
 

# Creating the Tkinter window
win = tkinter.Tk()
win.title("Registration Form")

# Creating labels for the form
l1 = tkinter.Label(win, text="Person Details")
l2 = tkinter.Label(win, text="Name")
l3 = tkinter.Label(win, text="Age")
l4 = tkinter.Label(win, text="Gender")
l5 = tkinter.Label(win, text="Email")
l6 = tkinter.Label(win, text="Mobile Number")

# Placing the labels on the grid
l1.grid(row=1, column=1)
l2.grid(row=2, column=1)
l3.grid(row=3, column=1)
l4.grid(row=4, column=1)
l5.grid(row=5, column=1)
l6.grid(row=6, column=1)

# Creating entry fields
e1 = tkinter.Entry(win)
e2 = tkinter.Entry(win)
e3 = tkinter.Entry(win)
e4 = tkinter.Entry(win)
e5 = tkinter.Entry(win)

# Placing the entry fields on the grid
e1.grid(row=2, column=2)
e2.grid(row=3, column=2)
e3.grid(row=4, column=2)
e4.grid(row=5, column=2)
e5.grid(row=6, column=2)

# Submit button to trigger the registration function
b = tkinter.Button(win, text="Submit", command=registration)
b.grid(row=7, column=1)

# Start the Tkinter loop
win.mainloop()

# Close the database connection when done
conn.close()
