from tkinter import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
 # now import pylustrator
# import pylustrator
 
#  # activate pylustrator
# pylustrator.start()



data1 = {'Country': ['US','CA','GER','UK','FR'],
         'GDP_Per_Capita': [45000,42000,52000,49000,47000]
        }
df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita'])


data2 = {'Year': [9.283336,7.566295,8.849375,10.689882,11.767467 ],
         'Unemployment_Rate': [ 10.611051,7.798551,5.842984,5.930875,7.996305]
        }
# for plotting closed boundary
# plt.fill(lon, lat, edgecolor='r', fill=False)
# 9.283336, 10.611051,
# 7.566295, 7.798551,
# 8.849375, 5.842984,
# 10.689882, 5.930875,
# 11.767467, 7.996305


df2 = DataFrame(data2,columns=['Year','Unemployment_Rate'])


data3 = {'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5,5],
         'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565,1500]
        }  
df3 = DataFrame(data3,columns=['Interest_Rate','Stock_Index_Price'])


root=Tk() 

figure1 = plt.Figure(figsize=(6,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')

figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=LEFT, fill=BOTH)
df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
# for plotting closed boundary
# plt.fill(lon, lat, edgecolor='r', fill=False)
ax2.set_title('Year Vs. Unemployment Rate')

# plt.fill([5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5,5], [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565,1500], edgecolor='r', fill=False)

figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Interest_Rate'],df3['Stock_Index_Price'], color = 'g')
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=LEFT, fill=BOTH)
ax3.legend(['Stock_Index_Price']) 
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Stock Index Price')

# for plotting closed boundary
# plt.fill(lon, lat, edgecolor='r', fill=False)


root= Tk() 
  


def got_clicked():
   
   print("I got clicked!")

my_button = Button(text="Click me", command=got_clicked)
my_button.pack()

root.mainloop()