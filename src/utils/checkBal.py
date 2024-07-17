from tkinter import *

def checkBal(user_window,con):
    check_bal=Toplevel(user_window)
    check_bal.title("CHECK BALANCE")
    label=Label(check_bal,bg="yellow",fg="red",text="Fill the details required to check your balance",justify=LEFT,font='arabic').grid(column=0,row =0)
    check_bal.geometry('600x500')
    
    account_number=Label(check_bal,text="Account Number (four digits) :",justify=LEFT)
    account_number.grid(column=0,row=3)    
    uacno=StringVar()
    e2=Entry(check_bal,textvariable=uacno,justify=LEFT).grid(row=3,column=1) 

    Password=Label(check_bal,text="Password :",justify=LEFT)
    Password.grid(column=0,row=4)       
    upasswd=StringVar()
    e5=Entry(check_bal,textvariable=upasswd,justify=LEFT,show="*").grid(row=4,column=1) 

    def close():
        check_bal.destroy()
    def save():
        try:
            b = "select PASSWORD from SECURED where ACNO= %s"
            data = (int(uacno.get()),)
            c = con.cursor()
            c.execute(b, data)
            if upasswd.get() == c.fetchone()[0]:
                a = "select OPENING_BALANCE from ACCOUNT where ACNO= %s"
                data = (int(uacno.get()),)
                c = con.cursor()
                c.execute(a, data)
                balance=c.fetchone()[0]
            else:
                msg=Label(check_bal,text="Wrong credentials...\n or Account didn't exist...\n Click on close button to close the window...",fg="red").grid(row=8,column=1)
                button00=Button(check_bal,text="Close",command=close).grid(column=1,row=13)                
                       
            msg=Label(check_bal,text=f"Your current balance is {balance}....\n Click on close button to close the window... ",fg="green").grid(row=8,column=1)
            button00=Button(check_bal,text="Close",command=close).grid(column=1,row=13)
            
        except Exception as e:
            msg=Label(check_bal,text="Wrong credentials...\n or Account didn't exist...\n Click on close button to close the window...",fg="red").grid(row=8,column=1)
            button00=Button(check_bal,text="Close",command=close).grid(column=1,row=13)

    button=Button(check_bal,text="Submit",command=save).grid(column=1,row=6)
    check_bal.mainloop()
