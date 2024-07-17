from tkinter import *

def withAmo(user_window,con):
    withdraw=Toplevel(user_window)
    withdraw.title("WITHDRAW AMOUNT")
    label=Label(withdraw,bg="yellow",fg="red",text="Fill the details required to withdraw the amount",justify=LEFT,font='arabic').grid(column=0,row =0)
    withdraw.geometry('600x500')
    
    account_number=Label(withdraw,text="Account Number (four digits) :",justify=LEFT)
    account_number.grid(column=0,row=3)    
    uacno=StringVar()
    e2=Entry(withdraw,textvariable=uacno,justify=LEFT).grid(row=3,column=1) 

    amount=Label(withdraw,text="Amount in Rupees :",justify=LEFT)
    amount.grid(column=0,row=4)    
    uamo=StringVar()
    e2=Entry(withdraw,textvariable=uamo,justify=LEFT).grid(row=4,column=1)

    Password=Label(withdraw,text="Password :",justify=LEFT)
    Password.grid(column=0,row=5)       
    upasswd=StringVar()
    e5=Entry(withdraw,textvariable=upasswd,justify=LEFT,show="*").grid(row=5,column=1)

    def close():
        withdraw.destroy()
    def save():
        count=1
        try:
            b = "select Password from SECURED where ACNO=%s"
            data = (int(uacno.get()),)
            c = con.cursor()
            c.execute(b, data)
            if upasswd.get() == c.fetchone()[0]:
                a = "select OPENING_BALANCE from ACCOUNT where ACNO = %s"
                data = (int(uacno.get()),)
                c = con.cursor()
                c.execute(a, data)
                tam = c.fetchone()[0]-int(uamo.get())
                if tam > 0:
                    sql = "update ACCOUNT set OPENING_BALANCE= %s where ACNO =%s"
                    d = (tam, int(uacno.get()))
                    c.execute(sql, d)
                    con.commit()
                else:
                    count=-1
                    msg=Label(withdraw,text="Current balance is lower than withdraw amount...\n Click on close button to close the window...",fg="red").grid(row=8,column=1)
                    button00=Button(withdraw,text="Close",command=close).grid(column=1,row=13)
            else:
                count=-1
                msg=Label(withdraw,text="Incorrect Password...\n Click on close button to close the window...",fg="red").grid(row=8,column=1)
                button00=Button(withdraw,text="Close",command=close).grid(column=1,row=13)     
            if count==1:
                msg=Label(withdraw,text=f"Amount Withdrawn....\n Click on close button to close the window... ",fg="green").grid(row=8,column=1)
                button00=Button(withdraw,text="Close",command=close).grid(column=1,row=13)
            
        except Exception as e:
            msg=Label(withdraw,text="Incorrect Credentials or.....\n Some error occoured\n Click on close button to close the window...",fg="red").grid(row=8,column=1)
            button00=Button(withdraw,text="Close",command=close).grid(column=1,row=13)

    button=Button(withdraw,text="Submit",command=save).grid(column=1,row=6)
    withdraw.mainloop()
