from tkinter import *

def openAcc(user_window,con):
    open_acc=Toplevel(user_window)
    open_acc.title("OPEN ACCOUNT")
    label=Label(open_acc,bg="yellow",fg="red",text="Fill the details required to open your account",justify=LEFT,font='arabic').grid(column=0,row =0)
    open_acc.geometry('600x500')
    
    name=Label(open_acc,text="Name :",justify=LEFT)
    name.grid(column=0,row=2)
    uname=StringVar()
    e1=Entry(open_acc,textvariable=uname,justify=LEFT).grid(row=2,column=1)

 
    account_number=Label(open_acc,text="Account Number (four digits) :",justify=LEFT)
    account_number.grid(column=0,row=3)    
    uacno=StringVar()
    e2=Entry(open_acc,textvariable=uacno,justify=LEFT).grid(row=3,column=1)    
    
    dob=Label(open_acc,text="DOB (YYYY-MM-DD):",justify=LEFT)
    dob.grid(column=0,row=4)    
    udob=StringVar()
    e3=Entry(open_acc,textvariable=udob,justify=LEFT).grid(row=4,column=1)    
    
    Phone_number=Label(open_acc,text="Phone Number :",justify=LEFT)
    Phone_number.grid(column=0,row=5)    
    uphno=StringVar()
    e4=Entry(open_acc,textvariable=uphno,justify=LEFT).grid(row=5,column=1)     
    
    opening_balance=Label(open_acc,text="Opening Balance :",justify=LEFT)
    opening_balance.grid(column=0,row=6) 
    uopbal=StringVar()
    e5=Entry(open_acc,textvariable=uopbal,justify=LEFT).grid(row=6,column=1)    
    
    Password=Label(open_acc,text="Password :",justify=LEFT)
    Password.grid(column=0,row=7)       
    upasswd=StringVar()
    e5=Entry(open_acc,textvariable=upasswd,justify=LEFT,show="*").grid(row=7,column=1)    

    Address=Label(open_acc,text="Address :",justify=LEFT)
    Address.grid(column=0,row=8)       
    uaddr=StringVar()
    e5=Entry(open_acc,textvariable=uaddr,justify=LEFT).grid(row=8,column=1)

    def close():
        open_acc.destroy()
    def save():
        try:
            data1 = (int(uacno.get()), uname.get(), udob.get(), uphno.get(), uaddr.get(), int(uopbal.get()))
            data2 = (int(uacno.get()), upasswd.get())        
            sql1 = 'insert into ACCOUNT values(%s,%s,%s,%s,%s,%s)'
            sql2 = 'insert into SECURED values(%s,%s)'
            c = con.cursor()
            c.execute(sql1, data1)
            c.execute(sql2, data2)
            con.commit()
            msg=Label(open_acc,text="Data entered Successfully ......\n Click on close button to close the window...",fg="green").grid(row=12,column=1)
            button00=Button(open_acc,text="Close",command=close).grid()
            
        except Exception as e:
            msg=Label(open_acc,text="Data was not entered...\n Some error occured...\n Click on close button to close the window...",fg="red").grid(row=12,column=1)
            button00=Button(open_acc,text="Close",command=close).grid(column=1,row=13)


    button=Button(open_acc,text="Submit",command=save).grid(column=2,row=10)
    open_acc.mainloop()