import sqlite3              # Import the modules
import sqbase as sqdatabase
import dupfinder as DF

from tkinter import ttk
import tkinter as tk
import tkfilebrowser
import exit as EXIT

DB_Name = "dupfiles.db"               # Database name
Table_Name = "duplicate_files"        # Table name

conn = sqlite3.connect(DB_Name)
cur = conn.cursor()
sqdatabase.DropTable(cur, Table_Name)
sqdatabase.CreateTable(cur, Table_Name)

################################################# GUI

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

dirs = []
dir_list = []
value_on = []
button_made = []
scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
checklist = tk.Text(root, width=20, bd=0, pady=10)
checklist.pack()

def Check_Dupli_Button():
   ttk.Button(root, text="Done", command=Final).place(x=((root.winfo_width()//2)-60), y=((root.winfo_height())-30), width=120, height=25)
   ttk.Button(root, text="Exit", command=EXIT.exit).place(x=((root.winfo_width())-70), y=((root.winfo_height())-30), width=60, height=25)



def Dir_picker():
    for dir in dir_list:
        if dir not in button_made:

            varr = tk.IntVar()
            varr.set(1)
            value_on.append(varr)
                
            checkbutton = ttk.Checkbutton(root, variable=varr, text=dir)#.place(x = 150, y = (dir_no * 25) + 5, width=600, height=25 )
            checklist.window_create("end", window=checkbutton)
            checklist.insert("end", "\n")
            Check_Dupli_Button()
            button_made.append(dir)

def dirs_list_maker():
    dir_no = 0
    
    dirs.append(tkfilebrowser.askopendirnames(title="Select directories to compare", foldercreation=False, okbuttontext="Done"))

    for dir_tuple_no in range(0, len(dirs)):
        for dir_no_in_tuple in range(0, len(list(dirs[dir_tuple_no]))):
            if list(dirs[dir_tuple_no])[dir_no_in_tuple] in dir_list:
                print()
            else:
                dir_list.append(list(dirs[dir_tuple_no])[dir_no_in_tuple])
                print(dir_list)

                dir_no += 1
    
    Dir_picker()

checklist.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=checklist.yview)
checklist.configure(state="disabled",bg=style.lookup('TFrame', 'background'))


def Final():
    for dir in range(0, len(dir_list)):
        print("DDDDDDDDDDDD: ", dir, dir_list[dir])
        if (value_on[dir].get()==0):
            print()
        else:
            print("stats: ",dir_list[dir], value_on[dir].get())
            File_List = DF.ScanAll(dir_list[dir])      # Get the list of all the files present in the given directory
            sqdatabase.FillDatabase(File_List, cur, Table_Name)
            conn.commit()
        print()  

ttk.Button(root, text='Add a Directory', command=dirs_list_maker).place(x=5, y=5, width=120, height=25)
ttk.Checkbutton(root, text='Check Button').place(x = 150, y = 5, width=600, height=25 )

root.mainloop()
conn.close()