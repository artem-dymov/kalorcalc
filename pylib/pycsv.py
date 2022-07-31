import csv

def get_read_db():
    db_file = open('pylib/db.csv', encoding='utf-8-sig', newline='')
    db_reader = csv.reader(db_file, delimiter=',')
    return db_reader

def get_write_db():
    db_file = open('pylib/db.csv', 'w', encoding='utf-8-sig', newline='')
    db_writer = csv.writer(db_file, delimiter=',')
    return db_writer

def get_read_food():
    db_file = open('pylib/food.csv', encoding='utf-8-sig', newline='')
    db_reader = csv.reader(db_file, delimiter=',')
    return db_reader

def get_write_food():
    db_file = open('pylib/food.csv', 'w', encoding='utf-8-sig', newline='')
    db_writer = csv.writer(db_file, delimiter=',')
    return db_writer



def get_usernames():
    db_reader = get_read_db()

    s = []
    print(s)
    for row in db_reader:
        s.append(row[0])
    return s


def check_password(username, password):
    db_reader = get_read_db()

    for row in db_reader:
        if username.lower() == row[0]:
            if password == row[1]:
                return True
            else:
                return False

def auth_writer(username, password):
    db_reader = get_read_db()
    s = []
    for row in db_reader:
        s.append(row)
    s.append([username.lower(), password])
    db_writer = get_write_db()
    db_writer.writerows(s)


def write_params(username, mass, growth, age, sex, activity, want):
    db_reader = get_read_db()
    db_reader2 = get_read_db()
    s = []
    for row in db_reader:
        if username == row[0]:
            s.extend([row[0], row[1]])


    s.extend([mass, growth, age, sex, activity, want])

    if len(s) < 9:
        s.extend([0, 0, 0, 0])
        print("1")
    else:
        print(len(s))

    db_reader = get_read_db()

    data = []
    for row in db_reader:
        if row[0] == username:
            pass
        else:
            data.append(row)

    data.append(s)

    db_writer = get_write_db()
    db_writer.writerows(data)


def get_choosed_data(username):
    db_reader = get_read_db()

    s = []
    for row in db_reader:
        if row[0] == username:
            for i in row:
                s.append(i)

    return s

def rewrite_param(username):
    db_reader = get_read_db()
    s = []
    for row in db_reader:
        if row[0] == username:
            for el in row:
                s.append(el)

def check_food(food_name):
    food_reader = get_read_food()
    flag = False
    for row in food_reader:
        if row[0] == food_name:
                flag = True

    return flag

def save_food(food_name, calories, protein, fats, carbon):
    food_reader = get_read_food()

    s = []
    for food in food_reader:
        s.extend([food])

    s.append([food_name, calories, protein, fats, carbon])
    food_writer = get_write_food()
    food_writer.writerows(s)

def get_food_data(food):
    food_reader = get_read_food()

    s = []
    for row in food_reader:
        if row[0] == food:
            for i in row:
                s.append(i)

    return s

def save_db_food(username, calories, protein, fats, carbon):
    db_reader = get_read_db()

    s = []
    for row in db_reader:
        if row[0] == username:

            row.pop(8)
            row.pop(8)
            row.pop(8)
            row.pop(8)
            row.extend([calories, protein, fats, carbon])
        s.extend([row])



    db_writer = get_write_db()
    db_writer.writerows(s)

def zeroing(username):
    db_reader = get_read_db()

    s = []
    for row in db_reader:
        if row[0] == username:
            row.pop(8)
            row.pop(8)
            row.pop(8)
            row.pop(8)
            row.extend([0,0,0,0])
        s.extend([row])


        db_writer = get_write_db()
        db_writer.writerows(s)

def get_food_table():
    food_reader = get_read_food()

    s = []
    for row in food_reader:
      s.append(row)

    return s