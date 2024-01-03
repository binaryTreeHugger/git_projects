import tkinter as tk
from tkinter import messagebox

# Create a function to display a message when the button is clicked
def show_message():
    messagebox.showinfo("Message", "Hello, Tkinter!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Example")

# Create a button and add it to the main window
button = tk.Button(root, text="Click Me", command=show_message)
button.pack(pady=20)  # Add some padding around the button

# Run the Tkinter event loop
root.mainloop()
