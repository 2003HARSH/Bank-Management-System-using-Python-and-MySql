from tkinter import *

from src.utils.openAcc import openAcc
from src.utils.checkBal import checkBal
from src.utils.depoAmo import depoAmo
from src.utils.withAmo import withAmo
from src.utils.closeAcc import closeAcc

def user_options(main_window):
    global user_window
    user_window=Toplevel(main_window)
    user_window.title("USER OPTIONS")
    user_window.geometry('600x400')
    l1=Label(user_window,text="Choose options to continue....... ",bg="yellow",fg="blue",font=('arabic 25 '),justify=CENTER).grid(column=0,row =0)

    option=Label(user_window,text="TO OPEN A NEW ACCOUNT ",justify=RIGHT)
    option.grid(column=0,row=2)
    button=Button(user_window,text="click here",justify=LEFT,command=openAcc).grid(column=1,row=2)

    option1=Label(user_window,text="TO DEPOSIT MONEY ",justify=RIGHT)
    option1.grid(column=0,row=3)
    button1=Button(user_window,text="click here",justify=LEFT,command=depoAmo).grid(column=1,row=3)

    option2=Label(user_window,text="TO WITHDRAW MONEY ",justify=RIGHT)
    option2.grid(column=0,row=4)
    button2=Button(user_window,text="click here",justify=LEFT,command=withAmo).grid(column=1,row=4)

    option3=Label(user_window,text=" TO CHECK BALANCE ",justify=RIGHT)
    option3.grid(column=0,row=5)
    button3=Button(user_window,text="click here",justify=LEFT,command=checkBal).grid(column=1,row=5)    

    option4=Label(user_window,text="TO CLOSE ACCOUNT  ",justify=RIGHT)
    option4.grid(column=0,row=6)
    button4=Button(user_window,text="click here",justify=LEFT,command=closeAcc).grid(column=1,row=6)
    user_window.mainloop()