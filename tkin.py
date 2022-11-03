from tkinter import *
from tkinter import ttk
import math
window=Tk()
window.title("Calculator")
window.geometry("300x350")
entry=Entry(width=38,borderwidth=5)
entry.pack()
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


B1= Button( text="1",padx=20,pady=20).grid(row=3,column=0)
B2= Button( text="2",padx=20,pady=20).grid(row=3,column=1)
B3= Button( text="3",padx=20,pady=20).grid(row=3,column=2)

B4= Button( text="4",padx=20,pady=20).grid(row=2,column=0)
B5= Button( text="5",padx=20,pady=20).grid(row=2,column=1)
B6= Button( text="6",padx=20,pady=20).grid(row=2,column=2)

B7= Button( text="7",padx=20,pady=20).grid(row=1,column=0)
B8= Button( text="8",padx=20,pady=20).grid(row=1,column=1)
B9= Button( text="9",padx=20,pady=20).grid(row=1,column=2)

B0= Button( text="0",padx=20,pady=20).grid(row=4,column=0)
BAdd= Button( text="+",padx=20,pady=20).grid(row=4,column=1)
BSub= Button( text="-",padx=20,pady=20).grid(row=4,column=2)

BMul= Button( text="*",padx=20,pady=20).grid(row=5,column=0)
BDiv= Button( text="/",padx=20,pady=20).grid(row=5,column=1)
BEqual= Button( text="=",padx=20,pady=20).grid(row=5,column=2)

window.mainloop()