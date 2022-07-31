import tkinter as tk
from tkinter import *
from tkinter import ttk
from pylib import pycsv, calculate


class LoginPage:
    def __init__(self, root):
        window = tk.Toplevel(root)
        window.title("Авторизація")
        window.geometry("300x200")

        frame = ttk.Frame(window, padding=10)

        ttk.Label(window, text="Вітаємо у KalorCalc!").pack()
        ttk.Label(window, text="Логін:").pack()

        self.username_entry = ttk.Entry(window)
        self.username_entry.pack()

        ttk.Label(window, text="Пароль:").pack()

        self.password_entry = ttk.Entry(window)
        self.password_entry.pack()

        self.btn = ttk.Button(window, text="Ввести",
                              command=lambda: self.auth(window, root, self.username_entry, self.password_entry))
        self.btn.pack()

        ttk.Label(window, text="Якщо логіна не буде у базі,\nми автоматично зареєструємо вас.").pack()

    def auth(self, window, root, username_entry, password_entry):
        if username_entry.get() == "" or password_entry.get() == "":
            ErrorEmptyPage(root)

        elif username_entry.get().lower() in pycsv.get_usernames():
            if username_entry.get().lower() == 'username':
                ErrorWrongPasswordPage(root)
            elif pycsv.check_password(username_entry.get(), password_entry.get()) == True:
                window.withdraw()
                s = pycsv.get_choosed_data(username_entry.get())
                MenuPage(root, username_entry.get(), calculate.imt_category(calculate.imt(float(s[2]), s[3])), calculate.kalor(username_entry.get()))
            else:
                ErrorWrongPasswordPage(root)


        else:
            pycsv.auth_writer(username_entry.get(), password_entry.get())
            window.withdraw()
            ParametersPage(root, username_entry.get())

class ParametersPage:
    def __init__(self, root, username):
        window = tk.Toplevel(root)
        window.title("Параметри")
        window.geometry('500x500')

        frame = ttk.Frame(window, padding=10)

        ttk.Label(window, text="Маса, кг").pack()

        entry_mass = ttk.Entry(window)
        entry_mass.pack()

        ttk.Label(window, text="Ріст, см").pack()

        entry_growth = ttk.Entry(window)
        entry_growth.pack()

        ttk.Label(window, text="Вік, роки").pack()

        entry_age = ttk.Entry(window)
        entry_age.pack()

        ttk.Label(window, text="Ваша стать").pack()

        var_sex = tk.StringVar()
        var_sex.set("male")

        r_btn_male = ttk.Radiobutton(window, text="Чоловіча", variable=var_sex, value="male")
        r_btn_male.pack()

        r_btn_female = ttk.Radiobutton(window, text="Жіноча", variable=var_sex, value="female")
        r_btn_female.pack()

        ttk.Label(window, text="Рівень вашої активності").pack()

        var_activity = tk.StringVar()
        var_activity.set("low")

        r_btn_activity_low = ttk.Radiobutton(window, variable=var_activity, value="low", text="Низький")
        r_btn_activity_low.pack()

        r_btn_activity_pomirn = ttk.Radiobutton(window, variable=var_activity, value="pomirn", text="Помірний")
        r_btn_activity_pomirn.pack()

        r_btn_activity_middle = ttk.Radiobutton(window, variable=var_activity, value="middle", text="Середній")
        r_btn_activity_middle.pack()

        r_btn_activity_high = ttk.Radiobutton(window, variable=var_activity, value="high", text="Високий")
        r_btn_activity_high.pack()

        r_btn_activity_very_high = ttk.Radiobutton(window, variable=var_activity, value="very_high", text="Дуже високий")
        r_btn_activity_very_high.pack()

        ttk.Label(window, text="Чого ви хочете?").pack()

        var_want = tk.StringVar()
        var_want.set("lose")

        r_btn_want_lose = ttk.Radiobutton(window, variable=var_want, value="lose", text="Схуднути")
        r_btn_want_lose.pack()

        r_btn_want_not = ttk.Radiobutton(window, variable=var_want, value="like", text="Не хочу міняти вагу")
        r_btn_want_not.pack()

        r_btn_want_gain = ttk.Radiobutton(window, variable=var_want, value="gaine", text="Хочу набрати вагу")
        r_btn_want_gain.pack()


        ttk.Button(window, text="Ввести", command=lambda: self.enter_params(
            username, entry_mass.get(), entry_growth.get(), entry_age.get(),
            var_sex.get(), var_activity.get(), var_want.get(), root, window
        )).pack()

        ttk.Button(window, text="Вийти", command=lambda: window.quit()).pack()

    def enter_params(self, username, mass, growth, age, sex, activity, want, root, window):
        if mass == "" or growth == "" or age == "":
            ErrorEmptyPage(root)
        else:
            pycsv.write_params(username, mass, growth, age, sex, activity, want)
            window.withdraw()
            MenuPage(root, username, calculate.imt_category(calculate.imt(mass, growth)), calculate.kalor(username))

