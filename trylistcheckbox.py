# from tkinter import *
# from tkinter import ttk

# root = Tk()
# style = ttk.Style(root)
# root.title("Vertical Scrollbar Example")

#     # tell tcl where to find the awthemes packages
# root.tk.eval("""
#     set base_theme_dir Y:/duplicate-finder/awthemes-10.4.0

#     package ifneeded awthemes 10.4.0 \
#         [list source [file join $base_theme_dir awthemes.tcl]]
#     package ifneeded colorutils 4.8 \
#         [list source [file join $base_theme_dir colorutils.tcl]]
#     package ifneeded awdark 7.12 \
#         [list source [file join $base_theme_dir awdark.tcl]]
#     package ifneeded awlight 7.6 \
#         [list source [file join $base_theme_dir awlight.tcl]]
#     """)
#     # load the awdark and awlight themes
# root.tk.call("package", "require", 'awdark')
# root.tk.call("package", "require", 'awlight')

#     # print(style.theme_names())
#     # --> ('awlight', 'clam', 'alt', 'default', 'awdark', 'classic')

# style.theme_use('awdark')
# root.configure(bg=style.lookup('TFrame', 'background'))

# # create a canvas and a scrollbar
# canvas = Canvas(root)
# scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=canvas.yview)
# style.theme_use('awdark')
# canvas.config(bg="grey")
# # link the scrollbar to the canvas
# canvas['yscrollcommand'] = scrollbar.set

# # place the canvas and the scrollbar on the root window
# canvas.pack(side=LEFT, fill=BOTH)
# scrollbar.pack(side=RIGHT, fill=Y)

# # create a frame inside the canvas
# frame = ttk.Frame(canvas)
# canvas.create_window(0, 0, window=frame, anchor='nw')

# # create multiple checkbox widgets inside the frame
# for i in range(20):
#     checkbox = ttk.Checkbutton(frame, text=f"Checkbox {i+1}")
#     checkbox.pack(anchor="w")

# # adjust the scroll region of the canvas
# canvas.configure(scrollregion=canvas.bbox('all'))

# root.mainloop()

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)
scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
ttk.Button(root, text='Add a Directory').place(x=5, y=5, width=120, height=25)
checklist = tk.Text(root, width=1000)
checklist.pack()

    # tell tcl where to find the awthemes packages
root.tk.eval("""
    set base_theme_dir Y:/duplicate-finder/awthemes-10.4.0

    package ifneeded awthemes 10.4.0 \
        [list source [file join $base_theme_dir awthemes.tcl]]
    package ifneeded colorutils 4.8 \
        [list source [file join $base_theme_dir colorutils.tcl]]
    package ifneeded awdark 7.12 \
        [list source [file join $base_theme_dir awdark.tcl]]
    package ifneeded awlight 7.6 \
        [list source [file join $base_theme_dir awlight.tcl]]
    """)
    # load the awdark and awlight themes
root.tk.call("package", "require", 'awdark')
root.tk.call("package", "require", 'awlight')

    # print(style.theme_names())
    # --> ('awlight', 'clam', 'alt', 'default', 'awdark', 'classic')

style.theme_use('awdark')
root.configure(bg=style.lookup('TFrame', 'background'))

vars = []
for i in range(50):
    var = tk.IntVar()
    vars.append(var)
    checkbutton = ttk.Checkbutton(checklist, text=i, variable=var)
    checklist.window_create("end", window=checkbutton)
    checklist.insert("end", "\n")

checklist.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=checklist.yview)

# disable the widget so users can't insert text into it
checklist.configure(state="disabled",bg=style.lookup('TFrame', 'background'))
style.theme_use('awdark')
root.mainloop()