import sqlite3
import datetime
import bcrypt

class User ():

    def __init__(self):
        #how can i store the database or tables instead of typing all the variables
        pass

    def make_personal_file(self):
        con = sqlite3.connect('user_data.db')
        cu = con.cursor()
        cu.execute("""CREATE TABLE IF NOT EXISTS personal_information ( 
            First text , 
            Last text , 
            Gender text ,
            Birth_date text , 
            Password text,
            Height real 
            )""")
        con.commit()
        con.close()

    def insert_personal_data(self):

        con = sqlite3.connect('user_data.db')
        cu = con.cursor()

        first = input("what is your first name ").lower()
        last = input("what is your last name ").lower()
        birth_date = input("what is your birth_date  as year/month/day format in numbers ").lower()
        user_height = (input("tell me about your height in cm"))

        height = int("".join([c for c in user_height if c.isdigit()]))

        while True:
            gender = input("tell me about your gender").lower().strip()
            if gender not in ["male", "female"]:
                print("PLZ enter male or female")
            else:
                break

        pas = input("what is your password ")
        pwd = bcrypt.hashpw(pas.encode("utf-8"), bcrypt.gensalt())

        cu.execute("INSERT INTO personal_information VALUES (:First, :Last, :Gender, :Birth_date,:Password , :Height)",
                   {'First': first, 'Last': last, 'Gender': gender, 'Birth_date': birth_date, 'Password': pwd.decode('utf-8'),
                    'Height': height})
        con.commit()
        con.close()

    def age (self):

        con = sqlite3.connect('user_data.db')
        cu = con.cursor()

        cu.execute("SELECT Birth_date FROM personal_information")
        row = cu.fetchone()
        birth_date = datetime.datetime.strptime(row[0], "%Y/%m/%d").date()
        today = datetime.date.today()

        age = today.year - birth_date.year

        con.commit()
        con.close()

        return age

    def make_health_tracker_file(self):

        con = sqlite3.connect('user_data.db')
        cu = con.cursor()

        cu.execute("""CREATE TABLE IF NOT EXISTS health_tracker (
        Date text ,
        Age integer ,
        Current_Weight real,
        Sleep integer ,
        Calories_needed integer,
        Calories_taken integer ,
        BMI real,
        BMR integer, 
        Min_Weight real , 
        Max_Weight real,
        Goal text
        )""")

        con.commit()
        con.close()

    def get_daily_enteries (self):
        current_weight = float(input("what is your current weight "))
        sleep = float(input("how much did you slept today sleep "))
        calories_taken = int(input("how much calories did you eat "))

        return current_weight, sleep, calories_taken

    def calcul_bmi (self, current_weight):
        con = sqlite3.connect('user_data.db')
        cu = con.cursor()

        cu.execute("SELECT Height FROM personal_information")
        row = cu.fetchone()
        height = row[0]


        bmi = current_weight / ((height / 100) ** 2)

        con.commit()
        con.close()

        return bmi

    def calcul_bmr (self, current_weight,age):
        con = sqlite3.connect('user_data.db')
        cu = con.cursor()

        cu.execute("SELECT Gender, Height FROM personal_information")
        row = cu.fetchone()
        gender = row[0]
        height = row[1]

        if gender in ["male"]:
            bmr = (current_weight * 10) + (6.25 * height) - (5 * age) + 5
        else:
            bmr = (current_weight * 10) + (6.25 * height) - (5 * age) - 161

        con.commit()
        con.close()

        return bmr

    def ideal_weights(self):
        con = sqlite3.connect('user_data.db')
        cu = con.cursor()

        cu.execute("SELECT Height FROM personal_information")
        row = cu.fetchone()
        height = row[0]

        min_weight = 18.5 * ((height/100) ** 2)
        max_weight = 24.9 * ((height/100) ** 2)

        con.commit()
        con.close()

        return min_weight, max_weight

    def goal_claories_needed(self,bmi,bmr):

        if bmi <= 18.5:
            plan ="gain_weight"
            calories_needed= bmr + 500
        elif 18.5 < bmi <= 25:
            plan ="maintain_weight"
            calories_needed = bmr
        elif 25 < bmi <= 30:
            plan ="lose_weight"
            calories_needed = bmr - 500
        else:
            plan ="lose_weight_aggressively"
            calories_needed = bmr - 750

        return plan, calories_needed

    def insert_daily_entries (self,age,current_weight, sleep,calories_needed, calories_taken,bmi,bmr, min_weight,max_weight,plan):
        con = sqlite3.connect('user_data.db')
        cu = con.cursor()
        cu.execute(
            "INSERT INTO health_tracker VALUES (:Date, :Age, :Current_Weight, :Sleep, :Calories_needed, :Calories_taken, :BMI, :BMR, :Min_Weight, :Max_Weight, :Goal)",
            {'Date':str(datetime.date.today()),
             'Age': age,
             'Current_Weight': current_weight,
             'Sleep': sleep,
             'Calories_needed': calories_needed,
             'Calories_taken': calories_taken,
             'BMI': bmi,
             'BMR': bmr,
             'Min_Weight': min_weight,
             'Max_Weight': max_weight,
             'Goal': plan})

        con.commit()
        con.close()



