from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import re
from HomePage import HomeScreenFrameGen

class Reg_screen:
     def __init__(self, master):
         self.reg_screen = Frame(master)
         self.reg_screen.configure(background="#1BD7BB")
         self.reg_screen.place(x=475, y=150, width=600, height=500)

         self.v_name = StringVar()
         self.v_mobile = StringVar()
         self.v_mailId = StringVar()
         self.v_gender = IntVar()
         self.v_country = StringVar()
         self.v_DOB = StringVar()
         self.v_username = StringVar()
         self.v_pwd = StringVar()
         self.v_confirmpwd = StringVar()

         def valid_phonenum(user_num):
             if user_num.isdigit():
                 return True
             else:
                 messagebox.showinfo('Information', 'Only digits are allowed for Mobile Number')
                 return False

         def isvalidemail(user_mail):
             if len(user_mail) > 7:
                 regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
                 if re.match(regex, user_mail) != None:
                     return True
                 else:
                     messagebox.showinfo('Error', 'This is not a Valid Email Address')
                     return False
             else:
                 messagebox.showinfo('Error', 'This is not a Valid Email Address')
                 return False

         def validateAllfields():
             if self.v_username.get() == "":
                 messagebox.showinfo('Information', 'Enter UserName to proceed')
             elif self.v_pwd.get() == "":
                 messagebox.showinfo('Information', 'Enter pwd to proceed')
             elif self.v_name.get() == "":
                 messagebox.showinfo('Information', 'Enter Name to proceed')
             elif self.v_mobile.get() == "":
                 messagebox.showinfo('Information', 'Enter Mobile Number to proceed')
             elif self.v_mailId.get() == "":
                 messagebox.showinfo('Information', 'Enter Mail ID to proceed')
             elif self.v_gender.get() == 0:
                 messagebox.showinfo('Information', 'Select Gender to proceed')
             elif self.v_country.get() == "" or self.v_country.get() == "Select your Country":
                 messagebox.showinfo('Information', 'Select Country to proceed')
             elif self.v_pwd.get() != self.v_confirmpwd.get():
                 messagebox.showinfo('Error', 'Password Mismatch')
             elif self.v_mailId.get() != "":
                 status = isvalidemail(self.v_mailId.get())
                 if (status):
                     messagebox.showinfo('', 'Registration Successful')
                     self.reg_screen.forget()
                     HomeScreenFrameGen(master)
                 else:
                     messagebox.showinfo('', 'Registration Unsuccessful')

         def clearallfields():
             self.v_username.set("")
             self.v_pwd.set("")
             self.v_confirmpwd.set("")
             self.v_name.set("")
             self.v_mobile.set("")
             self.v_mailId.set("")

         self.lbl_heading = Label(self.reg_screen, text="Registration Screen", font=("Verdana", 16, "bold"), bg="#1BD7BB").place(
             x=180, y=40)
         self.lbl_usrid = Label(self.reg_screen, text="User ID", font=("Goudy old style", 10, "bold"), bg="#1BD7BB").place(x=75,
                                                                                                                 y=90)
         self.ent_usrid = Label(self.reg_screen, text="***", font=("times new roman", 10, "bold")).place(x=200, y=90)

         self.lbl_usrname = Label(self.reg_screen, text="UserName", font=("Goudy old style", 10, "bold"), bg="#1BD7BB").place(
             x=75, y=120)
         self.ent_usrname = Entry(self.reg_screen, textvariable=self.v_username, font=("times new roman", 10, "bold")).place(x=200,
                                                                                                              y=120)

         self.lbl_pwd = Label(self.reg_screen, text="Password", font=("Goudy old style", 10, "bold"), bg="#1BD7BB").place(x=75,
                                                                                                                y=150)
         self.ent_pwd = Entry(self.reg_screen, textvariable=self.v_pwd, show="*", font=("times new roman", 10, "bold")).place(x=200,
                                                                                                               y=150)

         self.bl_confrmpwd = Label(self.reg_screen, text="Confirm Password", font=("Goudy old style", 10, "bold"),
                               bg="#1BD7BB").place(x=50, y=180)
         self.ent_confrmpwd = Entry(self.reg_screen, textvariable=self.v_confirmpwd, show="*",
                               font=("times new roman", 10, "bold")).place(x=200, y=180)

         self.lbl_Name = Label(self.reg_screen, text="Name", font=("Goudy old style", 10, "bold"), bg="#1BD7BB").place(x=75,
                                                                                                             y=210)
         self.ent_name = Entry(self.reg_screen, textvariable=self.v_name, font=("times new roman", 10, "bold")).place(x=200, y=210)

         self.lbl_mobile = Label(self.reg_screen, text="Mobile Number", font=("Goudy old style", 10, "bold"), bg="#1BD7BB").place(
             x=60, y=240)
         self.ent_mobile = Entry(self.reg_screen, textvariable=self.v_mobile, font=("times new roman", 10, "bold"))
         self.ent_mobile.place(x=200, y=240)
         # mobile num verification
         self.valid_phone = self.reg_screen.register(valid_phonenum)
         self.ent_mobile.config(validate="key", validatecommand=(self.valid_phone, '%P'))

         self.lbl_mail = Label(self.reg_screen, text="Mail ID", font=("Goudy old style", 10, "bold"), bg="#1BD7BB").place(x=75,
                                                                                                                y=270)
         self.ent_mail = Entry(self.reg_screen, textvariable=self.v_mailId, font=("times new roman", 10, "bold"))
         self.ent_mail.place(x=200, y=270)

         self.lbl_gender = Label(self.reg_screen, text="Gender", font=("Goudy old style", 10, "bold"), bg="#1BD7BB").place(x=75,
                                                                                                                 y=300)
         Radiobutton(self.reg_screen, text="Male", bg="#1BD7BB", font=("times new roman", 10, "bold"), padx=5,
                     variable=self.v_gender, value=1).place(x=200, y=300)
         Radiobutton(self.reg_screen, text="Female", bg="#1BD7BB", font=("times new roman", 10, "bold"), padx=5,
                     variable=self.v_gender, value=2).place(x=260, y=300)

         self.lbl_country = Label(self.reg_screen, text="Country", font=("Goudy old style", 10, "bold"), bg="#1BD7BB").place(x=75,
                                                                                                                   y=330)
         self.list_country = {'India', 'Germany', 'Spain', 'Nepal', 'Canada'}
         # if we remove * list will be displayed horizantally
         self.droplist = OptionMenu(self.reg_screen, self.v_country, *self.list_country)
         self.droplist.config(height=1, width=16)
         self.v_country.set('Select your Country')
         self.droplist.place(x=200, y=330)

         self.lbl_DOB = Label(self.reg_screen, text="Date of Birth", font=("Goudy old style", 10, "bold"), bg="#1BD7BB").place(
             x=65, y=370)
         self.cal = DateEntry(self.reg_screen, textvaribale=self.v_DOB, width=12, year=2021, month=4, day=10,
                         background='darkblue', foreground='white', borderwidth=2)
         self.cal.place(x=200, y=370)

         self.btn_register = Button(self.reg_screen, text="REGISTER", bg="#990F02", fg="white", font=("Helvetica", 12, "bold"),
                               command=validateAllfields)
         self.btn_register.place(x=300, y=420)

         self.btn_clear = Button(self.reg_screen, text="CLEAR", bg="#990F02", fg="white", font=("Helvetica", 10, "bold"),
                            command=clearallfields)
         self.btn_clear.place(x=60, y=420)

