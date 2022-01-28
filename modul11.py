# Grafische Interface
# Tkinter
# Ursprünglich in C
# Crossplatform
# Binding für TCL

import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3 as sql

root = Tk()
nameInput = Entry(root)
nameInput.place(x=67, y=88)
# This is the section of code which creates a text input box
valueOne=Entry(root)
valueOne.place(x=67, y=218)


# This is the section of code which creates a text input box
valueTwo=Entry(root)
valueTwo.place(x=217, y=218)


# this is a function to get the user input from the text input box
def getInputBoxValue():
    userInput = nameInput.get()
    return userInput


# this is the function called when the button is clicked


def rename():
    print('clicked')
    text = getInputBoxValue()
    nameInput.delete(0, len(text))
    root.title(text)

def clear():
    print("Clear wurde geklickt")
    valueOne.delete(0, len(valueOne.get()))
    valueTwo.delete(0, len(valueTwo.get()))


def save():
    with sql.connect("database.db") as conn:
        c = conn.cursor()
        try:
            x = int(valueOne.get())
            y = int(valueTwo.get())
            c.execute("Insert into test values (?,?)", (x, y))
            print(f"{x} und {y} wurden erfolgreich gespeichert.")
            clear()
        except ValueError as e:
            print(e)
            warning = Label(root, text=str(e), bg='#F0F8FF', font=('arial', 12, 'normal'))
            warning.place(x=67, y=308)
            clear()


def query():
    with sql.connect("database.db") as conn:
        c = conn.cursor()
        c.execute("Select * from Test")
        row = c.fetchone()
        result = Label(root, text=str(row), bg='#F0F8FF', font=('arial', 12, 'normal'))
        result.place(x=67, y=368)


# This is the section of code which creates the main window
root.geometry('880x580')
root.configure(background='#F0F8FF')
root.title('Hello World')

# This is the section of code which creates a text input box


# This is the section of code which creates the a label
Label(root, text='Name:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=67, y=68)

# This is the section of code which creates a button
Button(root, text='Umbennenen', bg='#F0F8FF', font=('arial', 12, 'normal'), command=rename).place(x=67, y=118)
Button(root, text='Exit', bg='#F0F8FF', font=('arial', 12, 'normal'), command=exit).place(x=817, y=338)




# This is the section of code which creates the a label
Label(root, text='X:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=67, y=198)


# This is the section of code which creates the a label
Label(root, text='Y:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=217, y=198)


# This is the section of code which creates a button
Button(root, text='Speichern', bg='#F0F8FF', font=('arial', 12, 'normal'), command=save).place(x=67, y=258)
Button(root, text='Zeile ausgeben', bg='#F0F8FF', font=('arial', 12, 'normal'), command=query).place(x=67, y=328)





# This is the section of code which creates a button
Button(root, text='clear', bg='#F0F8FF', font=('arial', 12, 'normal'), command=clear).place(x=217, y=258)
root.mainloop()

