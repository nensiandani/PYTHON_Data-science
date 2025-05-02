import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    # Insert a sample user (username: admin, password: admin123)
    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)
    ''', ('admin', 'admin123'))
    conn.commit()
    conn.close()

# Function to validate login
def validate_login(username, password):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

# Login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    if validate_login(username, password):
        messagebox.showinfo("Login Success", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# GUI setup
root = tk.Tk()
root.title("Login Form")

# Username label and entry
tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password label and entry
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, columnspan=2, pady=10)

# Run the setup database function
setup_database()

# Run the GUI loop
root.mainloop()
