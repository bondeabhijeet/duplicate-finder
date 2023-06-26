import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import os

# Function to handle delete button click event
def delete_file(item):
    values = tree.item(item, "values")
    print(values)
    if values:
        path = values[-1]  # Last value is the full path
        if path != "Delete":
            if os.path.exists(path):
                # Implement your logic here to delete the file
                try:
                    os.remove(path)
                    print("Deleted file:", path)
                    # Update the database
                    cursor.execute("DELETE FROM your_table WHERE filepaths=?", (path,))
                    conn.commit()
                    # Update the Treeview
                    tree.delete(item)
                except OSError as e:
                    print("Error deleting file:", e)
            else:
                print("File not found:", path)

# Function to handle button click event
def open_file(path):
    # Implement your logic here to open the file
    print("Opening file:", path)

# Create a Tkinter window
window = tk.Tk()
window.title("Duplicate Files")

# Create a Treeview widget to display the results
tree = ttk.Treeview(window)
tree["columns"] = ("Filename", "Paths", "Delete")
tree.heading("#0", text="MD5 Hash")
tree.column("#0", width=150)
tree.heading("Filename", text="Filename")
tree.column("Filename", width=200)
tree.heading("Paths", text="Duplicate Paths")
tree.column("Paths", width=400)
tree.heading("Delete", text="Delete")
tree.column("Delete", width=100)

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
    item = tree.insert("", "end", text=md5hash, values=(md5hash, paths))
    # Split the paths by newline character
    path_list = paths.split('\n')
    # Create buttons for each path
    for path in path_list:
        if path != "":
            button_text = path.split("/")[-1]  # Extracting only the filename for button text
            tree.insert(item, "end", text="", values=("", button_text, path))

    # Create delete button in the last column
    delete_button = ttk.Button(tree, text="Delete", command=lambda item=item: delete_file(item))
    tree.set(item, "Delete", "")
    tree.insert(item, "end", text="", values=("", "", ""), image="", tag="delete_button")
    tree.set(item, "Delete", delete_button)

# Close the database connection
cursor.close()
conn.close()

# Configure a button click event handler
def button_click(event):
    item = tree.focus()
    tags = tree.item(item, "tags")
    if tags:
        if "delete_button" in tags:
            delete_file(item)

# Bind the button click event to the Treeview widget
tree.bind("<Double-1>", button_click)

# Pack the Treeview widget
tree.pack(fill="both", expand=True)

# Run the Tkinter event loop
window.mainloop()
