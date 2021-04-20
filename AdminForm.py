from tkinter import *
from tkinter import font
from tkinter import messagebox

from ScreenTemplate import template


class AdminForm(template):
    def __init__(self, master):
        super().__init__(master)
        self.form_frame = Frame(self.baseFrame)

        # font for this screen
        self.form_font = font.Font(family='Microsoft YaHei UI', size=13, weight="bold")

        # form structure
        Label(self.form_frame, text='Enter admin credentials to get database privileges!', font=self.form_font).grid(
            row=0, column=0, columnspan=2)

        Label(self.form_frame, text='User ID:', font=self.form_font).grid(row=1, column=0)
        self.username_entry = Entry(self.form_frame, font=self.form_font)
        self.username_entry.grid(row=1, column=1)

        Label(self.form_frame, text='Password:', font=self.form_font).grid(row=2, column=0)
        self.pwd_entry = Entry(self.form_frame, font=self.form_font, show='*')
        self.pwd_entry.grid(row=2, column=1)

        Label(self.form_frame, text='Table Name:', font=self.form_font).grid(row=3, column=0)
        self.table_entry = Entry(self.form_frame, font=self.form_font)
        self.table_entry.grid(row=3, column=1)

        self.verify_button = Button(self.form_frame, text='Verify Credentials', font=self.form_font)
        self.verify_button.grid(row=4, columnspan=2)

        self.refresh_ui()

    def admin_verify(self):
        username = self.username_entry.get()
        pwd = self.pwd_entry.get()
        table = self.table_entry.get()
        self.table_entry.delete(0, 'end')
        self.pwd_entry.delete(0, 'end')
        self.username_entry.delete(0, 'end')

        if username == 'admin' and pwd == 'admin123':
            self.display_form(table)
        else:
            messagebox.showerror('Admin Login Error', 'These are not valid admin credentials')

    def refresh_ui(self):
        # place the frame and adjust grids
        for child in self.form_frame.winfo_children():
            child.grid_configure(padx=5, pady=10)
        self.form_frame.place(x=500, y=100)

    def display_form(self, table_name):
        # display the form to edit that specific table
        pass
