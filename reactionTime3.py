# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 16:54:42 2022

@author: ibroh
"""
import tkinter as tk
import time 
import random
from tkinter import ttk
from tkinter.messagebox import askretrycancel, showinfo
import os

window = tk.Tk()
window.title("Reaction Time")

def restart():
    window.destroy()
    os.startfile("reactionTime.pyw")
  

canvas = tk.Canvas(master = window, width = 600, height = 300)
canvas.grid(columnspan = 3, rowspan = 3)


instructions = tk.Label(master = window, 
                        text = "Please, press the GO button as soon as possible", 
                        font = "Raleway")
instructions.grid(columnspan=3, column = 0, row =1)

def confirm():
    answer = askretrycancel(
        title='Start the game',
        message='Do you want to restart?'
    )
    if answer:
        showinfo(
            title='Information',
            message='The game is restarting.')
        restart()     


tk.Button(
    window,
    text='Try Again',
    font = "Raleway", 
    bg = "#20bebe", 
    fg= "white", 
    height =2, 
    width =15,
    command=confirm).grid(column =1, row =3)

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def calculateTime(goButton):
    global reactionTime
    global endTime
    global startTime
    goButton.grid_forget()
    endTime = time.time()
    reactionTime = endTime - startTime
    result = truncate(reactionTime, 3)
    instructions = tk.Label(master = window, 
                            text = "Your reaction time is " + str(result) + "ms", 
                            font = "Raleway")
    instructions.grid(columnspan=3, column = 0, row =2)
    
    

def call(button):
    global startTime
    global randomTime
    randomTime = random.uniform(0.25, 3.0)
    time.sleep(randomTime)
    Button1.grid_forget()
    goButton.grid(column = 1, row = 2)
    startTime = time.time()
    
def clickMe(button):
    buttonText.set("Ready???")
    call(goButton)
    


buttonText = tk.StringVar()    
Button1 = tk.Button(
    master = window,
    textvariable = buttonText,
    command= lambda: clickMe(Button1), 
    font = "Raleway", 
    bg = "#20bebe", 
    fg= "white", 
    height =2, 
    width =15)
buttonText.set("Ready?")
Button1.grid(column = 1, row = 2)


goButton = tk.Button(
    master = window, 
    text ="GO", 
    command = lambda: calculateTime(goButton), 
    font = "Raleway", 
    bg = "#20bebe", 
    fg= "white", 
    height =2, 
    width =15)




window.mainloop()
