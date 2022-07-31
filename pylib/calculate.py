from pylib import pycsv

def imt(mass, growth):
    s = float(mass) / (float(growth) * 10**(-2))**2
    return s

def imt_category(imt_index):
    cat = "Категорія ІМТ: "
    if imt_index < 18.5:
        s = "нижче нормальної ваги."
    elif imt_index >= 18.5 and imt_index < 25:
        s = "нормальна вага."
    elif imt_index >= 25 and imt_index < 30:
        s = "є зайва вага."
    elif imt_index >= 30 and imt_index < 35:
        s = "ожиріння 1 степені."
    elif imt_index >= 35 and imt_index < 40:
        s = "ожиріння 2 степені."
    elif imt_index >= 40:
        s = "ожиріння 3 степені"

    s = cat + s

    return s

def kalor(username):

    data = pycsv.get_choosed_data(username)
    mass = float(data[2])
    growth = float(data[3])
    age = float(data[4])
    sex = data[5]
    activity = data[6]
    want = data[7]


    if sex == "male":
        bmr = 88.362 + (13.397 * mass) + (4.799 * growth) + (5.677 * age)
    elif sex == "female":
        bmr = 447.593 + (9.247 * mass) + (3.097 * growth) + (4.33 * age)

    if activity == "low":
        k = 1.2
    elif activity == "pomirn":
        k = 1.375
    elif activity == "middle":
        k = 1.55
    elif activity == "high":
        k = 1.725
    elif activity == "very_high":
        k = 1.9


    kbju = bmr * k

    if want == "lose":
        required_calories = 0.8 * kbju
    elif want == "like":
        required_calories = kbju
    elif want == "gaine":
        required_calories = 1.2 * kbju
    else:
        print("Error")


    required_proteins = required_calories * 0.1
    required_fats = required_calories * 0.25
    required_carbonhydrates = required_calories * 0.65

    s = [int(required_calories), int(required_proteins), int(required_fats), int(required_carbonhydrates)]

    x = pycsv.get_choosed_data(username)

    msg = "Ви з'їли {0} калорій з {1}\nВи з'їли {2} протеїнів з {3}\n Ви з'їли {4} жирів з {5}\n Ви з'їли {6} вуглеводів з {7}\n".format(x[8], s[0], x[9], s[1], x[10], s[2], x[11], s[3])

    return msg

def kalor_progress(username, food, grams):
    data = pycsv.get_food_data(food)
    s = pycsv.get_choosed_data(username)



    calories = float(s[8]) + float(data[1]) * (float(grams) * 0.01)
    protein = float(s[9]) + float(data[2]) * (float(grams) * 0.01)
    fats = float(s[10]) + float(data[3]) * (float(grams) * 0.01)
    carbon = float(s[11]) + float(data[4]) * (float(grams) * 0.01)

    pycsv.save_db_food(username, calories, protein, fats, carbon)




