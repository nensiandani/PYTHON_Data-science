import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to handle login logic with MySQL database
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Establishing connection to the database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username (root by default)
            password="",  # Replace with your MySQL password (empty by default in XAMPP)
            database="demo"  # Replace with your database name
        )
        
        cursor = connection.cursor()

        # Query to check if the username and password are correct
        query = "insert into login(username,password) values(%s,%s)"
        cursor.execute(query, (username, password))

        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to handle quitting the application
def quit_app():
    window.destroy()

# Creating the main window
window = tk.Tk()
window.title("Login Form")

# Username label and text entry box
label_username = tk.Label(window, text="Username")
label_username.pack(pady=5)
entry_username = tk.Entry(window)
entry_username.pack(pady=5)

# Password label and password entry box
label_password = tk.Label(window, text="Password")
label_password.pack(pady=5)
entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=5)

# Login button
button_login = tk.Button(window, text="Login", command=login)
button_login.pack(pady=5)

# Quit button
button_quit = tk.Button(window, text="Quit", command=quit_app)
button_quit.pack(pady=5)

# Start the GUI event loop
window.mainloop()
