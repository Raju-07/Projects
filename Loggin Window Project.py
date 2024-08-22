# Modules to be import
import webbrowser 
import time
from tkinter import *
from customtkinter import *
from PIL import Image,ImageTk
import os
from tkinter import messagebox as ms
#window Appearance   
set_appearance_mode("dark")
set_default_color_theme("blue")

#Initializing Window
app=CTk()
app.geometry("856x650")
app.title("Logging Window")
app.resizable(False,False)

#User Data
list_of_Email=["rajuyadav782760@gmail.com"]
list_of_password=["Rajuyadav@2005"]

# For getting image in program
file_path=os.path.dirname(os.path.realpath(__file__))
bg_image=CTkImage(Image.open(file_path + "/Background_image2.jpg"),size=(856,650))   #Dawnload all the icon using in this project from Icon8 website
Email_icon=CTkImage(Image.open(file_path +"/Email_icon.png"),size=(30,30))
password_icon=CTkImage(Image.open(file_path + "/password_icon.png"),size=(33,33))
google_icon=CTkImage(Image.open(file_path + "/Google_icon.png"),size=(33,33))
show_pass=CTkImage(Image.open(file_path + "/show_pass_icon.png"),size=(20,20))
hide_pass=CTkImage(Image.open(file_path + "/hide_pass_icon.png"),size=(20,20))

#Function for Operation
def login():
    Email_id=Email_Entry.get()
    Password=pass_Entry.get()
    if Email_id in list_of_Email and Password in list_of_password:
        ms.showinfo("Success","You're Logged In")

def con_google():
    querry="https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?client_id=445112211283-sk04feuogpcjd3dq8eshrdnr4bpm1sfk.apps.googleusercontent.com&response_type=code&access_type=offline&scope=openid%20email%20profile%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcalendar%20https%3A%2F%2Fwww.google.com%2Fm8%2Ffeeds%2F%20https%3A%2F%2Fmail.google.com%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuser.birthday.read&prompt=consent&include_granted_scopes=true&redirect_uri=https%3A%2F%2Foutlook.office.com%2Fmail%2FoauthRedirect.html%3Fapp%3Dnative&login_hint=rajuyadav782760%40gmail.com&enable_granular_consent=true&state=Y29ycmVsYXRpb25faWQ9YTdmOWUwOTYtZDY5YS00ZjU5LTZlNzctYTFkNTZiMDc4YjI5JmxvZ2luX2hpbnQ9cmFqdXlhZGF2NzgyNzYwQGdtYWlsLmNvbSZ0eXBlX2hpbnQ9R29vZ2xlJmluc3RhbmNlX2lkPTE%3D&service=lso&o2v=2&ddm=0&flowName=GeneralOAuthFlow"
    webbrowser.open(querry)

def hide_password():
    if pass_Entry.cget("show")=="":    
        hide_pass_button.configure(image=show_pass)
        pass_Entry.configure(show="*")
    else:
        hide_pass_button.configure(image=hide_pass)
        pass_Entry.configure(show="")
#Creating New account
def createnewaccount():
    new_acc_label.configure(text_color="blue")
    time.sleep(0.5)
    ms.showerror("Development","This function is in development")  

# Dynamic effect for create new account Label
def on_enter(event):
    new_acc_label.configure(text_color="Purple")
def on_leave(event):
    new_acc_label.configure(text_color="black")
    

#Inserting image for application Background    
label=CTkLabel(master=app,
               text="",
               image=bg_image)
label.place(relwidth=1,relheight=1)
# Frame for Loggin Widgets
login_frame=CTkFrame(master=app,
                     width=400,
                     height=650,
                     fg_color="white",
                     corner_radius=15,
                     border_width=1,
                     border_color="white")
login_frame.place(relx=0.55,rely=0.0)

#Creating Label on the frame
label_headig=CTkLabel(master=login_frame,
                     text="Welcome Back!",
                     text_color="Purple",
                     font=("Roboto Bold",25,"bold"))
label_headig.place(relx=0.1,rely=0.1)

label_subheading=CTkLabel(master=login_frame,
                          text="Sign in to your account",
                          text_color="black",
                          font=("Roboto Bold",15))
label_subheading.place(relx=0.1,rely=0.15)

#Label for Email
Email_label=CTkLabel(master=login_frame,
                     text="Email:",
                     text_color="Purple",
                     font=("Roboto Bold",19,"bold"),
                     image=Email_icon,
                     compound="left")
Email_label.place(relx=0.1,rely=0.3)

#Entry box for Email
Email_Entry=CTkEntry(master=login_frame,
                     width=300,
                     height=40,
                     corner_radius=9,
                     border_color="Purple",
                     border_width=2,
                     font=("Roboto Bold",17),
                     text_color="Purple",
                     fg_color="#E8F0F1",
                     placeholder_text_color="Purple")
Email_Entry.place(relx=0.1,rely=0.36)
#Creating Label for Password
pass_label=CTkLabel(master=login_frame,
                    text="Password:",
                    text_color="Purple",
                    font=("Roboto Bold",19,"bold"),
                    image=password_icon,
                    compound="left")
pass_label.place(relx=0.1,rely=0.48)

#Entry box for password
pass_Entry=CTkEntry(master=login_frame,
                     width=300,
                     height=40,
                     corner_radius=9,
                     border_color="Purple",
                     border_width=2,
                     font=("Roboto Bold",17),
                     text_color="Purple",
                     fg_color="#E8F0F1",
                     placeholder_text_color="Purple",
                     show="")      #✴
pass_Entry.place(relx=0.1,rely=0.54)

# Creating Loging Button
login_button=CTkButton(master=login_frame,
                       text="Login",
                       text_color="white",
                       fg_color="#703DF1",
                       width=300,
                       height=40,
                       font=("Roboto Bold",17,"bold"),
                       hover_color="#8C2FD8",
                       command=login)
login_button.place(relx=0.1,rely=0.65)

# creating button for Login with Google
google_log_button=CTkButton(master=login_frame,
                            text="Continue with Google",
                            text_color="Purple",
                            fg_color="#F2E7F4",
                            corner_radius=8,
                            width=300,
                            height=40,
                            font=("Roboto",17,"bold"),
                            hover_color="grey",
                            image=google_icon,
                            compound="left",
                            command=con_google)
google_log_button.place(relx=0.1,rely=0.74)

hide_pass_button=CTkButton(master=login_frame,
                           text="",
                           hover_color="white",
                           height=20,
                           width=10,
                           bg_color="transparent",
                           fg_color="transparent",
                           corner_radius=15,
                           command=hide_password,
                           image=hide_pass,
                           compound="left")
hide_pass_button.place(relx=0.85,rely=0.55)
#Label for creating New Account
new_acc_label=CTkLabel(master=login_frame,
                       text="Create new account",
                       text_color="black",
                       font=("Arial",15,"underline"))
new_acc_label.place(relx=0.1,rely=0.89)
new_acc_label.bind("<Button-1>",lambda event: createnewaccount())
new_acc_label.bind("<Enter>",on_enter)
new_acc_label.bind("<Leave>",on_leave)
#Mainloop for Running GUI
app.mainloop()

