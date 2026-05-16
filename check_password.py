import sqlite3
import bcrypt
import sys
def chek_the_password():
    con = sqlite3.connect('user_data.db')
    cu = con.cursor()

    try:
        cu.execute("SELECT Password FROM personal_information")
        result = cu.fetchone()

        stored_password = result[0]

        for i in range(3):
            inpt_pass = input(" What is the password? ").encode('utf-8')

            if bcrypt.checkpw(inpt_pass, stored_password.encode('utf-8')):
                print("Login successful!")
                con.close()
                return True
            else:
                print("Access Denied!")

        sys.exit("Too many failed attempts. Program locked.")

    except Exception as e:
        sys.exit(f"Database error: {e}")