from charts import main_chart , calories_chart

def chart():
    print("what are the charts you want to see ?")
    print(" type 1 for weight progression over time with the ideal healh range ")
    print(" type 2 for calories chart ")

def slt_chart():

    value = input()
    for i in range(3):
         value = input()
         if value not in ["1","2"]:
            print("please enter a valid number")
            value = input()
         elif value == "1" :
            main_chart ()
            
         elif value == "2" :
            calories_chart ()
         
slt_chart() 
