import tkinter as tk    
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file


def _quit():
    win.quit()
    win.destroy()
    exit()

def _about_msg_box():
    msg.showinfo("About","Created by Jared Letts\n Version 0.5")





""" 
***************************GUI*********************
"""
win = tk.Tk()
win.title("PDF Encryptor")
win.resizable(False, False)

menu_bar = Menu(win)    #Menu bar configuration
win.config(menu = menu_bar)

file_menu = Menu(menu_bar, tearoff = 0) #File menu
file_menu.add_command(label = "Quit", command = _quit)
menu_bar.add_cascade(label = "File", menu = file_menu)

help_menu = Menu(menu_bar, tearoff = 0) #Help Menu
menu_bar.add_cascade(label = "Help", menu = help_menu)
help_menu.add_command(label = "About", command = _about_msg_box)

master = ttk.Labelframe(win, text = "1 -> 4")   # Master Frame
master.grid(column = 0, row = 0, padx = 8, pady = 4)

frm_choose = ttk.Labelframe(master, text = "1") # Frame 1
frm_choose.grid(column = 0, row = 0, padx = 10, pady = 20)
btn_choose = ttk.Button(frm_choose, text = "\n Choose PDF file to encrypt \n")
btn_choose.pack(padx = 10, pady = 10)

frm_pass = ttk.Labelframe(master, text = "2")   # Frame 2
frm_pass.grid(column = 1, row = 0, padx = 10, pady = 2, ipadx = 2, ipady = 8)
lbl_pass = ttk.Label(frm_pass, text = "Set Password:")
lbl_pass.grid(column = 0, row = 0, sticky = "w")
entr_pass = ttk.Entry(frm_pass)
entr_pass.grid(column = 0, row = 1, padx = 8, pady = 10, sticky = "w")
entr_pass.focus()   #Place cursor into password entry line when the app starts

frm_output = ttk.Labelframe(master, text = "3") # Frame 3
frm_output.grid(column = 2, row = 0, padx = 8, pady = 10, ipadx = 2, ipady = 13)
rad_output_default = ttk.Radiobutton(frm_output, text = "Output to default folder")
rad_output_default.grid(column = 0, row = 0, sticky = "sw", pady = 6)
rad_output_choose = ttk.Radiobutton(frm_output, text = "Output to a different folder")
rad_output_choose.grid(column = 0, row = 1, sticky = "sw")

frm_encrypt = ttk.LabelFrame(master, text = "4")    #Frame 4
frm_encrypt.grid(column = 3, row = 0, padx = 8, pady = 10)
btn_encrypt = ttk.Button(frm_encrypt, text = "\nEncrypt\n")
btn_encrypt.pack(padx = 10, pady = 12)


win.mainloop()
"""
***************************GUI*********************
"""