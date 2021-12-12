import tkinter
from tkinter import *
from tkinter import ttk


class LoginPage:
    window = Tk()
    window.title("Login")
    window.geometry("300x200")

    frame = ttk.Frame(window, padding=10)

    Label(text="Вітаємо у KalorCalc!").pack()
    LabelName = tkinter.Label(window, text="Username:")
    LabelName.pack()

    getusername = tkinter.StringVar()
    getpassword = tkinter.StringVar()

    TxtBoxName = tkinter.Entry(window, textvariable=getusername)
    TxtBoxName.pack()


    Label(window, text="Password:").pack()
    Entry(window, textvariable=getpassword).pack()


    Button(window, text="Enter").pack()

    window.mainloop()



if __name__ == "__main__":
    LoginPage
