# 🩺 Health Tracker

A command-line health tracking application built with Python that securely stores user health data, calculates BMI and BMR, and tracks daily progress using an SQLite database.

> This project demonstrates object-oriented programming, secure authentication, data persistence, and modular application design.

---

## 📌 Overview

Health Tracker is a Python CLI application designed to help users monitor their personal health information over time.

The application allows users to create secure accounts, record daily health metrics, calculate body measurements, and store all information locally using SQLite.

This project focuses on building a complete, well-structured Python application rather than a collection of isolated programming exercises.

---

## ✨ Features

### 🔐 Secure Authentication

- Password hashing using **bcrypt**
- Protection against brute-force login attempts
- Secure user authentication

### 👤 User Profile Management

- Create personal profiles
- Store height, birth date, and gender
- Input validation for user data

### 📊 Health Calculations

Automatically calculates:

- Body Mass Index (BMI)
- Basal Metabolic Rate (BMR)
- Healthy weight range
- Daily calorie recommendations

### 📝 Daily Progress Tracking

Track daily:

- Weight
- Sleep hours
- Calorie intake

All records are stored permanently using SQLite.

### 💾 Persistent Storage

- SQLite database
- Automatic data retrieval
- Organized database structure

---

# 🛠 Technologies Used

- Python 3
- SQLite
- bcrypt
- Object-Oriented Programming (OOP)
- datetime
- Modular Python Architecture

---

# 📁 Project Structure

```
Health-Tracker/
│
├── src/
│   ├── __main__.py          # Application entry point
│   ├── modules.py           # Core application logic
│   ├── check_file.py        # User profile verification
│   └── check_password.py    # Authentication system
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Getting Started

## Clone the repository

```bash
git clone https://github.com/AyoubAboulhcen/Health-Tracker.git
```

## Create a virtual environment

```bash
python -m venv venv
```

## Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the application

```bash
python -m src
```

---

# 💡 Technical Highlights

This project demonstrates practical experience with:

- Object-Oriented Programming
- Modular project organization
- SQLite database design
- Secure password hashing
- Exception handling
- Input validation
- Working with dates and time
- File organization
- Clean separation of application logic

---

# 📈 Planned Improvements

Future versions may include:

- Data visualization using Matplotlib
- CSV data export
- Progress charts
- Goal completion statistics
- Improved input validation
- Configuration file support

---

# 📷 Screenshots

*Screenshots and demo GIFs will be added in future updates.*

---

# 🎯 Purpose

This project was built to practice developing a complete Python application from the ground up.

Instead of solving isolated coding exercises, the goal was to design a maintainable application that combines secure authentication, persistent storage, modular architecture, and health data management into a single project.

---

# 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Ayoub Aboulhcen**

Python Developer focused on:

- Python Automation
- Data Processing
- Excel Automation
- Data Cleaning
- Desktop & CLI Applications

GitHub:
https://github.com/AyoubAboulhcen
