from tkinter import ttk
import tkinter as tk
import tkfilebrowser

root = tk.Tk()
style = ttk.Style(root)
root.geometry("1000x300")

def Theme_Changer():
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
    
Theme_Changer()


def Check_Dupli_Button():
   ttk.Button(root, text="Done", command=Final).place(x=((root.winfo_width()//2)-60), y=((root.winfo_height())-30), width=120, height=25)

dirs = []
value_on = []

def Dir_picker():
    dir_no = 0
    
    dirs.append(tkfilebrowser.askopendirnames(title="Select directories to compare", foldercreation=False, okbuttontext="Done"))
    print(list(dirs[0]), type(dirs[0]))

    for dir_tuple_no in range(0, len(dirs)):
        for dir_no_in_tuple in range(0, len(list(dirs[dir_tuple_no]))):

            dir_no += 1
            varr = tk.IntVar()
            varr.set(1)
            value_on.append(varr)
            
            ttk.Checkbutton(root, variable=varr, text=list(dirs[dir_tuple_no])[dir_no_in_tuple]).place(x = 150, y = (dir_no * 25) + 5, width=600, height=25 )
            Check_Dupli_Button()
    # for dir_no in range (0, len(list(dirs))):
    #     ttk.Checkbutton(root, text=dirs[dir_no]).place(x = 150, y = (dir_no * 25) + 25, width=600, height=25 )
  
    # print(", ".join(str(s) for s in dirs))
######################################################### implement exit
def Final():
    print()    
ttk.Button(root, text='Add a Directory', command=Dir_picker).place(x=5, y=5, width=120, height=25)
ttk.Checkbutton(root, text='Check Button').place(x = 150, y = 5, width=600, height=25 )

# screen_width = root.winfo_width()
# screen_height = root.winfo_height()
# ttk.Button(root, text="Done", command=Final).place(x=270, y=int(screen_height-50), width=120, height=25)

root.mainloop()