#1. Ask name and save it
#2. Collect height, weight, age, sex, training frequency
#3. Calculate BMI and validate it
#4. Calculate BMR
#5. Suggest daily calorie plan based on BMI
#6. Show BMI category and ideal weight range
#7. Describe user summary
#8. (Coming in version 2) Add food calories tracker
#9. (Coming in version 2) Save daily data with dates
#10. (Coming in version 2) Charts for weight, calories, sleep
#-----------------------------the functions needed----------------------------------------------------------------------

def get_user_name(): #this get the user-name and save it
    print ('Hello user')
    name = input("how can i call you???")
    return name

def get_user_data(user_name): #this get the height-weight-and height meters in
    print("okay", user_name, "let's get to know you more,\nfirst let's calculate your BMI and healthy weight range")
    height = int(input("tell me about your height in cm"))
    weight = int(input("tell me about your weight in kg"))
    age = int(input("tell me about your age in years"))
    sex = input("are you , male or female , pleas enter m for male or f if your a female ")
    height_m = height / 100
    return height , weight , age , sex , height_m
def validate_sex (sex): #this check if the user writes the formal values we need
    if sex in ["m","f"]:
       validation = True
    else :
        validation= False
    return validation
def calcule_bmr(user_sex,user_weight,user_height,user_age): #this calculates the Basal Metabolic Rate and save it in bmr
    if user_sex == "m":
        bmr = (user_weight*10)+(6.25*user_height)-(5*user_age)+5
    else :
        bmr = (user_weight*10)-(6.25*user_height)-(5*user_age)-161
    return bmr

def calcule_bmi(user_weight,user_height_m): #this calculates the bmi and save it
    bmi = user_weight / (user_height_m ** 2)
    return bmi

def validate_bmi (user_bmi): # this validates the bmi resultes
    if user_bmi < 10 or user_bmi > 60 :
       return False
    return True
def introduce_the_bmi(user_age,user_bmi): # this describes what the bmi means in ibmi variable
    if 16 <= user_age <= 40 :
        if user_bmi < 18.5:
            ibmi = "your under weight , is it hard to eat "
        elif 18.5 < user_bmi < 25:
            ibmi =" you are in perfect shape i like that "
        elif 25 < user_bmi < 30:
            ibmi = " overweight , hhhhhh kinda chuby "
        else:
            ibmi = "obese , you need to start working out right now "
    else :
        ibmi = " not fit "
    return ibmi
def ideal_weights(user_height_m): #this calculates the ideal weight range of the user and save it
    min_weight=18.5 * (user_height_m **2)
    max_weight=24.9 * (user_height_m **2)
    return min_weight,max_weight
def seggest_plan(user_bmi,user_bmr,user_age):
    calories_needed = 0
    plan = "no plan available"
    if 16 <= user_age <= 40 :
        if user_bmi < 18.5:
            plan = "Gain weight "
            calories_needed = user_bmr +500
        elif 18.5 < user_bmi < 25:
            plan = "Maintain weight "
            calories_needed = user_bmr
        elif 25 < user_bmi < 30:
            plan = "lose weight "
            calories_needed = user_bmr -500
        else:
            plan = "lose weight Aggressively "
            calories_needed = user_bmr - 900
    return plan , calories_needed

def describ_user(user_name, user_age, user_height_m, user_weight, user_bmi ,ibmi, min_weight,max_weight,user_plan,user_calories_needed):
    print("+--------------------------i'm describing you right now focus----------------------+")
    print(f"|                {user_name} your are currently {user_age} years old")
    print(f"|             you are {user_height_m} m  , and your weight is {user_weight} kg")
    print(f"|      your bmi is {round(user_bmi, 2)} , it mean you are {ibmi}    ")
    print(f"|               your Ideal weight range is from {round(min_weight, 1)} to {round(max_weight, 1)} kg")
    print(f"|           your plan is {user_plan} , and your daily calories needed is {user_calories_needed}")
    print("+----------------------------------------------------------------------------------+")
#--------------------------------the programme----------------------------------------------------#

name = get_user_name()
bmi = 0 # i did this so the value defined properly in the loops

while True:
    height, weight, age, sex, height_m = get_user_data(name)
    if not validate_sex(sex):
        print("Please enter m or f only.")
        continue
    bmi = calcule_bmi(weight, height_m)
    if not validate_bmi(bmi):
        print("Something is wrong with your data. Try again.")
        continue
    break
bmr=calcule_bmr(sex,weight,height,age)
plan , calories_needed =seggest_plan(bmi,bmr,age)
ibmi=introduce_the_bmi(age,bmi)
min_weight , max_weight =ideal_weights(height_m)
describ_user(name,age,height_m,weight,bmi,ibmi,min_weight,max_weight,plan,calories_needed)



