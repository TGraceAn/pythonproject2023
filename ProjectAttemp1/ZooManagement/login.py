
from tkinter import *
from tkinter import messagebox
import pymysql as pymysql
import pymysql.cursors
import os
from functools import partial

# import threading
root = Tk()
root.title('Login')
root.geometry('900x450+300+200')
root.configure(bg = "#fff")
root.resizable(False,False)

def SignIn(root):
    EFullname = user.get()
    EID = password.get()

    if (EFullname == "" or EFullname == "Employee Fullname" ) or (EID == "" or EID == "Employee ID"):
        messagebox.showerror("Entry error", "Type Employee Fullname or Employee ID")

    else:
        try:
            mydb = pymysql.connect(host='localhost',
                             user='admin',
                             port= 3306,
                             database='ZOO',
                             cursorclass=pymysql.cursors.DictCursor)
            mycursor = mydb.cursor()
            print("Connected to database.")

        except Exception as e:
            print("Failed to connect to database", e)
            messagebox.showerror("Failed to connect to database. ")
            return

        command = "use ZOO"
        mycursor.execute(command)

        command = "select * from EMPLOYEE where EmployeeFullName = %s and EmployeeID = %s"
        mycursor.execute(command,(EFullname, EID))
        myresult = mycursor.fetchall()
        print(myresult)

        if not myresult:
            messagebox.showinfo('Invalid')
        else:
            try:
                os.system("python3 main.py")
                root.destroy()
            except Exception as e:
                print(e)


img = PhotoImage(file = 'login.png')
Label(root, image = img, bg = 'white').place(x=50, y=50)

frame = Frame(root, width = 350, height = 350, bg = 'white')
frame.place(x=480, y=70)

heading = Label(frame, text = 'Sign In', fg = '#58783c', bg = 'white', font = ('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=135, y=5)

###########
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Employee Fullname')


user = Entry(frame, width = 25, fg='black', border = 0, bg = 'white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0,'Employee Fullname')

user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width = 295, height = 2, bg = 'black').place(x=25, y=107)


################
def on_enter(e):
    password.delete(0, 'end')
def on_leave(e):
    name=password.get()
    if name=='':
        password.insert(0, 'Employee ID')


password = Entry(frame, width = 25, fg='black', border = 0, bg = 'white', font=('Microsoft Yahei UI Light', 11), show ="*")
password.place(x=30, y=150)
password.insert(0,'Employee ID')

password.bind('<FocusIn>', on_enter)
password.bind('<FocusOut>', on_leave)

Frame(frame, width = 295, height = 2, bg = 'black').place(x=25, y=177)


#################
Button(frame, width = 25, pady = 7, text = 'Sign in', bg = '#B4E18D', fg = 'black', border = 0, command= partial(SignIn,root)).place(x=45, y=207)

root.mainloop()







