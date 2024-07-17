from tkinter import *

def depoAmo(user_window,con):
    depo_amo=Toplevel(user_window)
    depo_amo.title("DEPOSIT AMOUNT")
    label=Label(depo_amo,bg="yellow",fg="red",text="Fill the details required to deposit the amount",justify=LEFT,font='arabic').grid(column=0,row =0)
    depo_amo.geometry('600x500')
    
    account_number=Label(depo_amo,text="Account Number (four digits) :",justify=LEFT)
    account_number.grid(column=0,row=3)    
    uacno=StringVar()
    e2=Entry(depo_amo,textvariable=uacno,justify=LEFT).grid(row=3,column=1) 

    amount=Label(depo_amo,text="Amount in Rupees :",justify=LEFT)
    amount.grid(column=0,row=4)    
    uamo=StringVar()
    e2=Entry(depo_amo,textvariable=uamo,justify=LEFT).grid(row=4,column=1)


    def close():
        depo_amo.destroy()
    def save():
        try:
            if int(uamo.get())<0:
                msg=Label(depo_amo,text="Amount not deposited.....\n Some error occoured\n Click on close button to close the window...",fg="red").grid(row=8,column=1)
                button00=Button(depo_amo,text="Close",command=close).grid(column=1,row=13)            
            else:                
                a = "select OPENING_BALANCE from ACCOUNT where ACNO = %s"
                data = (int(uacno.get()),)
                c = con.cursor()
                c.execute(a, data)
                tam = c.fetchone()[0]+int(uamo.get())
                df = int(tam)
                sql = "update ACCOUNT set OPENING_BALANCE=%s where ACNO=%s"
                d = (df, int(uacno.get()))
                c.execute(sql, d)
                con.commit()                
                msg=Label(depo_amo,text=f"Amount deposited....\n Click on close button to close the window... ",fg="green").grid(row=8,column=1)
                button00=Button(depo_amo,text="Close",command=close).grid(column=1,row=13)
            
        except Exception as e:
            msg=Label(depo_amo,text="Amount not deposited.....\n Some error occoured\n Click on close button to close the window...",fg="red").grid(row=8,column=1)
            button00=Button(depo_amo,text="Close",command=close).grid(column=1,row=13)

    button=Button(depo_amo,text="Submit",command=save).grid(column=1,row=6)
    depo_amo.mainloop()
