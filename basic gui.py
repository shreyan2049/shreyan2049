import tkinter as tk
from tkinter import messagebox



root=tk.Tk()

root.geometry("500x300")
root.title("Image Viewer")
message=tk.Label(root, text="it is a basic gui in python", font=("Arial", 20),bg="light blue",fg="black")
message.pack( padx=50, pady=50)



root.mainloop()