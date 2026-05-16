from matplotlib import pyplot as plt
import sqlite3

def main_chart ():
    plt.style.use('ggplot')

    con = sqlite3.connect('user_data.db')
    cu = con.cursor()
    
    cu.execute("SELECT Date , Current_Weight ,Min_Weight , Max_Weight" \
    " FROM health_tracker ")
    rows = cu.fetchall()
    Date = [row[0] for row in rows]
    Current_Weight = [row[1] for row in rows]
    Min_Weight = [row[2] for row in rows]
    Max_Weight = [row[3] for row in rows]
    con.close()

    plt.plot(Date, Current_Weight,marker =".",color='brown',linewidth=3, label='Current Weight')
    plt.fill_between(Date, Max_Weight, Min_Weight, color='green', alpha=0.5, label='Ideal Weight Range')

    plt.xlabel('Date')
    plt.ylabel('Weight')
    plt.title('Health Tracker')

    plt.legend()
    plt.tight_layout()
    plt.grid(True)

    plt.show()

def calories_chart():
    plt.style.use('ggplot')

    con = sqlite3.connect('user_data.db')
    cu = con.cursor()
    
    cu.execute("SELECT Calories_taken , Calories_needed" \
    " FROM health_tracker ORDER BY Date DESC LIMIT 1")
    row = cu.fetchone()
    Calories_taken =row[0]
    Calories_needed = row[1]
    con.close()

    slices = [Calories_taken, Calories_needed]
    labels = ['Calories Taken', 'Calories Needed']
    
    plt.pie(slices, labels=labels, shadow =True, startangle=90,autopct='%1.1f%%')

    plt.title('Calories Taken vs Calories Needed')
    plt.tight_layout()
    plt.show()
    
