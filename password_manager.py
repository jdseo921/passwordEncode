import tkinter as tk
from tkinter import messagebox
import sqlite3

def setup_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def login():
    def check_login():
        username = username_entry.get()
        password = password_entry.get()
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            messagebox.showinfo("Login Success", "Welcome, {}!".format(username))
            # Proceed to the next part of your app
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    login_window = tk.Tk()
    login_window.title("Login")

    tk.Label(login_window, text="Username").pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    tk.Label(login_window, text="Password").pack()
    password_entry = tk.Entry(login_window, show='*')
    password_entry.pack()

    tk.Button(login_window, text="Login", command=check_login).pack()

    login_window.mainloop()

def register():
    def add_user():
        username = username_entry.get()
        password = password_entry.get()

        if username and password:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()
            try:
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
                conn.commit()
                messagebox.showinfo("Registration Success", "User registered successfully!")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username already exists")
            conn.close()
        else:
            messagebox.showerror("Error", "Both fields are required")

    register_window = tk.Tk()
    register_window.title("Register")

    tk.Label(register_window, text="Username").pack()
    username_entry = tk.Entry(register_window)
    username_entry.pack()

    tk.Label(register_window, text="Password").pack()
    password_entry = tk.Entry(register_window, show='*')
    password_entry.pack()

    tk.Button(register_window, text="Register", command=add_user).pack()

    register_window.mainloop()

def main():
    setup_db()
    
    main_window = tk.Tk()
    main_window.title("Password Manager")

    tk.Label(main_window, text="Password Manager", font=("Helvetica", 16)).pack(pady=20)

    tk.Button(main_window, text="Login", command=login).pack(pady=10)
    tk.Button(main_window, text="Register", command=register).pack(pady=10)

    main_window.mainloop()

if __name__ == "__main__":
    main()
