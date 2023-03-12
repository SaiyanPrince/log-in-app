from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#functions

def user_enter(event):
    #event variable is only there to store the random assigned value to avoid error
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    #event variable is only there to store the random assigned value to avoid error
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0, END)

def hide():
    open_eye.config(file='close_eye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    open_eye.config(file='open_eye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def signup_page():
    login_window.destroy()
    import signup

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All fields are required!')
    
    else:
        try:
            conn=pymysql.connect(host='Localhost',
                                user='username',
                                password='password')
            mycursor=conn.cursor()
        except:
             messagebox.showerror('Error', 'Connection Not Established. Please Try Again!')
             return
        
        query='use users'
        mycursor.execute(query)

        query='select * from data where username=%s and password=%s'
        mycursor.execute(query, 
                         (usernameEntry.get(), passwordEntry.get())
                         )
        
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Success', 'Login Successfull')

def forget_password():
    def change_password():
        if user_entry.get()=='' or new_password_entry.get()=='' or confirm_pass_entry.get()=='':
            messagebox.showerror('Error', 'All fields are required!', parent=window) 
        elif new_password_entry.get() != confirm_pass_entry.get():
            messagebox.showerror('Error', 'Password does not match with Confirm Password!', parent=window)
        else:
            conn=pymysql.connect(host='Localhost',
                                user='username',
                                password='password',
                                database='users')
            mycursor=conn.cursor()
            query='select * from data where username=%s'
            mycursor.execute(query, (user_entry.get()))

            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error', 'Incorrect username', parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query, (new_password_entry.get(), user_entry.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo('Success', 'Password is reset, please login with new password!', parent=window)
                window.destroy()


    window = Toplevel()
    window.title('Change Password')
    window.resizable(0,0)

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bgLabel=Label(window, image=bgPic)
    bgLabel.grid()

    heading_label=Label(window, text='RESET PASSWORD', 
                        font=('arial', 18, 'bold'),
                        bg='white', fg='magenta2')
    heading_label.place(x=485, y=60)

    userLabel = Label(window, text='Username',
                      font=('arial', 12, 'bold'),
                        bg='white', fg='orchid2')
    userLabel.place(x=470, y=130)

    user_entry=Entry(window, width=25,
                     fg='magenta2', font=('arial', 11, 'bold'),
                     bd=0)
    user_entry.place(x=470, y=160)

    Frame(window, width=250, height=2, bg='orchid2').place(x=470, y=180)

    new_passwordLabel = Label(window, text='New Password',
                      font=('arial', 12, 'bold'),
                        bg='white', fg='orchid2')
    new_passwordLabel.place(x=470, y=210)

    new_password_entry=Entry(window, width=25,
                     fg='magenta2', font=('arial', 11, 'bold'),
                     bd=0)
    new_password_entry.place(x=470, y=240)

    Frame(window, width=250, height=2, bg='orchid2').place(x=470, y=260)

    confirm_passLabel = Label(window, text='Confirm Password',
                      font=('arial', 12, 'bold'),
                        bg='white', fg='orchid2')
    confirm_passLabel.place(x=470, y=290)

    confirm_pass_entry=Entry(window, width=25,
                     fg='magenta2', font=('arial', 11, 'bold'),
                     bd=0)
    confirm_pass_entry.place(x=470, y=320)

    Frame(window, width=250, height=2, bg='orchid2').place(x=470, y=340)

    submitButton = Button(window, text='Submit',
                      font=('arial', 16, 'bold'),
                        bg='magenta2', fg='white',
                        bd=0, activebackground='magenta2', activeforeground='white',
                        width=19, cursor='hand2',
                        command=change_password)
    submitButton.place(x=475, y=390)

    window.mainloop()


#GUI

login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')

bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(login_window, image=bgImage) 
bgLabel.place(x=0, y=0)

heading=Label(login_window, text='USER LOGIN', 
              font=('Microsoft Yahei UI Light', 23, 'bold'),
              bg='white', fg='firebrick1')
heading.place(x=605,y=120)

usernameEntry=Entry(login_window, width=25,
                    font=('Microsoft Yahei UI Light', 11, 'bold'), 
                    bd=0, fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)

username_frame=Frame(login_window, width=250, height=2,bg='firebrick1')
username_frame.place(x=580,y=222)

passwordEntry=Entry(login_window, width=25,
                    font=('Microsoft Yahei UI Light', 11, 'bold'), 
                    bd=0, fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)

password_frame=Frame(login_window, width=250, height=2,bg='firebrick1')
password_frame.place(x=580,y=282)

open_eye=PhotoImage(file='open_eye.png')
eyeButton=Button(login_window, image=open_eye, bd=0, bg='white', 
                 activebackground='white',cursor='hand2',
                 command=hide)
eyeButton.place(x=800,y=255)

forgetButton=Button(login_window, text='Forgot Password?', bd=0, bg='white', 
                 activebackground='white',cursor='hand2',
                 font=('Microsoft Yahei UI Light', 9, 'bold'),
                 fg='firebrick1', activeforeground='firebrick1',
                 command=forget_password)
forgetButton.place(x=715,y=295)

loginButton=Button(login_window, text='Login', font=('Open Sans', 16, 'bold'),
                   fg='white', bg='firebrick1',cursor='hand2',
                   activebackground='firebrick1', activeforeground='white',
                   bd=0, width=19, command=login_user)
loginButton.place(x=578,y=350)

orLabel=Label(login_window, text='-------------- OR --------------', font=('Open Sans', 16),
              fg='firebrick1', bg='white')
orLabel.place(x=582,y=400)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=640,y=440)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window, image=google_logo, bg='white')
googleLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window, image=twitter_logo, bg='white')
twitterLabel.place(x=740,y=440)

signupLabel=Label(login_window, text="Don't have an account?", font=('Open Sans', 9, 'bold'),
              fg='firebrick1', bg='white')
signupLabel.place(x=585,y=500)

new_accountButton=Button(login_window, text='Create New One', font=('Open Sans', 9, 'bold underline'),
                   fg='blue', bg='white',cursor='hand2',
                   activebackground='white', activeforeground='blue',
                   bd=0, command=signup_page)
new_accountButton.place(x=727,y=500)

login_window.mainloop()