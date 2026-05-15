from matplotlib import pyplot as plt
import sqlite3
#print(plt.style.available)
plt.style.use('ggplot')
def main_chart ():
    con = sqlite3.connect('user_data.db')
    cu = con.cursor()
    
    cu.execute("SELECT Date , Current_Weight , Sleep ,Min_Weight , Max_Weight" \
    " FROM health_tracker ")
    rows = cu.fetchall()
    Date = [row[0] for row in rows]
    Current_Weight = [row[1] for row in rows]
    Sleep = [row[2] for row in rows]
    Min_Weight = [row[3] for row in rows]
    Max_Weight = [row[4] for row in rows]
    print(rows)
    print(Date)
    print(Current_Weight)
    print(Sleep)
    print(Min_Weight)
    print(Max_Weight)

    plt.bar(Date, Current_Weight,width=0.5,color='brown', label='Current Weight')
    plt.plot(Date, Sleep, marker='o', color='blue', label='Sleep')

    plt.xlabel('Date')
    plt.ylabel('Sleep/Weight')
    plt.title('Health Tracker')
    plt.legend()
    plt.grid(True)

    plt.show()

def calories_chart():
    con = sqlite3.connect('user_data.db')
    cu = con.cursor()
    
    cu.execute("SELECT Calories_taken , Calories_needed" \
    " FROM health_tracker ORDER BY Date DESC LIMIT 1")
    row = cu.fetchone()
    Calories_taken =row[0]
    Calories_needed = row[1]
    
    slices = [Calories_taken, Calories_needed]
    labels = ['Calories Taken', 'Calories Needed']
    #explodes = [0.1, 0]  # Explode the first slice (Calories Taken)

    plt.pie(slices, labels=labels, shadow =True, startangle=90,autopct='%1.1f%%')

    plt.title('Calories Taken vs Calories Needed')
    plt.tight_layout()
    plt.show()
    

#main_chart()

calories_chart()

