import tkinter as tk    
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg
import os
import pikepdf
from pikepdf import Pdf


input_dir_chosen = False
current_dir = os.getcwd()

def _quit():    #quits the application
    win.quit()
    win.destroy()
    exit()

def _about_msg_box():   #displays the about message box
    msg.showinfo("About","Created by Jared Letts\n Version 0.5")

def _get_filename():    #Opens a dialog bot asking for the input file
    global original_path
    global input_dir_chosen
    original_path = askopenfilename(initialdir = "/", title = "Select PDF to Encrypt", filetypes = (("PDF files","*.pdf"),("all files","*.*"))) # show an "Open" dialog box and return the path to the selected file
    if original_path.endswith(".pdf") or original_path.endswith(".PDF"):
        original_path = original_path
        input_dir_chosen = True
    elif original_path == "":   #If box is opened but nothing is chosen
        original_path = False
    else:
        msg.showerror("Error", "Please choose a PDF file\nThey end in .pdf")
        
def _different_output():    #If the user chooses to save into a different directory than the default
    output = askdirectory(initialdir = current_dir)

def _encrypt_btn(): #This is the flow of operations when the Encrypt button is pressed
    PDF_FILE()._file_check()
    PDF_FILE()._password_check()
    rad_sel = radVar.get()
    if rad_sel == 1:
        PDF_FILE()._default_output()
    
    pass
"""
**************************************Encryption Begins***********************************
"""
class PDF_FILE:
    

    def __init__(self):
        pass
        
    
        

    def _file_check(self):   #If no file was selected before pushing encrypt button
        if input_dir_chosen == False:  
            return msg.showerror("Error", "Please choose a PDF file that you want to Encrypt\nOption:1")

    def _password_check(self):  #Checks to make sure that a valid password was entered
        if password == "":
            return msg.showerror("Error", "Please enter a password!")
    
    def _default_output(self):  #Creates a default folder if one does not exist
        if os.path.isdir(current_dir + '\Encrypted Files'):
            pass
        else:
            try:
                os.mkdir(current_dir + '\Encrypted Files')
            except OSError:
                return msg.showerror("Error", "Creation of a default folder failed")
            else:
                output = current_dir + '\Encrypted Files'
    
    def _encryption(self):
        pass
"""
**************************************Encryption Ends*************************************
"""

"""
***************************************Tool Tips Begins***********************************
"""

class ToolTip(object):
    def __init__(self, widget, tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        widget.bind('<Enter>', self.mouse_enter)           # bind mouse events
        widget.bind('<Leave>', self.mouse_leave)

    def mouse_enter(self, _event):                       
        self.show_tooltip()
        
    def mouse_leave(self, _event):
        self.hide_tooltip()

    def show_tooltip(self):
        if self.tip_text:
            x_left = self.widget.winfo_rootx()                          # get widget top-left coordinates
            y_top = self.widget.winfo_rooty() - 18                      # place tooltip above widget or it flickers
            
            self.tip_window = tk.Toplevel(self.widget)                  # create Toplevel window; parent=widget
            self.tip_window.overrideredirect(True)                      # remove surrounding toolbar window
            self.tip_window.geometry("+%d+%d" % (x_left, y_top))        # position tooltip 
    
            label = tk.Label(self.tip_window, text=self.tip_text, justify=tk.LEFT,
                          background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                          font=("tahoma", "8", "normal"))
            label.pack(ipadx=1)

    def hide_tooltip(self):
        if self.tip_window:
            self.tip_window.destroy()       

"""
***************************************Tool Tips Ends***********************************
"""
""" 
*****************************************GUI Begins*************************************
"""
win = tk.Tk()   #Initialization of the GUI window
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

frm_choose = ttk.Labelframe(master, text = "1") # Frame 1 - Input Selection
frm_choose.grid(column = 0, row = 0, padx = 10, pady = 20)
btn_choose = ttk.Button(frm_choose, text = "\n Choose PDF file to encrypt \n", command = _get_filename)
btn_choose.pack(padx = 10, pady = 10)
ToolTip(frm_choose, "Select the PDF file that you would like to encrypt")  # Tool tip

frm_pass = ttk.Labelframe(master, text = "2")   # Frame 2 - Password entry
frm_pass.grid(column = 1, row = 0, padx = 10, pady = 2, ipadx = 2, ipady = 8)
lbl_pass = ttk.Label(frm_pass, text = "Set Password:")
lbl_pass.grid(column = 0, row = 0, sticky = "w")

entr_pass = ttk.Entry(frm_pass)
entr_pass.grid(column = 0, row = 1, padx = 8, pady = 10, sticky = "w")
entr_pass.focus()   #Place cursor into password entry line when the app starts
password = entr_pass.get()
ToolTip(frm_pass, "Please enter the password that you \nwould like to have on the encrypted PDF")  # Tool tip

frm_output = ttk.Labelframe(master, text = "3") # Frame 3 - Output Selection
frm_output.grid(column = 2, row = 0, padx = 8, pady = 10, ipadx = 2, ipady = 13)
radVar = tk.IntVar()
rad_output_default = ttk.Radiobutton(frm_output, text = "Save copy to default folder", variable = radVar, value = 1)
rad_output_default.grid(column = 0, row = 0, sticky = "sw", pady = 6)
rad_output_default.invoke()
rad_output_choose = ttk.Radiobutton(frm_output, text = "Save copy to a different folder", variable = radVar, value = 2, command = _different_output)
rad_output_choose.grid(column = 0, row = 1, sticky = "sw")
ToolTip(frm_output, "Please indicate whether you would like the option to choose where the copied encrypted file is saved") # Tool tip

frm_encrypt = ttk.LabelFrame(master, text = "4")    #Frame 4 - Execute
frm_encrypt.grid(column = 3, row = 0, padx = 8, pady = 10)
btn_encrypt = ttk.Button(frm_encrypt, text = "\nEncrypt\n", command = _encrypt_btn)
btn_encrypt.pack(padx = 10, pady = 12)
ToolTip(frm_encrypt, "Press this to begin encryption")  # Tool tip

win.mainloop()
""" 
*****************************************GUI Ends*************************************
"""