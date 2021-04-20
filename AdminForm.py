from tkinter import *
from tkinter import font
from tkinter import messagebox

from ScreenTemplate import template


class AdminForm(template):
    def __init__(self, master):
        super().__init__(master)
        self.form_frame = Frame(self.baseFrame)
        self.insertion_form = Frame(self.baseFrame)

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
        table_name = self.table_entry.get()

        if username == 'admin' and pwd == 'admin123':
            self.display_form(table_name)
        else:
            messagebox.showerror('Admin Login Error', 'These are not valid admin credentials')

    def refresh_ui(self):
        # place the frame and adjust grids
        for child in self.form_frame.winfo_children():
            child.grid_configure(padx=5, pady=10)
        self.form_frame.place(x=500, y=100)

    def display_form(self, table_name):
        self.open_a_connection()
        self.acursor.execute(f"select column_name from user_tab_cols where table_name='{table_name.upper()}'")
        self.attribute_list = [col[0] for col in self.acursor.fetchall()]
        self.entry_list = []
        for index, name in enumerate(self.attribute_list):
            Label(self.insertion_form, text=name, font=self.form_font).grid(row=index, column=0)
            self.entry_list.append(Entry(self.insertion_form, font=self.form_font))
            self.entry_list[index].grid(row=index, column=1)
        self.insertion_form.place(x=500, y=400)

        self.insert_button = Button(self.insertion_form, text='Insert data', font=self.form_font,
                                    command=lambda: self.insertion_function(table_name))
        self.insert_button.grid(row=len(self.entry_list), columnspan=2)
        print(self.attribute_list)
        self.close_a_connection()

    def insertion_function(self, table_name):
        insertion_data = f"insert into {table_name.upper()} values("
        for entry in self.entry_list:
            insertion_data += (entry.get() + ",")
            # clear entries
            entry.delete(0, END)
        insertion_data = insertion_data[:-1]
        insertion_data += ")"
        print(insertion_data)
        self.open_a_connection()
        self.acursor.execute(f"{insertion_data}")
        self.close_a_connection()

        # clear entries
        self.table_entry.delete(0, 'end')
        self.pwd_entry.delete(0, 'end')
        self.username_entry.delete(0, 'end')

        messagebox.showinfo('Insertion successful',
                            'Your data has been successfully entered. Please restart your app to see changes.')
