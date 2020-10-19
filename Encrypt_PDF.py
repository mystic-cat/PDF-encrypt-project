import tkinter as tk    # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import ttk
 

filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
win = tk.Tk()


win.mainloop()