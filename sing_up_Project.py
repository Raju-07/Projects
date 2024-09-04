from customtkinter import *
from PIL import Image
import os
from tkinter import messagebox as mb
#Image Area
file_path=os.path.dirname(os.path.realpath(__file__))
bg_image=CTkImage(Image.open(file_path + "/sing_up_image.png"),size=(600,650))
Name_icon=CTkImage(Image.open(file_path + "/Name_icon2.png"),size=(30,30))
email_icon=CTkImage(Image.open(file_path + "/Email_icon.png"),size=(30,30))
password_icon=CTkImage(Image.open(file_path + "/password_icon.png"),size=(30,30))


#Window Appearance
set_appearance_mode("light")
window=CTk()
window.geometry('856x750')
window.title("Sign Up")
window.resizable(False,False)
window.configure(fg_color="white")

#function in this program
def create_account():
    try:
        name=name_Eb.get()
        email=Email_Eb.get()
        password = Password_Eb.get()
        con_password = con_password_Eb.get()
        if (name.isspace() or len(name)==0) or (len(email) == 0 or email.isspace()):
            mb.showerror("Error","Please fill the form Completely...")
        elif password.isspace() or len(password) == 0:
            mb.showerror("Error  o(><；)oo ","Please Enter Passowrd..")
        elif(password != con_password):
            mb.showerror("Error","Your password isn't same\nPlease Conform your password")
        else:
            mb.showerror("All done!","Account created...")

    except:
        raise Exception("Fuctions isn't working correctly...")


bg_image_label=CTkLabel(master=window,
                        text="",
                        image=bg_image)
bg_image_label.place(relheight=1,relwidth=0.6)
wel_label=CTkLabel(master=window,
                       text="Welcome!",
                       text_color="Purple",
                       font=("Roboto Bold",40,"bold"),
                       corner_radius=8,
                       bg_color="transparent")
wel_label.place(relx=0.68,rely=0.05)
#Name Label
name_label=CTkLabel(master=window,
                        text="Name",
                        text_color="Purple",
                        font=("Roboto Bold",19,"bold"),
                        image=Name_icon,
                        compound="left")
name_label.place(relx=0.68,rely=0.2)
# Name Entry Box
name_Eb=CTkEntry(master=window,
                width=250,
                height=40,
                corner_radius=9,
                border_color="Purple",
                border_width=2,
                font=("Roboto Bold",19,"bold"),
                text_color="Purple",
                fg_color="#E8F0F1")
name_Eb.place(relx=0.68,rely=0.25)

#Label For Email
email_label=CTkLabel(master=window,
                     text="Email",
                     text_color="Purple",
                     font=("Roboto Bold",19,"bold"),
                     image=email_icon,
                     compound="left")
email_label.place(relx=0.68,rely=0.35)
#Entrybox for Email
Email_Eb=CTkEntry(master=window,
                  width=250,
                  height=40,
                  corner_radius=9,
                  border_color="Purple",
                  border_width=2,
                  font=("Roboto Bold",18,"bold"),
                  text_color="Purple",
                  fg_color="#E8F0F1",
                  placeholder_text_color="Purple")
Email_Eb.place(relx=0.68,rely=0.40)

#Label for Password
password_label=CTkLabel(master=window,
                        text="Password",
                        text_color=("Purple"),
                        font=("Roboto Bold",19,"bold"),
                        image=password_icon,
                        compound="left")
password_label.place(relx=0.68,rely=0.50)
#Entry box for Password
Password_Eb=CTkEntry(master=window,
                     width=250,
                     height=40,
                     corner_radius=9,
                     font=("Roboto Bold",19,"bold"),
                     border_color="Purple",
                     border_width=2,
                     text_color="Purple",
                     fg_color="#E8F0F1",
                     placeholder_text_color="Purple")
Password_Eb.place(relx=0.68,rely=0.55)

#Label for Confirm Password
con_password_label=CTkLabel(master=window,
                        text="Confirm Password",
                        text_color=("Purple"),
                        font=("Roboto Bold",19,"bold"),
                        image=password_icon,
                        compound="left")
con_password_label.place(relx=0.68,rely=0.65)
#Entry box for Confirm Password
con_password_Eb=CTkEntry(master=window,
                     width=250,
                     height=40,
                     corner_radius=9,
                     font=("Roboto Bold",19,"bold"),
                     border_color="Purple",
                     border_width=2,
                     text_color="Purple",
                     fg_color="#E8F0F1",
                     placeholder_text_color="Purple")
con_password_Eb.place(relx=0.68,rely=0.70)
# Button for Creating Account
create_button=CTkButton(master=window,
                        width=70,
                        height=45,
                        corner_radius=9,
                        text="Create Account",
                        text_color="White",
                        font=("Roboto Bold",20,"bold"),
                        fg_color="Purple",
                        command=create_account)
create_button.place(relx=0.73,rely=0.8)

window.mainloop()