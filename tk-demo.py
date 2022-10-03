from tkinter import *

master = Tk()

master.geometry("800x600")

colors = ["green", "red", "blue", "purple"]
ndx = 0
def changeColors (event = None):
    global master
    global colors
    global ndx
    master.configure(background= colors[ndx])
    ndx += 1
    ndx = ndx % len(colors)
    master.after(100, changeColors)
    
master.after(100, changeColors)
mainloop()
