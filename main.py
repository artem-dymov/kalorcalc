import tkinter as tk
from tkinter import *
from tkinter import ttk




class LoginPage:
    def __init__(self, window):
        window.title("Login")
        window.geometry("300x200")

        print("1")


        frame = ttk.Frame(window, padding=10)

        tk.Label(text="Вітаємо у KalorCalc!").pack()
        tk.Label(window, text="Username:").pack()

        self.entry = tk.Entry(window)
        self.entry.pack()


        tk.Label(window, text="Password:").pack()
        Entry(window).pack()


        self.btn = tk.Button(window, text="Enter", command=lambda: self.btn_click(window, self.entry))
        self.btn.pack()

        tk.Label(window, text="Якщо логіна не буде у базі,\nми автоматично зареєструємо вас.").pack()

    def btn_click(self, window, e):
        return print(e.get())
    print("2")



def main():
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
