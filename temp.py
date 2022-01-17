# Import required libraries
from tkinter import *
from tkinter import ttk
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create an instance of tkinter frame      pyinstaller.exe --onefile --icon=myicon.ico Tkinter.py
win= Tk()

# Set the window size
win.geometry("700x350")

# Use TkAgg
matplotlib.use("TkAgg")

# Create a figure of specific size
figure = Figure(figsize=(3, 3), dpi=100)

# Define the points for plotting the figure
plot = figure.add_subplot(1, 1, 1)
plot.plot(0.5, 0.3, color="blue", marker="o", linestyle="")

# Define Data points for x and y axis
x = [0.2,0.5,0.8,1.0 ]
y = [ 1.0, 1.2, 1.3,1.4]
plot.plot(x, y, color="red", marker="x", linestyle="")

# Add a canvas widget to associate the figure with canvas
canvas = FigureCanvasTkAgg(figure, win)
canvas.get_tk_widget().grid(row=0, column=0)

win.mainloop()

from tkinter import * # all modules imported, most remain unused atm
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk

def UseData():
    data1, data2 = OpenFile()
    plt.figure(1)
    plt.plot(data1, data2)
    plt.title('Variable')
    plt.ylabel('Some Units')
    plt.xlabel('More Units')
    plt.tight_layout()
    result = messagebox.askyesno("Window-1", "Data processed. \nWould you like to save the figure?")
    if result== True:
        asksaveasfile(filetypes=(("PNG Image", "*.png"),("All Files", "*.*")), 
            defaultextension='.png', title="Window-2")
        # a = 'picture.png'
        # plt.savefig(a)
        messagebox.showinfo("Window-3", "Plot Saved.") # Conf. message of saving



//////////////////////////////////////////////

 # import matplotlib and numpy as usual
import matplotlib.pyplot as plt
import numpy as np
 
 # now import pylustrator
import pylustrator
 
 # activate pylustrator
pylustrator.start()
 # build plots as you normally would
np.random.seed(1)
t = np.arange(0.0, 2, 0.001)
y = 2 * np.sin(np.pi * t)
a, b = np.random.normal(loc=(5., 3.), scale=(2., 4.), size=(100,2)).T
b += a

plt.figure(1)
plt.subplot(131)
plt.plot(t, y)

plt.subplot(132)
plt.plot(a, b, "o")

plt.subplot(133)
plt.bar(0, np.mean(a))
plt.bar(1, np.mean(b))

# show the plot in a pylustrator window
plt.show()