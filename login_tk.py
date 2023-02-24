# sing up page with tkinter 

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import sqlite3

root = ttk.Window(themename="cosmo") 
root.title("Log In")
root.iconbitmap("D:\mycode\Tkinter\icons8-punisher-128.ico")
root.geometry('925x500+300+200')
root.resizable(False,False)


# backend

mydb= sqlite3.connect('userdata.db')
# make curser 
curser =mydb.cursor()

# querys

q1="""CREATE TABLE userdata(
    username text NOT NULL PRIMARY KEY,
    password text NOT NULL
   );"""

q2="SELECT * FROM userdata"

# functions 

def userin():
    username=user.get()
    password=passwd.get()
    
    curser.execute("SELECT username,password FROM userdata")
    list=curser.fetchall()
    if (username,password) in list:
        messagebox.showinfo("Successful","Successful Login!")
    else:
        messagebox.showerror("Error","Invalid Input!")

def sign_in():
    signup_button.config(text='SING IN')
    c_passwd.delete(0,'end')
    c_passwd.insert(0,'******')
    c_passwd.config(state='disabled')
    messagebox.showinfo("Info","Enter Username and Password")
    signup_button.config(command=userin)
    
    
# forntend 

def on_in(e):
    user.delete(0,'end')
    
def on_out(e):
    if user.get() == '':
        user.insert(0,'USERNAME')

def sign_up():
    
    username=user.get()
    password=passwd.get()
    c_password=c_passwd.get()
    print(username,password,c_password)

    if password==c_password and username!='': 
        try:
            curser.execute("INSERT INTO userdata(username,password) VALUES(?,?)",(username,password))
            mydb.commit()
            messagebox.showinfo("Successful","Successful Login!")
            print('cool')
        except:
            messagebox.showerror("Error","Username Already Exists!")
    else:
        messagebox.showerror("Error","Invalid Input!")

# background image

im = ttk.PhotoImage(file="D:\mycode\images\login-1.png")
ttk.Label(root,image=im,border=0,background='white').place(x=50,y=90)

# frame

frame=ttk.Frame(root,width=350,height=390,bootstyle='default')
frame.place(x=480,y=50)

# heading label

heading =ttk.Label(frame,text='Sing Up',foreground='#57a1f8',background='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

# entry widgets

user = ttk.Entry(frame,width=25,foreground='black',font=('Microsoft Yahei UI Light',11),bootstyle='light')
user.place(x=30,y=80)
user.insert(0,'USERNAME')
user.bind("<FocusIn>",on_in)
user.bind("<FocusOut>",on_out)

ttk.Separator(frame,bootstyle='info',orient=HORIZONTAL).place(x=25,y=118,relwidth=0.9)

def on_in(e):
    passwd.delete(0,'end')
    
def on_out(e):
    if passwd.get() == '':
        passwd.insert(0,'PASSWORD')

passwd = ttk.Entry(frame,width=25,foreground='black',font=('Microsoft Yahei UI Light',11),bootstyle='light')
passwd.place(x=30,y=150)
passwd.insert(0,'PASSWORD')
passwd.bind("<FocusIn>",on_in)
passwd.bind("<FocusOut>",on_out)

ttk.Separator(frame,bootstyle='info',orient=HORIZONTAL).place(x=25,y=185,relwidth=0.9)

def on_in(e):
    c_passwd.delete(0,'end')
    
def on_out(e):
    if c_passwd.get() == '':
        c_passwd.insert(0,'CONFORM PASSWORD')

c_passwd = ttk.Entry(frame,width=25,foreground='black',font=('Microsoft Yahei UI Light',11),bootstyle='light')
c_passwd.place(x=30,y=220)
c_passwd.insert(0,'CONFORM PASSWORD')
c_passwd.bind("<FocusIn>",on_in)
c_passwd.bind("<FocusOut>",on_out)

ttk.Separator(frame,bootstyle='info',orient=HORIZONTAL).place(x=25,y=253,relwidth=0.9)

# buttons

signup_button = ttk.Button(frame,width=30,text='SING UP',bootstyle='primary',command=sign_up)
signup_button.place(x=35,y=280)

leble = ttk.Label(frame,text="I Have An Account",bootstyle='dark',font=('Microsoft Yahei UI Light',10))
leble.place(x=75,y=340)

singin=ttk.Button(frame,width=6,text='Sing In',bootstyle='primary,outline',command=sign_in)
singin.place(x=225,y=335)

root.mainloop()