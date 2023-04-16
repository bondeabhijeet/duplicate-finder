import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)
scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# create a list box
langs = ('Java', 'C#', 'C', 'C++', 'Python',
         'Go', 'JavaScript', 'PHP', 'Swift')
var = tk.Variable(value=langs)
listbox = tk.Listbox(root, listvariable=var, height=6, selectmode=tk.EXTENDED)

checklist = tk.Text(root, width=600)
checklist.pack()
listbox.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

vars = []
for i in range(50):
    var = tk.IntVar()
    vars.append(var)
    checkbutton = ttk.Checkbutton(checklist, text=i, variable=var)
    checklist.window_create("end", window=checkbutton)
    checklist.insert("end", "\n")

checklist.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=checklist.yview)


root.mainloop()