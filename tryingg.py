import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
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
        
root.tk.call("package", "require", 'awdark')                   # load the awdark and awlight themes
root.tk.call("package", "require", 'awlight')              
style = ttk.Style(root)
style.theme_use('awdark')                                      # Applying the theme
root.configure(bg=style.lookup('TFrame', 'background'))
root.title('Listbox')


# create a list box
langs = ('Java', 'C#', 'C', 'C++', 'Python',
         'Go', 'JavaScript', 'PHP', 'Swift')

var = tk.Variable(value=langs)

listbox = tk.Listbox(
    root,
    listvariable=var,
    height=6,
    selectmode=tk.EXTENDED)

listbox.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

# link a scrollbar to a list
scrollbar = ttk.Scrollbar(
    root,
    orient=tk.VERTICAL,
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

def items_selected(event):
    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'

    showinfo(title='Information', message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)

root.mainloop()