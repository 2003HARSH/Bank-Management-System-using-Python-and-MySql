from tkinter import *

def admin_options(main_window,con):
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