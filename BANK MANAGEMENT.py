import mysql.connector as a
con = a.connect(host="localhost", user="root", passwd="3557", database="bank")
from tkinter import *

def openAcc():
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

def checkBal():
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

def closeAcc():
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

def depoAmo():
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

def withAmo():
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


def user_options():
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

def admin_options():
    admin_window=Toplevel(main_window)
    admin_window.title("ADMIN PANEL")
    label=Label(admin_window,bg="yellow",fg="red",text="ADMINISTRATOR LOGIN",justify=LEFT,font='arabic').grid(column=0,row =0)
    admin_window.geometry('600x500')
    
    Password=Label(admin_window,text="Admin Password :",justify=LEFT)
    Password.grid(column=0,row=3)       
    upasswd=StringVar()
    e5=Entry(admin_window,textvariable=upasswd,justify=LEFT,show="*").grid(row=3,column=1)
  
    def show():
        x = "select * from ACCOUNT"
        c = con.cursor()
        c.execute(x)
        count=0
        l=[("ACCOUNT_NUMBER","NAME","DOB","PHONE_NO.","ADDRESS","OPENING_BALANCE")]
        for i in c.fetchall():
            l.append(i)
        for i in range(len(l)):
            for j in range(len(l[0])):
                e=Entry(admin_window,width=18,fg='blue',font='arial')
                e.grid(row=i+15,column=j)
                e.insert(END,l[i][j])    

    def close():
        admin_window.destroy()
    def save():
        if upasswd.get()=='P@$$w0rd':
            msg=Label(admin_window,text="Welcome Administrator...\n ",fg="green").grid(row=6,column=1)
            button00=Button(admin_window,text="Show DATA",command=show).grid(column=1,row=8)
            button01=Button(admin_window,text="Close",command=close).grid(column=2,row=8)
        else:
            msg=Label(admin_window,text="Incorrect Credentials or.....\n Some error occoured\n Click on close button to close the window...",fg="red").grid(row=10,column=1)
            button00=Button(admin_window,text="Close",command=close).grid(column=1,row=13)


    button=Button(admin_window,text="Submit",command=save).grid(column=1,row=6)
    admin_window.mainloop()

def main():
    global main_window
    main_window=Tk()
    main_window.title("BANK MANAGEMENT")
    main_window.geometry('600x300')
    l1=Label(main_window,text="Welcome to Bank....... ",bg="yellow",fg="blue",font=('arabic 32 '),justify=CENTER).grid(column=0,row =0)

    option=Label(main_window,text="LOGIN AS USER",justify=RIGHT)
    option.grid(column=0,row=1)
    main_button=Button(main_window,text="User Login",justify=LEFT,command=user_options).grid(column=1,row=1)

    option1=Label(main_window,text="LOGIN AS ADMINISTRATOR",justify=RIGHT)
    option1.grid(column=0,row=2)
    main_button1=Button(main_window,text="Admin Login",justify=LEFT,command=admin_options).grid(column=1,row=2)
    main_window.mainloop()

  
main()    
