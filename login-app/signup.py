from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


#functions

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)

def login_page():
    signup_window.destroy()
    import signin

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error', 'All fields are required!')

    elif passwordEntry.get()!= confirmEntry.get():
        messagebox.showerror('Error', "The password does not match!")

    elif check.get()==0:
        messagebox.showerror('Error', 'Please accept the Terms and Conditions!')

    else:
        try:
            conn=pymysql.connect(host='Localhost',
                            user='Username',
                            password='Password')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return
        
        try:
            query='create database users'
            mycursor.execute(query)
            query='use users'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use users')

        query='select * from data where username=%s'
        mycursor.execute(query, 
                         (usernameEntry.get())
                         )
        
        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('Error', 'Username already exists!')
        else:

            query='insert into data(email, username, password) values (%s, %s, %s)'
            mycursor.execute(query, 
                            (emailEntry.get(), usernameEntry.get(), passwordEntry.get())
                            )
            conn.commit()
            conn.close
            messagebox.showinfo('Success','Registration Successful!')
            clear() 
            signup_window.destroy()
            import signin



#GUI

signup_window=Tk()
signup_window.geometry('990x660+50+50')
signup_window.resizable(0,0)
signup_window.title('Sign Up Page')

bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(signup_window, image=bgImage) 
bgLabel.grid()

frame=Frame(signup_window, bg='white')
frame.place(x=554,y=100)

heading=Label(frame, text='CREATE AN ACCOUNT', 
              font=('Microsoft Yahei UI Light', 16, 'bold'),
              bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=27, pady=10)


emailLabel=Label(frame, text='Email',
                 font=('Microsoft Yahei UI Light', 10, 'bold'),
                 bg='white', fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10,0))

emailEntry=Entry(frame, width=29, font=('Microsoft Yahei UI Light', 10, 'bold'),
                bg='pink')
emailEntry.grid(row=2, column=0, sticky='w', padx=28)


usernameLabel=Label(frame, text='Username',
                 font=('Microsoft Yahei UI Light', 10, 'bold'),
                 bg='white', fg='firebrick1')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10,0))

usernameEntry=Entry(frame, width=29, font=('Microsoft Yahei UI Light', 10, 'bold'),
                bg='pink')
usernameEntry.grid(row=4, column=0, sticky='w', padx=28)


passwordLabel=Label(frame, text='Password',
                 font=('Microsoft Yahei UI Light', 10, 'bold'),
                 bg='white', fg='firebrick1')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10,0))

passwordEntry=Entry(frame, width=29, font=('Microsoft Yahei UI Light', 10, 'bold'),
                bg='pink')
passwordEntry.grid(row=6, column=0, sticky='w', padx=28)


confirmLabel=Label(frame, text='Confirm Password',
                 font=('Microsoft Yahei UI Light', 10, 'bold'),
                 bg='white', fg='firebrick1')
confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10,0))

confirmEntry=Entry(frame, width=29, font=('Microsoft Yahei UI Light', 10, 'bold'),
                bg='pink')
confirmEntry.grid(row=8, column=0, sticky='w', padx=28)


check=IntVar()
agree=Checkbutton(frame, text="I agree to the Terms & Conditions",
                  font=('Microsoft Yahei UI Light', 9, 'bold'),
                  bg='white', padx=17, pady=15, fg='firebrick1',
                  activebackground='white', activeforeground='firebrick1',
                  cursor='hand2', variable=check)

agree.grid(row=9, column=0)


signupButton=Button(frame, text='Sign Up', font=('Open Sans', 16, 'bold'),
                   fg='white', bg='firebrick1',cursor='hand2',
                   activebackground='firebrick1', activeforeground='white',
                   bd=0, width=19, command=connect_database)
signupButton.grid(row=10, column=0, pady=10)


accountLabel=Label(frame, text="Already have an account?", font=('Open Sans', 9, 'bold'),
              fg='firebrick1', bg='white')
accountLabel.grid(row=11, column=0, sticky='w', padx=30)

loginButton=Button(frame, text='Log in', font=('Open Sans', 9, 'bold underline'),
                   fg='blue', bg='white',cursor='hand2',
                   activebackground='white', activeforeground='blue',
                   bd=0, command=login_page)
loginButton.grid(row=11, column=0, sticky='e', padx=55)

signup_window.mainloop()