
#-----------------------------the functions--------------------------------------------------------------------
class User :
    def __init__(self):
        self.name = ""
        self.height = 0
        self.weight = 0
        self.age = 0
        self.bmi = 0
        self.gender = 0
        self.bmr = 0

    def bmi_data(self):
        # Method to handle BMI , height, weight, and age
        while True:
            try:
                user_height = (input("tell me about your height in cm"))
                user_weight = (input("tell me about your weight in kg"))
                user_age = (input("tell me about your age in years"))
                self.height = int("".join([c for c in user_height if c.isdigit()]))
                self.weight = int("".join([c for c in user_weight if c.isdigit()]))
                self.age = int("".join([c for c in user_age if c.isdigit()]))
                self.bmi = self.weight / ((self.height / 100) ** 2)
                if self.bmi < 10 or self.bmi > 60:
                    print("sorry there is a problem with your data")
                else:
                    break
            except ValueError:
                print("Please make sure to include numbers for height, weight, and age.")

    def bmr_data(self):
        # method to handle gender and bmr
        while True:
            self.gender = input("tell me about your gender").lower().strip()
            if not self.gender in ["male", "female"]:
                print("PLZ enter male or female")
            else:
                break
        if self.gender in ["male"]:
            self.bmr = (self.weight * 10) + (6.25 * self.height) - (5 * self.age) + 5
        else:
            self.bmr = (self.weight * 10) - (6.25 * self.height) - (5 * self.age) - 161

    def data_taken(self):
        self.name = input("how can i call you plz")
        self.bmi_data()
        self.bmr_data()
        
    def ideal_weights(self):
        min_weight = 18.5 * ((self.height/100) ** 2)
        max_weight = 24.9 * ((self.height/100) ** 2)
        return min_weight, max_weight

    def introduce_the_bmi(self):
        if 16 <= self.age <= 40:
            if self.bmi <= 18.5:
                ibmi = "your under weight , is it hard to eat "
            elif 18.5 < self.bmi <= 25:
                ibmi = " you are in perfect shape i like that "
            elif 25 < self.bmi <= 30:
                ibmi = " overweight , hhhhhh kinda chuby "
            else:
                ibmi = "obese , you need to start working out right now "
        else:
            ibmi = " sorry i'm not built to help you yet "
        return ibmi
    def seggest_plan(self):
        calories_needed = 0
        plan = "no plan available"
        if 16 <= self.age <= 40:
            if self.bmi <= 18.5:
                plan = "Gain weight "
                calories_needed = self.bmr + 500
            elif 18.5 < self.bmi <= 25:
                plan = "Maintain weight "
                calories_needed = self.bmr
            elif 25 < self.bmi <= 30:
                plan = "lose weight "
                calories_needed = self.bmr - 500
            else:
                plan = "lose weight Aggressively "
                calories_needed = self.bmr - 900
        return plan, calories_needed
    def describ_user(self,ibmi,min_weight,max_weight,plan, calories_needed):
        print("+--------------------------i'm describing you right now focus----------------------+")
        print(f"|                {self.name} your are currently {self.age} years old")
        print(f"|             you are {self.height/100} m  , and your weight is {self.weight} kg")
        print(f"|      your bmi is {round(self.bmi, 2)} , it means you are {ibmi}    ")
        print(f"|               your Ideal weight range is from {round(min_weight, 1)} to {round(max_weight, 1)} kg")
        print(f"|           your plan is to {plan} , and your daily calories needed is {calories_needed}")
        print("+----------------------------------------------------------------------------------+")

#--------------------------------the programme----------------------------------------------------#
user = User()
user.data_taken()
min_weight,max_weight=user.ideal_weights()
ibmi=user.introduce_the_bmi()
plan,calories_needed=user.seggest_plan()
user.describ_user(ibmi,min_weight,max_weight,plan, calories_needed)
print()