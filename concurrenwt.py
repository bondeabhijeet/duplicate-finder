# from multiprocessing import Process
# from concurrent.futures import ProcessPoolExecutor
# import time

# def func1():
#     print("waiting 3 seconds")
#     time.sleep(3)
#     print("Done waiting 3 seconds")


# def func2():
#     print("waiting 5 seconds")
#     time.sleep(5)
#     print("Done waiting 5 seconds")


# if __name__ == '__main__':
#     with ProcessPoolExecutor(max_workers=2) as executor:
#         future1 = executor.submit(func1)
#         future2 = executor.submit(func2)
#         # wait for the futures to complete
#         future1.result()
#         future2.result()

import tkinter as tk
import time

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frame = tk.Frame(self)
        self.frame.pack(side="top", fill = "both", expand=True)

        self.label = tk.Label(self, text = "Hello, world")
        button1 = tk.Button(self, text = "Start to do something",
                                  command = self.do_something)
        self.label.pack(in_=self.frame)
        button1.pack(in_=self.frame)

    def do_something(self):
        self.label.config(text = "Wait till I'm done...")
        self.label.update_idletasks()
        time.sleep(2)
        print ("end sleep")
        self.label.config(text = "I'm done doing...")

def main():
    app = SampleApp()
    app.mainloop()  
    return 0
    
if __name__ == '__main__':
    main()