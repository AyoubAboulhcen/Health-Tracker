# HealthTrack 

HealthTrack is a project I'm building starting from day one of learning Python .
Every new concept I learned, I applied directly to this project.
It helped me understand Python faster than any exercises could.

## Version History
- v1.0 — Basic variables, math, and if/else logic
- v1.1 — Using loops and try/except to stop crashes
- v1.2 — Moving code into Classes and Methods
- v1.3 — SQLite database integration and modular file structure
- v1.4 — Secure login using bcrypt password hashing

## What it does
- **Secure Authentication:** Hashes passwords using bcrypt. Locks the program after 3 failed login attempts.
- **Persistent Storage:** Saves personal data and daily logs in an SQLite database.
- **Automated Calculations:** Calculates BMI and BMR using stored user profiles.
- **Profile Management:** Collects and validates name, height, birth date, and gender.
- **Progress Tracking:** Records daily weight, sleep hours, and calorie intake.
- **Goal Setting:** Suggests ideal weight ranges and daily calorie targets based on BMI category.

## What I learned building this
- Functions, parameters, and return values
- Input validation using loops and try/except
- Object-Oriented Programming — classes, methods, and constructors
- Database integration — creating tables, inserting and fetching records using sqlite3
- Modular programming — splitting logic across multiple files (modules.py, check_file.py,
  check_password.py)
- Date manipulation — calculating age from a birth date using the datetime module
- Security — hashing passwords with bcrypt and implementing brute-force protection with sys.exit()
- Input sanitization — cleaning raw user input before storing it in the database

## Project Structure
Health_Tracker/
├── src/
  ├── __init__.py
  ├── __main__.py        # Entry point
  ├── modules.py         # User class and all core logic
  ├── check_file.py      # Checks if a user profile exists
  └── check_password.py  # Handles login and brute-force protection

## How to run
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python __main__.py`

## Coming Soon
- Input validation and error handling improvements.
- Visual Analytics: Generating charts and graphs to visualize weight loss and sleep trends over
  time.
- Data export to CSV

## Note
This is a learning project built while studying Python Essentials 1 & 2 and utilizing resources from w3schools.
This was built concept by concept, mistake by mistake.
!! NO VIBE CODING OR ASKING AI !!

