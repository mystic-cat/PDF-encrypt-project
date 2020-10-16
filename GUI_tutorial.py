# import tkinter as tk

# window = tk.Tk()
# greeting = tk.Label(text = "Hello World") #Will create a text label
# greeting.pack() #Shrinks the window as small as it can 
# window.mainloop() # need this at the end of the python script to create the GUI. It tells Python to run the Tkinter event loop

# window2 = tk.Tk()
# salutation = tk.Label(text = "Hello, and good day!", foreground = "black", background = "white", height = 10, width = 20)
# salutation.pack()
# button = tk.Button(text = "Click me!", width = 11, height = 3, bg = "black", fg = "white")
# button.pack()
# window2.mainloop()

# window3 = tk.Tk()
# label = tk.Label(text = "Name")
# entry = tk.Entry()
# label.pack()
# entry.pack()
# window3.mainloop()

# window4 = tk.Tk()
# label = tk.Label(text = "This is a text widget!",height = 2, width = 25)
# text = tk.Text()
# text.pack()
# label.pack()
# window4.mainloop()

# window5 = tk.Tk()
# frame_a = tk.Frame()
# frame_b = tk.Frame()

# label_a = tk.Label(master = frame_a, text = "I'm in Frame A!")
# label_a.pack()

# label_b = tk.Label(master = frame_b, text = "I'm in Frame B!")
# label_b.pack()

# frame_a.pack()
# frame_b.pack()

# window5.mainloop()


# import tkinter as tk

# border_effects = {
#     "flat" : tk.FLAT,
#     "sunken" : tk.SUNKEN,
#     "raised" : tk.RAISED,
#     "groove" : tk.GROOVE,
#     'ridge' : tk.RIDGE
# }

# window6 = tk.Tk()

# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master = window6, relief = relief, borderwidth = 5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master = frame, text = relief_name)
#     label.pack()
# window6.mainloop()

# import tkinter as tk

# window_7 = tk.Tk()

# frm_1 = tk.Frame(master = window_7, width = 100, height = 100, bg = "red")
# frm_1.pack(fill = tk.X)

# frm_2 = tk.Frame(master = window_7, width = 50, height = 50, bg = "yellow")
# frm_2.pack(fill = tk.X)

# frm_3 = tk.Frame(master = window_7, width = 25, height = 25, bg = "blue")
# frm_3.pack(fill = tk.X)

# window_7.mainloop()

# import tkinter as tk

# window8 = tk.Tk()

# frm1 = tk.Frame(master = window8, height = 100, width = 200, bg = "blue")
# frm1.pack(fill = tk.Y, side = tk.LEFT)

# frm2 = tk.Frame(master = window8, width = 100, bg = "yellow")
# frm2.pack(fill = tk.Y, side = tk.LEFT)

# frm3 = tk.Frame(master = window8, width = 50, bg = "green")
# frm3.pack(fill = tk.Y, side = tk.LEFT)

# window8.mainloop()

# import tkinter as tk

# window9 = tk.Tk()

# frm1 = tk.Frame(master = window9, width = 150, height = 150)
# frm1.pack()

# label1 = tk.Label(master = frm1, text = "I'm at (0,0)", bg = "red")
# label1.place(x=0, y=0)

# label2 = tk.Label(master = frm1, text = "I'm at (75,75)", bg = "blue")
# label2.place(x=75,y=75)

# window9.mainloop()

# import tkinter as tk

# window10 = tk.Tk()

# for i in range(3):
#     window10.columnconfigure(i, weight = 1, minsize = 100)
#     window10.rowconfigure(i, weight = 1, minsize = 100)
#     for j in range(3):
#         frame = tk.Frame(
#             master = window10,
#             relief = tk.RAISED,
#             borderwidth = 2
#         )
#         frame.grid(row = i, column = j, padx = 5, pady = 5)
#         label = tk.Label(master = frame, text = f"Row {i} \nColumn {j}")
#         label.pack(padx = 5, pady = 5)
# window10.mainloop()

# import tkinter as tk

# window11 = tk.Tk()
# window11.columnconfigure(0,minsize = 250)
# window11.rowconfigure([0,1], minsize = 100)

# lbl1 = tk.Label(text = "A")
# lbl1.grid(row=0, column = 0, sticky = "n")

# lbl2 = tk.Label(text = "B")
# lbl2.grid(row = 1, column = 0, sticky = "sw")

# window11.mainloop()

# from tkinter import *
# from tkinter import ttk
# root = Tk()
# l =ttk.Label(root, text="Starting...")
# l.grid()
# l.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
# l.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))
# l.bind('<ButtonPress-1>', lambda e: l.configure(text='Clicked left mouse button'))
# l.bind('<3>', lambda e: l.configure(text='Clicked right mouse button'))
# l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
# l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))
# root.mainloop()

import tkinter as tk

form_criteria = [
    "First Name:",
    "Last Name:",
    "Address Line 1:",
    "Address Line 2:",
    "City:",
    "State/Province:",
    "Postal Code:",
    "Country:"
]

win = tk.Tk()
win.columnconfigure([0,1,2,3], minsize = 100, weight = 1)
# win.rowconfigure(0, minsize = 100, weight = 1)
win.title("Address Entry Form")

for index, criteria in enumerate(form_criteria):
    frm_criteria = tk.Frame(master = win)
    frm_criteria.grid(row = index, column = 0, sticky = 'e')
    lbl_criteria = tk.Label(master = frm_criteria, text = criteria)
    lbl_criteria.pack()
    frm_ent_criteria = tk.Frame(master = win)
    frm_ent_criteria.grid(row = index, column = 1)
    ent_criteria = tk.Entry(master = frm_ent_criteria)
    ent_criteria.pack()
win.mainloop()


