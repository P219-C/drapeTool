import numpy as np
import matplotlib.pyplot as plt
from tkinter import *



root = Tk()
root.title('The Log Editor Boss')

e = Entry(root, width=50) # take entry bit.. 
e.pack()
e.insert(0, "type your name") # info to put in the box.. 

def take_entry():
    hello = ' hello  ' + e.get()
    entry1 = Label(root, text = hello)
    entry1.pack()

mybutton3 = Button(root, text='whats your name ', command=take_entry)
mybutton3.pack()


prices = [30,40,50,70,75,65,30,25,50,70,80,100,120,90,91,150,-20,-20,-20]

graphchange = Scale(root, from_=0, to=len(prices))
graphchange.pack()

def graph():
    global prices
    if graphchange.get()==0:
        newprices = prices
    else:
        newprices = prices[:int('-'+str(graphchange.get()))]
    plt.plot(newprices)
    plt.show()


graph_button = Button(root, text='Drag the slider and plot it. ', command=graph)
graph_button.pack()

button_exit = Button(root, text='QUIT', command=root.quit)
button_exit.pack()


root.mainloop()