"""
Ibrahim Pulatov
Professor Talaga
CSCI-420
9/13/2022
Homework_2_GUI_stopWatch
Extra Credit
"""

"""
In this code I could not implement timer functionality,
but did stopWatch functionality

"""


import tkinter as tk


global running
count =0


class stopWatch():
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Stop Watch")
        self.window.geometry("600x200")
        self.text_counter = tk.StringVar()
        self.text_counter.set("00:00:00")
        self.myLabel = tk.Label(self.window,textvariable=self.text_counter,font="Raleway",bg="#E39FF6")
        self.start_btn = tk.Button(self.window,text="Start",command=self.start,font="Raleway",bg="#E39FF6")
        self.stop_btn = tk.Button(self.window,text="Stop",command=self.stop,font="Raleway",bg="#E39FF6")
        self.reset_btn = tk.Button(self.window,text="Reset",command=self.reset,font="Raleway",bg="#E39FF6")
        self.exit_btn =tk. Button(self.window, text="Exit", command=self.close,font="Raleway",bg="#E39FF6")
        self.myLabel.place(x=240,y=10)
        self.start_btn.place(x=120,y=100)
        self.stop_btn.place(x=220,y=100)
        self.reset_btn.place(x=320,y=100)
        self.exit_btn.place(x=420,y=100)
        self.label = tk.Label(self.window,text="",font=("Raleway 40 bold"))
        self.window.configure(bg='white')
        self.window.mainloop()
        
    def reset(self):
        global count
        count=1
        self.text_counter.set('00:00:00')    
        
    def start(self):
        global count
        count=0
        self.timer() 
        
    def stop(self):
        global count
        count=1
        
    def close(self):
        self.window.destroy()
        
    def timer(self):
        global count
        if(count==0):
            self.current_info = str(self.text_counter.get())
            h,m,s = map(int,self.current_info.split(":")) 
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    m=0
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.current_info=h+":"+m+":"+s           
            self.text_counter.set(self.current_info)
            
            if(count==0):
                self.window.after(1000,self.timer) 
                
    
stopWatch()      