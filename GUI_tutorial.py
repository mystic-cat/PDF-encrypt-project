import tkinter as tk

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

window3 = tk.Tk()
label = tk.Label(text = "Name")
entry = tk.Entry()
label.pack()
entry.pack()
window3.mainloop()
