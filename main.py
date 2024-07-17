from tkinter import *

import mysql.connector as a
con = a.connect(host="localhost", user="root", passwd="3557", database="bank")

from src.UI.user_options import user_options
from src.UI.admin_options import admin_options

def main():
    global main_window
    main_window=Tk()
    main_window.title("BANK MANAGEMENT")
    main_window.geometry('600x300')
    l1=Label(main_window,text="Welcome to Bank....... ",bg="yellow",fg="blue",font=('arabic 32 '),justify=CENTER).grid(column=0,row =0)

    option=Label(main_window,text="LOGIN AS USER",justify=RIGHT)
    option.grid(column=0,row=1)
    main_button=Button(main_window,text="User Login",justify=LEFT,command=user_options(main_window)).grid(column=1,row=1)

    option1=Label(main_window,text="LOGIN AS ADMINISTRATOR",justify=RIGHT)
    option1.grid(column=0,row=2)
    main_button1=Button(main_window,text="Admin Login",justify=LEFT,command=admin_options(main_window,con)).grid(column=1,row=2)
    main_window.mainloop()
  
main()    
