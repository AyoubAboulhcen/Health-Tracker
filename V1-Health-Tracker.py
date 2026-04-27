
#-----------------------------the functions--------------------------------------------------------------------

class User:
    def __init__(self, name, height, weight, age, gender):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.gender = gender
        self.height_m = height / 100

    def validate_gender(self):
        if self.gender in ["m", "f"]:
            validation = True
        else:
            validation = False
        return validation

    def calcule_bmi(self):
        bmi = self.weight / (self.height_m ** 2)
        return bmi

    def validate_bmi(self, user_bmi):
        if user_bmi < 10 or user_bmi > 60:
            return False
        return True

    def calcule_bmr(self):
        if self.gender == "m":
            bmr = (self.weight * 10) + (6.25 * self.height) - (5 * self.age) + 5
        else:
            bmr = (self.weight * 10) - (6.25 * self.height) - (5 * self.age) - 161
        return bmr

    def introduce_the_bmi(self, user_bmi):
        if 16 <= self.age <= 40:
            if user_bmi <= 18.5:
                ibmi = "your under weight , is it hard to eat "
            elif 18.5 < user_bmi <= 25:
                ibmi = " you are in perfect shape i like that "
            elif 25 < user_bmi <= 30:
                ibmi = " overweight , hhhhhh kinda chuby "
            else:
                ibmi = "obese , you need to start working out right now "
        else:
            ibmi = " sorry i'm not built to help you yet "
        return ibmi

    def ideal_weights(self):
        min_weight = 18.5 * (self.height_m ** 2)
        max_weight = 24.9 * (self.height_m ** 2)
        return min_weight, max_weight

    def seggest_plan(self, user_bmi, user_bmr):
        calories_needed = 0
        plan = "no plan available"
        if 16 <= self.age <= 40:
            if user_bmi <= 18.5:
                plan = "Gain weight "
                calories_needed = user_bmr + 500
            elif 18.5 < user_bmi <= 25:
                plan = "Maintain weight "
                calories_needed = user_bmr
            elif 25 < user_bmi <= 30:
                plan = "lose weight "
                calories_needed = user_bmr - 500
            else:
                plan = "lose weight Aggressively "
                calories_needed = user_bmr - 900
        return plan, calories_needed

    def describ_user(self, user_bmi, user_ibmi, user_min_weight, user_max_weight,
                     user_plan, user_calories_needed):
        print("+--------------------------i'm describing you right now focus----------------------+")
        print(f"|                {self.name} your are currently {self.age} years old")
        print(f"|             you are {self.height_m} m  , and your weight is {self.weight} kg")
        print(f"|      your bmi is {round(user_bmi, 2)} , it means you are {user_ibmi}    ")
        print(
            f"|               your Ideal weight range is from {round(user_min_weight, 1)} to {round(user_max_weight, 1)} kg")
        print(f"|           your plan is to {user_plan} , and your daily calories needed is {user_calories_needed}")
        print("+----------------------------------------------------------------------------------+")


def get_user_data():
    print('Hello user')
    name = input("how can i call you???", )
    print("okay", "let's get to know you ")
    height = int(input("tell me about your height in cm"))
    weight = int(input("tell me about your weight in kg"))
    age = int(input("tell me about your age in years"))
    gender = input("plz enter m if you are male or f if you are female ")
    return name, height, weight, age, gender


#--------------------------------the programme----------------------------------------------------#

while True:
    name,height, weight, age, gender= get_user_data()
    bmi=0
    user = User (
        name=name,
        height=height,
        weight=weight,
        age=age,
        gender=gender)
    if not user.validate_gender():
        print("Please enter m or f only.")
        continue
    bmi = user.calcule_bmi()
    if not user.validate_bmi(bmi):
        print("Something is wrong with your data. Try again.")
        continue
    break
bmr= user.calcule_bmr()
plan , calories_needed =user.seggest_plan(bmi,bmr)
ibmi= user.introduce_the_bmi(bmi)
min_weight , max_weight = user.ideal_weights()
user.describ_user(bmi,ibmi,min_weight,max_weight,plan,calories_needed)

