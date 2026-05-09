# HealthTrack 

HealthTrack is a project I'm building starting from day one of learning Python .
Every new concept I learned, I applied directly to this project.
It helped me understand Python faster than any exercises could.

This is not a tutorial project. It was built concept by concept, mistake by mistake.

## Version History
v1.0 :Basic variables, math, and if/else logic.
v1.1 :Using loops and try/except to stop crashes.
v1.2 :Moving code into Classes and Methods.
v2.0 :SQLite Database integration and Modular file structure.

## What it does
- Persistent Storage: Saves personal data and daily logs in an SQLite database (.db).
- Automated Calculations: Instantly calculates BMI and BMR using stored user profiles.
- Profile Management: Collects and validates name, height, birth date, and gender.
- Progress Tracking: Records daily weight, sleep hours, and calorie intake.
- Goal Setting: Suggests ideal weight ranges and daily calorie targets based on your BMI category.

## What I learned building this
- Functions, parameters, and return values
- Input validation using loops and try/except
- Breaking a complex program into small focused pieces
- Object Oriented Programming — classes, methods, constructors
- Database Integration: How to create tables, insert data, and fetch records using sqlite3.
- Modular Programming: Splitting code into different files (modules.py, check_file.py) for better     organization.
- Date Manipulation: Using the datetime module to calculate age from a birth date and timestamp       daily entries.
- Object-Oriented Programming (OOP): Building a User class to act as the "brain" of the application.
- File Handling: Checking for the existence of files using the os library.

## How to run
Make sure Python is installed, then run:
python health_track.py

## Coming Soon
- Security: Password protection with hashing using hashlib (in progress) 
- Visual Analytics: Generating charts and graphs to visualize weight loss and sleep trends over time.

## Note
This is a learning project built while studying Python Essentials 1 & 2 and utilizing resources from w3schools.
