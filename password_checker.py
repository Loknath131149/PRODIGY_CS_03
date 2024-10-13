import tkinter as tk
import re


# Function to check password complexity
def check_password():
    password = entry.get()

    if len(password) < 8:
        result_label.config(text="Weak: Too short")
    elif not re.search(r'[A-Z]', password):
        result_label.config(text="Weak: No uppercase letter")
    elif not re.search(r'[a-z]', password):
        result_label.config(text="Weak: No lowercase letter")
    elif not re.search(r'\d', password):
        result_label.config(text="Weak: No number")
    elif not re.search(r'[\W_]', password):
        result_label.config(text="Weak: No special character")
    else:
        result_label.config(text="Strong Password!")


# Setup the Tkinter window
window = tk.Tk()
window.title("Password Checker")
window.geometry("300x150")

# Password input
entry = tk.Entry(window, show="*", width=30)
entry.pack(pady=10)

# Button to check password
check_button = tk.Button(window, text="Check", command=check_password)
check_button.pack(pady=5)

# Label to display result
result_label = tk.Label(window, text="")
result_label.pack(pady=5)

# Run the Tkinter main loop
window.mainloop()
