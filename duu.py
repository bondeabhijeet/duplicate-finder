# import sqlite3
# import tkinter as tk
# from tkinter import ttk

# # Create a Tkinter window
# window = tk.Tk()
# window.title("Duplicate Files")

# # Create a Treeview widget to display the results
# tree = ttk.Treeview(window)
# tree["columns"] = ("Filename", "Paths")
# tree.heading("#0", text="MD5 Hash")
# tree.column("#0", width=150)
# tree.heading("Filename", text="Filename")
# tree.column("Filename", width=200)
# tree.heading("Paths", text="Duplicate Paths")
# tree.column("Paths", width=400)

# # Connect to the SQLite database
# conn = sqlite3.connect("dupfiles.db")
# cursor = conn.cursor()

# # Execute a query to find duplicate MD5 hashes
# query = "SELECT hash, GROUP_CONCAT(paths, '\n') AS paths, COUNT(*) AS count FROM duplicate_files GROUP BY hash HAVING count > 1"
# cursor.execute(query)

# # Fetch the results
# results = cursor.fetchall()

# # Display the results in the Treeview widget
# for md5hash, paths, count in results:
#     item = tree.insert("", "end", text=md5hash, values=(md5hash, paths))

# # Close the database connection
# cursor.close()
# conn.close()

# # Pack the Treeview widget
# tree.pack(expand=True, fill="both")

# # Run the Tkinter event loop
# window.mainloop()



import sqlite3
import tkinter as tk
from tkinter import ttk
import subprocess
import os

# Function to handle button click event
def open_file(path):
    # Implement your logic here to open the file
    print("Opening file:", path)
    subprocess.Popen("explorer " + f"{path}")

# Create a Tkinter window
window = tk.Tk()
window.title("Duplicate Files")

# Create a Treeview widget to display the results
tree = ttk.Treeview(window)
tree["columns"] = ("Filename", "Paths")
tree.heading("#0", text="MD5 Hash")
tree.column("#0", width=150)
tree.heading("Filename", text="Filename")
tree.column("Filename", width=200)
tree.heading("Paths", text="Duplicate Paths")
tree.column("Paths", width=400)

# Connect to the SQLite database
conn = sqlite3.connect("dupfiles.db")
cursor = conn.cursor()

# Execute a query to find duplicate MD5 hashes
query = "SELECT hash, GROUP_CONCAT(paths, '\n') AS paths, COUNT(*) AS count FROM duplicate_files GROUP BY hash HAVING count > 1"
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Display the results in the Treeview widget
for md5hash, paths, count in results:
    path_list = paths.split('\n')
    full_name = os.path.basename(path_list[0])
    item = tree.insert("", "end", text=md5hash, values=(full_name, f"{len(path_list)} copies"))
    # Split the paths by newline character
    
    # Create buttons for each path
    for path in path_list:
        button_text = path.split("/")[-1]  # Extracting only the filename for button text
        tree.insert(item, "end", text="", values=("", button_text, path))

# Close the database connection
cursor.close()
conn.close()

# Configure a button click event handler
def button_click(event):
    item = tree.focus()
    values = tree.item(item, "values")
    if values:
        path = values[-1]  # Last value is the full path
        open_file(path)

# Bind the button click event to the Treeview widget
tree.bind("<Double-1>", button_click)

# Pack the Treeview widget
tree.pack(expand=True, fill="both")

# Run the Tkinter event loop
window.mainloop()
