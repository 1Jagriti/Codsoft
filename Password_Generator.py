import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

# Function to handle the button click event
def on_generate_button_click():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Invalid Input", "Password length should be at least 1.")
            return
        password = generate_password(length)
        result_label.config(text=f"Generated password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")

# Create the main window
base = tk.Tk()
base.title("Password Generator")

# Create and place the widgets
tk.Label(base, text="Enter the desired length for your password:").pack(pady=10)
length_entry = tk.Entry(base)
length_entry.pack(pady=5)

generate_button = tk.Button(base, text="Generate Password", command=on_generate_button_click)
generate_button.pack(pady=20)

result_label = tk.Label(base, text="")
result_label.pack(pady=10)

# Run the application
base.mainloop()

