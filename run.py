
import tkinter as tk
from tkinter import messagebox, filedialog
import datetime

def show_hello():
    messagebox.showinfo("Hello", "Hello, World!")

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        messagebox.showinfo("Selected File", f"You selected: {file_path}")

def show_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messagebox.showinfo("Current Time", f"Current time: {current_time}")

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Multi-Feature App")
root.geometry("300x200")

# Create a button to show the hello message
hello_button = tk.Button(root, text="Say Hello", command=show_hello)
hello_button.pack(pady=10)

# Create a button to open a file dialog
file_button = tk.Button(root, text="Open File", command=open_file)
file_button.pack(pady=10)

# Create a button to show the current time
time_button = tk.Button(root, text="Show Time", command=show_time)
time_button.pack(pady=10)

# Create a button to exit the application
exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=10)

# Run the application
root.mainloop()
