from tkinter import *

def closeAcc(user_window,con):
    close_acc=Toplevel(user_window)
    close_acc.title("CLOSE ACCOUNT")
    label=Label(close_acc,bg="yellow",fg="red",text="Fill the details required to close your account",justify=LEFT,font='arabic').grid(column=0,row =0)
    close_acc.geometry('600x500')
    
    account_number=Label(close_acc,text="Account Number (four digits) :",justify=LEFT)
    account_number.grid(column=0,row=3)    
    uacno=StringVar()
    e2=Entry(close_acc,textvariable=uacno,justify=LEFT).grid(row=3,column=1) 

    Password=Label(close_acc,text="Password :",justify=LEFT)
    Password.grid(column=0,row=4)       
    upasswd=StringVar()
    e5=Entry(close_acc,textvariable=upasswd,justify=LEFT,show="*").grid(row=4,column=1) 

    def close():
        close_acc.destroy()
    def save():
        try:
            b = "select PASSWORD from SECURED where ACNO= %s"
            data = (int(uacno.get()),)
            c = con.cursor()
            c.execute(b, data)
            if upasswd.get() == c.fetchone()[0]:
                sql1 = "delete from ACCOUNT where ACNO =%s"
                sql2 = "delete from SECURED where ACNO= %s"
                data = (int(uacno.get()),)
            c = con.cursor()
            c.execute(sql1, data)
            c.execute(sql2, data)
            con.commit()
            msg=Label(close_acc,text="Data deleted Successfully ......\n Click on close button to close the window...",fg="green").grid(row=8,column=1)
            button00=Button(close_acc,text="Close",command=close).grid(column=1,row=13)
            
        except Exception as e:
            msg=Label(close_acc,text="Wrong credentials...\n or Account didn't exist...\n Click on close button to close the window...",fg="red").grid(row=8,column=1)
            button00=Button(close_acc,text="Close",command=close).grid(column=1,row=13)

    button=Button(close_acc,text="Submit",command=save).grid(column=1,row=6)
    close_acc.mainloop()