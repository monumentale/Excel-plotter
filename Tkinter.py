__author__ = 'Dania'
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import pandas as pd
import textwrap
from tkinter.filedialog import askopenfilename

from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
import numpy as np
import matplotlib.pyplot as plt

global filename
global textBox
class mclass:
    def __init__(self,  window):
        self.window = window
        # self.box = Entry(window)
        self.button = Button (window, text="plot", command=self.plot)
        # self.box.pack ()
        self.button.pack()

    def plot (self):
        var = pd.read_excel(filename)
        print(var)
        x = list(var['Easting'])
        y = list(var['Northing'])
        # x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        # v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
        # p= np.array ([16.23697,17.31653,17.22094,17.68631,17.73641 ,18.6368,19.32125,19.31756 ,21.20247,22.41444,22.11718,22.12453])

        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.scatter(x,y,color='red',s=10)
        # a.style.use('seaborn')
        # a.fill([9.283336,7.566295,8.849375,10.689882,11.767467 ], [ 10.611051,7.798551,5.842984,5.930875,7.996305],edgecolor='r', fill=False)
        # a.fill(x, y,edgecolor='r', fill=False)
        # for plotting closed boundary
        # plt.fill(lon, lat, edgecolor='r', fill=False)
        a.invert_yaxis()
        inputValue=textBox.get("1.0","end-1c") 
        a.set_title (inputValue, fontsize=16)
        a.set_ylabel("EASTING", fontsize=14)
        a.set_xlabel("Northing", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()
        UseData()
        
def UseData():
    var = pd.read_excel(filename)
    print(var)
    x = list(var['Easting'])
    y = list(var['Northing'])
    plt.figure(1)
    plt.scatter(x,y,color='red',s=10)
    # plt.fill(x, y,edgecolor='r', fill=False)
    inputValue=textBox.get("1.0","end-1c")
     
    # plt.set_title (inputValue, fontsize=16)
    # plt.set_ylabel("EASTING", fontsize=14)
    # plt.set_xlabel("Northing", fontsize=14)
    # plt.title('Variable')
    # plt.ylabel('Some Units')
    # plt.xlabel('More Units')
    plt.tight_layout()
    result = messagebox.askyesno("Window-1", "Data processed. \nWould you like to save the figure?")
    if result== True:
        a = asksaveasfilename(filetypes=(("PDF FILE", "*.pdf"),("All Files", "*.*")), 
            defaultextension='.pdf', title="Window-2")
        if a:
            plt.savefig(a)
            messagebox.showinfo("Window-3", "Plot Saved.") # Conf. message of saving  
            
           
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
window= Tk()
textBox=Text(window, height=2, width=10)
textBox.pack()
start= mclass (window)
window.mainloop()



        
