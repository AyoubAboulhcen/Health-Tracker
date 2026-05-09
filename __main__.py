from modules import User
from check_file import check

user = User()

if not check :
        user.make_personal_file()
        user.insert_personal_data()

age=user.age()
user.make_health_tracker_file()
current_weight, sleep, calories_taken = user.get_daily_enteries()
bmi= user.calcul_bmi(current_weight)
bmr = user.calcul_bmr(current_weight,age)
min_weight, max_weight = user.ideal_weights()
plan, calories_needed= user.goal_claories_needed(bmi,bmr)
user.insert_daily_entries(age,current_weight, sleep, calories_needed, calories_taken, bmi, bmr, min_weight, max_weight, plan)


