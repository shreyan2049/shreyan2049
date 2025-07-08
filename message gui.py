import tkinter as tk
from tkinter import messagebox  # Import messagebox
from functools import partial  # Import partial

root = tk.Tk()
root.geometry("600x400")
root.title("My App")
frame = tk.Frame(root)
frame.pack()  
def custom_message(message: str):  # Corrected function name
    messagebox.showinfo("Title of Message", message)  # Corrected 'titel' to 'Title'

button = tk.Button(frame,
                   text="Don't show me",
                   fg="red",
                   bg="yellow",
                   font="calibri 15 italic",
                   relief=tk.RAISED,  # Use tk.RAISED for raised effect
                   command=quit)
                   
button.pack(padx=40, pady=40)

msg_box_btn = tk.Button(frame,
                        text="Show message",
                        fg="blue",
                        bg="lightgreen",
                        font="calibri 15 italic",
                        relief=tk.RAISED,  # Use tk.RAISED for raised effect
                        command=partial(custom_message, "A good boy shows respect to elders, teachers, and peers, using polite language and demonstrating good manners in all situations. He treats everyone with kindness and consideration,regardless of their age or background")) # Use partial to pass the message
# Use partial to pass the message to the function
msg_box_btn.pack(padx=20, pady=20)
root.mainloop()  # Set background color to light blue