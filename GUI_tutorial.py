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

window5 = tk.Tk()
frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master = frame_a, text = "I'm in Frame A!")
label_a.pack()

label_b = tk.Label(master = frame_b, text = "I'm in Frame B!")
label_b.pack()

frame_a.pack()
frame_b.pack()

window5.mainloop()
