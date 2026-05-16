
from charts import main_chart, calories_chart

def chart():
    print("what are the charts you want to see ?")
    print(" type 1 for weight progression over time with the ideal healh range ")
    print(" type 2 for calories taken vs calories needed ")
    
def slt_chart():
    
    for i in range(3):
        value = input()
        if value == "1":
             main_chart()
        elif value == "2" :
              calories_chart()
        else :
              print("nothing found")

