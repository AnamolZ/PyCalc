#Lib
import customtkinter
import tkinter as tk
import tkinter.messagebox

#Theme
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

#Geometry Section 
app = customtkinter.CTk()
app.title("MAS-COMPUTE")
app.geometry("340x450")
app.minsize(340, 450)
app.maxsize(340, 450)

#Display Frame
frame = customtkinter.CTkFrame(master=app,width=450,height=190,fg_color="#161A22")
frame.place(relx=0, rely=0)

#screen_display
entry=customtkinter.CTkEntry(width=340,fg_color="#161A22",border_color="#161A22",text_font="serif 20 bold")
entry.pack(ipadx=50,ipady=20,pady=60)

# function
def click(number):
    entry.insert(tk.END, number)
 
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tk.messagebox.showinfo("Error", "Syntax Error")
 
def clear():
    entry.delete(0, tk.END)

#1F2A3B
frame_box = customtkinter.CTkFrame(master=app,width=450,height=530,fg_color="#0D1017")
frame_box.place(relx=0,rely=0.43)

#these functions are ordred in coloumn form
def first(fix):
    cancle_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="C",fg_color="#CC575D",command=clear)
    cancle_button.place(relx=fix, rely=0.45)
    seven_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="7",fg_color="#1F2A3B",command=lambda:click(7))
    seven_button.place(relx=fix, rely=0.56)
    four_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="4",fg_color="#1F2A3B",command=lambda:click(4))
    four_button.place(relx=fix, rely=0.67)
    one_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="1",fg_color="#1F2A3B",command=lambda:click(1))
    one_button.place(relx=fix, rely=0.78)
    zero_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="0",fg_color="#1F2A3B",command=lambda:click(0))
    zero_button.place(relx=fix, rely=0.89)

def second(sx):    
    left_bracket_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="(",fg_color="#1F2A3B",command=lambda:click('('))
    left_bracket_button.place(relx=sx, rely=0.45)
    eight_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="8",fg_color="#1F2A3B",command=lambda:click(8))
    eight_button.place(relx=sx, rely=0.56)
    five_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="5",fg_color="#1F2A3B",command=lambda:click(5))
    five_button.place(relx=sx, rely=0.67)
    two_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="2",fg_color="#1F2A3B",command=lambda:click(2))
    two_button.place(relx=sx, rely=0.78)
    dot_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text=".",fg_color="#1F2A3B",command=lambda:click('.'))
    dot_button.place(relx=sx, rely=0.89)

def third(tx):
    right_bracket_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text=")",fg_color="#1F2A3B",command=lambda:click(')'))
    right_bracket_button.place(relx=tx, rely=0.45)
    nine_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="9",fg_color="#1F2A3B",command=lambda:click(9))
    nine_button.place(relx=tx, rely=0.56)
    six_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="6",fg_color="#1F2A3B",command=lambda:click(6))
    six_button.place(relx=tx, rely=0.67)
    three_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="3",fg_color="#1F2A3B",command=lambda:click(3))
    three_button.place(relx=tx, rely=0.78)
    per_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="%",fg_color="#1F2A3B",command=lambda:click('*1/100'))
    per_button.place(relx=tx, rely=0.89)

def fourth(ox):
    mod_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="mod",fg_color="#1F2A3B",command=lambda:click('%'))
    mod_button.place(relx=ox, rely=0.45)
    divide_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="÷",fg_color="#1F2A3B",command=lambda:click('/'))
    divide_button.place(relx=ox, rely=0.56)
    mul_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="x",fg_color="#1F2A3B",command=lambda:click('*'))
    mul_button.place(relx=ox, rely=0.67)
    sub_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="-",fg_color="#1F2A3B",command=lambda:click('-'))
    sub_button.place(relx=ox, rely=0.78)
    add_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="+",fg_color="#1F2A3B",command=lambda:click('+'))
    add_button.place(relx=ox, rely=0.89)

def fifth(fx):
    pi_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="π",fg_color="#1F2A3B",command=lambda:click('22/7'))
    pi_button.place(relx=fx, rely=0.45)
    root_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="√",fg_color="#1F2A3B",command=lambda:click('0.5'))
    root_button.place(relx=fx, rely=0.56)
    sqr_button = customtkinter.CTkButton(master=app,width=60,height=45,border_width=0,corner_radius=8,text="x²",fg_color="#1F2A3B",command=lambda:click('**2'))
    sqr_button.place(relx=fx, rely=0.67)
    equal_button = customtkinter.CTkButton(master=app,width=60,height=95,border_width=0,corner_radius=8,text="=",fg_color="#1F2A3B",command=equal)
    equal_button.place(relx=fx, rely=0.78)

first(0.05)
second(0.23)
third(0.41)
fourth(0.59)
fifth(0.77)

app.mainloop()
