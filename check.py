import tkinter as tk
from tkinter import ttk
from MUserDL import MUser_DL
MUser_DL.ReadUserFromFile("Users.txt")
def displaydata():
    for item in MUser_DL.userlist:
        datagrid.insert("", "end", values=(item.GetUsername(), item.GetPassword(), item.GetRole()))

# Create the main window
root = tk.Tk()

# Create a Treeview widget
datagrid = ttk.Treeview(root, columns=("Username", "Password", "Role"), show="headings")

# Set column headings
datagrid.heading("Username", text="Username")
datagrid.heading("Password", text="Password")
datagrid.heading("Role", text="Role")

# Insert data into the Treeview
# displaydata()

# Apply padding and add lines between rows using the style option
style = ttk.Style()
style.configure("Custom.Treeview", padding=(0, 10), rowheight=25)

datagrid.configure(style="Custom.Treeview")

# Insert data and formatting
displaydata()

# Pack the Treeview widget
datagrid.pack()

# Run the main loop
root.mainloop()
