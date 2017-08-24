"""
Tkinter Treeview
================

This example demonstrates using Tkinter Treeview as table to display
a database of employees.
"""

from tkinter import *
from tkinter import ttk
import sqlite3


class Employee:
    db_name = 'company.db'

    def __init__(self, wind):
        self.wind = wind
        self.wind.title('IT Employees')

        frame = LabelFrame(self.wind, text='Add new record')
        frame.grid(row=0, column=1)

        Label(frame, text='First Name: ').grid(row=1, column=1)
        self.fname = Entry(frame)
        self.fname.grid(row=1, column=2)

        Label(frame, text='Last Name: ').grid(row=2, column=1)
        self.lname = Entry(frame)
        self.lname.grid(row=2, column=2)

        Label(frame, text='Gender: ').grid(row=3, column=1)
        self.sex = Entry(frame)
        self.sex.grid(row=3, column=2)

        Label(frame, text='Start Date: ').grid(row=4, column=1)
        self.sdate = Entry(frame)
        self.sdate.grid(row=4, column=2)

        Label(frame, text='Date of Birth: ').grid(row=5, column=1)
        self.dob = Entry(frame)
        self.dob.grid(row=5, column=2)

        ttk.Button(frame, text='Add record', command=self.adding).grid(row=6, column=2)
        self.message = Label(text='', fg='red')
        self.message.grid(row=7, column=0)

        self.tree = ttk.Treeview(height=10, columns=("lname", "sex", "sdate", "dob"))
        self.tree.grid(row=100, column=0, columnspan=100)
        self.tree.heading('#0', text='First Name', anchor=W)
        self.tree.heading("#1", text='Last Name', anchor=W)
        self.tree.heading("#2", text='Gender', anchor=W)
        self.tree.heading("sdate", text='Start Date', anchor=W)
        self.tree.heading("#4", text='Birth Date', anchor=W)

        ttk.Button(text='Delete record', command=self.deleting).grid(row=10, column=5)
        ttk.Button(text='Edit record').grid(row=10, column=1)

        self.viewing_records()

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            query_result = cursor.execute(query, parameters)
            conn.commit()
        return query_result

    def viewing_records(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query = 'SELECT * FROM employee'
        db_rows = self.run_query(query)
        for row in db_rows:
           self.tree.insert('', 2, text=row[1], values=(row[2], row[3], row[4], row[5]))

    def validation(self):
        return len(self.fname.get()) != 0 and len(self.lname.get()) != 0

    def adding(self):
        if self.validation():
            query = 'INSERT INTO employee VALUES (NULL, ?, ?, ?, ?, ?)'
            parameters = (self.fname.get(), self.lname.get(), self.sex.get(), self.sdate.get(), self.dob.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Record {} added'.format(self.fname.get())
            self.fname.delete(0, END)
            self.lname.delete(0, END)
            self.sex.delete(0, END)
            self.sdate.delete(0, END)
            self.dob.delete(0, END)
            self.viewing_records()
        else:
            self.message['text'] = 'First Name and Last Name is empty'

    def deleting(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Please select record'
            return
        self. message['text'] = ''
        fname = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM employee WHERE fname = ?'
        self.run_query(query, (fname,))
        self.message['text'] = 'Record {} deleted'.format(fname)
        self.viewing_records()


if __name__ == "__main__":
    root = Tk()
    application = Employee(root)
    root.mainloop()
