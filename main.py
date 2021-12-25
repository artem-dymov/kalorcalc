import tkinter as tk
from tkinter import *
from tkinter import ttk
from pylib import pycsv, calculate


class LoginPage:
    def __init__(self, root):
        window = Toplevel(root)
        window.title("Login")
        window.geometry("300x200")

        frame = ttk.Frame(window, padding=10)

        ttk.Label(window, text="Вітаємо у KalorCalc!").pack()
        ttk.Label(window, text="Username:").pack()

        self.username_entry = ttk.Entry(window)
        self.username_entry.pack()

        ttk.Label(window, text="Password:").pack()

        self.password_entry = ttk.Entry(window)
        self.password_entry.pack()

        self.btn = ttk.Button(window, text="Enter",
                             command=lambda: self.btn_click(window, self.username_entry, self.password_entry, root))
        self.btn.pack()

        ttk.Label(window, text="Якщо логіна не буде у базі,\nми автоматично зареєструємо вас.").pack()


    def auth(self, username_entry, window, root):
        if username_entry.get() in pycsv.csv_auth_get('usernames'):
            print("Ви зареєстровані")

        else:
            window.withdraw()
            ParametersPage(root)

    def btn_click(self, window, user, password, root):
        self.auth(self.username_entry, window, root)


class ParametersPage:
    def __init__(self, root):

        window = Toplevel(root)
        window.title("Parameters")
        window.geometry('500x500')

        frame = ttk.Frame(window, padding=10)

        ttk.Label(window, text="Маса").pack()

        entry_mass = ttk.Entry(window)
        entry_mass.pack()

        ttk.Label(window, text="Ріст").pack()

        entry_growth = ttk.Entry(window)
        entry_growth.pack()

        ttk.Label(window, text="Вік").pack()

        entry_age = ttk.Entry(window)
        entry_age.pack()

        ttk.Label(window, text="Ваша стать").pack()

        var_sex = tk.IntVar()
        var_sex.set(1)


        r_btn_male = ttk.Radiobutton(window, text="Чоловіча", variable=var_sex, value=1)
        r_btn_male.pack()

        r_btn_female = ttk.Radiobutton(window, text="Жіноча", variable=var_sex, value=2)
        r_btn_female.pack()

        ttk.Label(window, text="Рівень вашої активності").pack()

        var_activity = tk.IntVar()
        var_activity.set(1)

        r_btn_activity_low = ttk.Radiobutton(window, variable=var_activity, value=1, text="Низький")
        r_btn_activity_low.pack()

        r_btn_activity_pomirn = ttk.Radiobutton(window, variable=var_activity, value=2, text="Помірний")
        r_btn_activity_pomirn.pack()

        r_btn_activity_middle = ttk.Radiobutton(window, variable=var_activity, value=3, text="Середній")
        r_btn_activity_middle.pack()

        r_btn_activity_high = ttk.Radiobutton(window, variable=var_activity, value=4, text="Високий")
        r_btn_activity_high.pack()

        r_btn_activity_very_high = ttk.Radiobutton(window, variable=var_activity, value=5, text="Дуже високий")
        r_btn_activity_very_high.pack()

        ttk.Label(window, text="Чого ви хочете?").pack()

        var_want = tk.IntVar()
        var_want.set(1)

        r_btn_want_lose = ttk.Radiobutton(window, variable=var_want, value=1, text="Схуднути")
        r_btn_want_lose.pack()

        r_btn_want_not = ttk.Radiobutton(window, variable=var_want, value=2, text="Не хочу міняти вагу")
        r_btn_want_not.pack()

        r_btn_want_gain = ttk.Radiobutton(window, variable=var_want, value=3, text="Хочу набрати вагу")
        r_btn_want_gain.pack()


        ttk.Button(window, text="Quit", command=lambda: window.quit()).pack()
        ttk.Button(window, text="Test", command=lambda: print()).pack()



def main():
    root = tk.Tk()
    root.withdraw()
    LoginPage(root)
    root.mainloop()


if __name__ == "__main__":
    main()
