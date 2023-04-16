import sqlite3              # Import the modules
import sqbase as sqdatabase
import dupfinder as DF

from tkinter import ttk
import tkinter as tk
import tkfilebrowser
import exit as EXIT
import time

class duplicate_finder:
    def __init__(self):
        self.DB_Name = "dupfiles.db"                    # Database name
        self.Table_Name = "duplicate_files"             # Table name

        self.conn = sqlite3.connect(self.DB_Name)                   # Connecting to the named database, if not pesent then create
        self.cur = self.conn.cursor()                               # Creating the cursor
        sqdatabase.DropTable(self.cur, self.Table_Name)             # Droping the perexisting table
        sqdatabase.CreateTable(self.cur, self.Table_Name)           # Creating a new table

        self.root = tk.Tk()                                         # Root window for the GUI
        self.style = ttk.Style(self.root)                           # Creating the style attribute to add style to the GUI
        self.root.geometry("1000x300")                              # Fixing the size of the opened window
        self.dirs = []                                                  # List of multiple directories seleted from the tkfilebrowser (multiple selection gives a tuple)
        self.dir_list = []                                              # Separating directory from tuple to create a simple list
        self.value_on = []                                              # List of all the values that have tick's of selection
        self.button_made = []                                           # List of all the buttons that have been displayed on the sreen already
        self.scrollbar = ttk.Scrollbar(self.root)                       # Adding srollar to the list of buttons
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)                   # Packng the scrollbar
        self.checklist = tk.Text(self.root, width=20, bd=0, pady=10)    # This is used to append the buttons from the bottom of the list
        self.checklist.pack()

    def scrlbr(self):                                                   # Configuring the scollbar
        self.checklist.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.checklist.yview)
        self.checklist.configure(state="disabled",bg=self.style.lookup('TFrame', 'background'))     # Setting the theme
        ttk.Button(self.root, text='Add a Directory', command=self.dirs_list_maker).place(x=5, y=5, width=120, height=25)
        # ttk.Checkbutton(self.root, text='Check Button').place(x = 150, y = 5, width=600, height=25 )


    def Theme_Changer(self):                                            # Change the theme of the app from default to awdark using the tcl files
        # tell tcl where to find the awthemes packages
        self.root.tk.eval("""
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
        
        self.root.tk.call("package", "require", 'awdark')                   # load the awdark and awlight themes
        self.root.tk.call("package", "require", 'awlight')              

        self.style.theme_use('awdark')                                      # Applying the theme
        self.root.configure(bg=self.style.lookup('TFrame', 'background'))

    def Done_Exit_button(self):
        self.start_button = ttk.Button(self.root, text="Start", command=self.Final).place(x=((self.root.winfo_width()//2)-60), y=((self.root.winfo_height())-30), width=120, height=25)
        ttk.Button(self.root, text="Exit", command=EXIT.exit).place(x=((self.root.winfo_width())-70), y=((self.root.winfo_height())-30), width=60, height=25)

    def Dir_picker(self, args):
        for dir in self.dir_list:
            if dir not in self.button_made:

                varr = tk.IntVar()
                varr.set(1)
                self.value_on.append(varr)
                    
                self.checkbutton = ttk.Checkbutton(self.root, variable=varr, text=dir)#.place(x = 150, y = (dir_no * 25) + 5, width=600, height=25 )
                self.checklist.window_create("end", window=self.checkbutton)
                self.checklist.insert("end", "\n")
                self.Done_Exit_button()
                self.button_made.append(dir)

    def dirs_list_maker(self):
        dir_no = 0
        
        self.dirs.append(tkfilebrowser.askopendirnames(title="Select directories to compare", foldercreation=False, okbuttontext="Done"))

        for dir_tuple_no in range(0, len(self.dirs)):
            for dir_no_in_tuple in range(0, len(list(self.dirs[dir_tuple_no]))):
                if list(self.dirs[dir_tuple_no])[dir_no_in_tuple] in self.dir_list:
                    print()
                else:
                    self.dir_list.append(list(self.dirs[dir_tuple_no])[dir_no_in_tuple])
                    print(self.dir_list)

                    dir_no += 1
        
        self.Dir_picker(self)

    def Final(self):
        self.root.destroy()

        for dir in range(0, len(self.dir_list)):
            if (self.value_on[dir].get()==0):
                print()
            else:
                print("stats: ", self.dir_list[dir], self.value_on[dir].get())
                # ttk.Label(self.root, text=f" PROCESSNG").place(x=((self.root.winfo_width())-350), y=((self.root.winfo_height())-100))
                File_List = DF.ScanAll(self.dir_list[dir])      # Get the list of all the files present in the given directory
                sqdatabase.FillDatabase(File_List, self.cur, self.Table_Name)
                self.conn.commit()
            print()  


    def startw(self):
        self.root.mainloop()

    def ccn_lose(self):
        self.conn.close()

r = duplicate_finder()
r.Theme_Changer()
r.scrlbr()
r.startw()