class ErrorEmptyPage:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Помилка!")
        self.window.geometry('200x125')

        frame = ttk.Frame(self.window, padding=10)

        ttk.Label(self.window, text="Незаповнені всі поля").pack()


class ErrorWrongPasswordPage:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Помилка!")
        self.window.geometry("225x150")

        frame = ttk.Frame(self.window, padding=15)

        ttk.Label(self.window, text="Користувач з таким ніком існує.\nНеправильний пароль").pack()


class MenuPage:
    def __init__(self, root, username, imt_set, kalor_set):
        self.window = tk.Toplevel(root)
        self.window.title("Меню")
        self.window.geometry('400x300')

        frame = ttk.Frame(self.window, padding=10)

        mass_growth = pycsv.get_choosed_data(username)

        var_imt = tk.StringVar()
        var_imt.set(imt_set)

        var_kalor = tk.StringVar()
        var_kalor.set(kalor_set)

        tk.Label(self.window, textvariable=var_imt).pack()
        tk.Label(self.window, textvariable=var_kalor).pack()


        tk.Button(self.window, text="Змінити дані", command=lambda: self.change_params(root, username)).pack()

        tk.Button(self.window, text="Новий день", command=lambda: self.new_day(root, self.window, username)).pack()

        tk.Button(self.window, text="Я поїв", command=lambda: self.btn_eat(root, username, self.window)).pack()

        tk.Button(self.window, text="Таблиця їжі", command=lambda: self.table(root, self.window)).pack()

        tk.Button(self.window, text="Вийти", command=lambda: self.window.quit()).pack()

    def change_params(self, root, username):
        self.window.withdraw()
        ParametersPage(root, username)


    def btn_eat(self, root, username, window):
        window.withdraw()
        IEatPage(root, username)

    def new_day(self, root, window, username):
        pycsv.zeroing(username)
        window.withdraw()
        s = pycsv.get_choosed_data(username)
        MenuPage(root, username, calculate.imt_category(calculate.imt(float(s[2]), s[3])),
                 calculate.kalor(username))

    def table(self, root, window):
        TablePage(root)

class IEatPage:
    def __init__(self, root, username):

        self.window = tk.Toplevel(root)
        self.window.title("Я поїв")
        self.window.geometry('250x150')

        frame = ttk.Frame(self.window, padding=10)

        tk.Label(self.window, text="Що ви з'їли").pack()

        entry_food = tk.Entry(self.window)
        entry_food.pack()

        tk.Label(self.window, text="Скільки ви з'їли у грамах").pack()

        entry_grams = tk.Entry(self.window)
        entry_grams.pack()

        tk.Button(self.window, text="Ввести", command=lambda: self.btn_ieat(entry_food.get().lower(), entry_grams.get(), root, username, self.window)).pack()

    def  btn_ieat(self, food, grams, root, username, window):
        if food == "" or grams == "":
            ErrorEmptyPage(root)
        else:
            if pycsv.check_food(food) == True:
                window.withdraw()
                calculate.kalor_progress(username, food, grams)
                s = pycsv.get_choosed_data(username)
                MenuPage(root, username, calculate.imt_category(calculate.imt(float(s[2]), s[3])),
                         calculate.kalor(username))

            else:
                NewFoodPage(root, food)


class NewFoodPage:
    def __init__(self, root, food):

        self.window = tk.Toplevel(root)
        self.window.title("Нова страва")
        self.window.geometry('250x300')

        frame = ttk.Frame(self.window, padding=10)

        tk.Label(self.window, text="Калорій на 100г").pack()

        calories_entry = tk.Entry(self.window)
        calories_entry.pack()

        tk.Label(self.window, text="Протеїну на 100г").pack()

        protein_entry = tk.Entry(self.window)
        protein_entry.pack()

        tk.Label(self.window, text="Жирів на 100г").pack()

        fats_entry = tk.Entry(self.window)
        fats_entry.pack()

        tk.Label(self.window, text="Вуглеводів на 100г").pack()

        carbon_entry = tk.Entry(self.window)
        carbon_entry.pack()

        tk.Button(self.window, text="Додати", command=lambda: self.add_food(root, calories_entry.get(), protein_entry.get(),
                                                                            fats_entry.get(), carbon_entry.get(), food)).pack()

    def add_food(self, root, calories, protein, fats, carbon, food):

        if calories == "" or protein == "" or fats == "" or carbon == "":
            ErrorEmptyPage(root)
        else:
            pycsv.save_food(food, calories, protein, fats, carbon)
            self.window.withdraw()

class TablePage:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Таблиця")
        self.window.geometry('300x350')

        frame = ttk.Frame(self.window, padding=10)

        s = pycsv.get_food_table()

        for i in s:
            tk.Label(self.window, text=i).pack()
def main():
    root = tk.Tk()
    root.withdraw()
    LoginPage(root)
    root.mainloop()


if __name__ == "__main__":
    main()

