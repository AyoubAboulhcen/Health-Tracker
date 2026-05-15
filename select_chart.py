
from charts import mains_charts, caloriess_charts

def slt_chart():
    print("what are the charts you want to see ?")
    print(" type 1 for weight progression over time with the ideal healh range ")
    print(" type 2 for calories taken vs calories needed ")
    print(" type 3 for your weight cith your sleep ")
    print (" type 4 for your calories consumed with your sleep")
    
    value = input()

    if value == "1":
        mains_charts()
    elif value == "2" :
        caloriess_charts()
    else :
        print("nothing found")

slt_chart ()
