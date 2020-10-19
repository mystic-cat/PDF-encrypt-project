import tkinter as tk    # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter import ttk
 

# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
win = tk.Tk()
win.title("PDF Encryptor")
win.resizable(True, True)

master = ttk.Labelframe(win, text = "1 -> 4")   # Master Frame
master.grid(column = 0, row = 0, padx = 8, pady = 4)

frm_choose = ttk.Labelframe(master, text = "1") # Frame 1
frm_choose.grid(column = 0, row = 0, padx = 10, pady = 20)
btn_choose = ttk.Button(frm_choose, text = "\n Choose PDF file to encrypt \n")
btn_choose.pack(padx = 10, pady = 10)

frm_pass = ttk.Labelframe(master, text = "2")   # Frame 2
frm_pass.grid(column = 1, row = 0, padx = 10, pady = 2, ipadx = 2, ipady = 10)
lbl_pass = ttk.Label(frm_pass, text = "Set Password:")
lbl_pass.grid(column = 0, row = 0, sticky = "w")
entr_pass = ttk.Entry(frm_pass)
entr_pass.grid(column = 0, row = 1, padx = 8, pady = 10, sticky = "w")

frm_output = ttk.Labelframe(master, text = "3") # Frame 3
frm_output.grid(column = 2, row = 0, padx = 8, pady = 10)
rad_output_default = ttk.Radiobutton(frm_output, text = "Output to default folder")
rad_output_default.grid(column = 0, row = 0, sticky = "w")
rad_output_choose = ttk.Radiobutton(frm_output, text = "Output to a different folder")
rad_output_choose.grid(column = 0, row = 1, sticky = "w")

frm_encrypt = ttk.LabelFrame(master, text = "4")    #Frame 4
frm_encrypt.grid(column = 3, row = 0, padx = 8, pady = 10)
btn_encrypt = ttk.Button(frm_encrypt, text = "Encrypt")
btn_encrypt.pack(padx = 10, pady = 10)




win.mainloop()