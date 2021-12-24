import tkinter as tk
from tkinter import *
from tkinter import ttk
from pylib import pycsv, calculate


class LoginPage:
    def __init__(self, window):
        window.title("Login")
        window.geometry("300x200")

        frame = ttk.Frame(window, padding=10)

        tk.Label(text="Вітаємо у KalorCalc!").pack()
        tk.Label(window, text="Username:").pack()

        self.username_entry = tk.Entry(window)
        self.username_entry.pack()

        tk.Label(window, text="Password:").pack()

        self.password_entry = tk.Entry(window)
        self.password_entry.pack()

        self.btn = tk.Button(window, text="Enter",
                             command=lambda: self.btn_click(window, self.username_entry, self.password_entry))
        self.btn.pack()

        tk.Label(window, text="Якщо логіна не буде у базі,\nми автоматично зареєструємо вас.").pack()

    def auth(self, username_entry):
        if username_entry.get() in pycsv.csv_auth_get('usernames'):
            print("Ви зареєстровані!")
        else:
            print('Ви не зареєстровані!')

    def btn_click(self, window, user, password):
        self.auth(self.username_entry)
        return print(user.get(), password.get(), pycsv.csv_auth_get('usernames'))


def main():
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()


if __name__ == "__main__":
    main()
