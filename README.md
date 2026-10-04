🎓 IIPS Academic Risk Prediction System

An Object-Oriented Analysis and Design (OOAD) project to evaluate and predict academic risk levels for students based on attendance metrics and assessment performance trends.

✨ Key Features

Attendance Risk: Evaluates risk below the 75% attendance threshold.

Assessment Risk: Evaluates risk below the passing benchmark of 50 marks.

Trend Risk: Identifies downward performance trajectories between consecutive exams.

Semester Tracking: Supports semester-wise evaluation records (Semesters 1 through 8).

SQLite Database: Automatically logs student evaluations and historical records.

Interactive Web UI: Clean interface built with Flask and HTML5.

📂 Project Architecture

app.py: Flask application, routing, and database integration

risk_engine.py: Core risk computation algorithms

schema.sql: Database schema and index definitions

templates/index.html: Web frontend interface

README.md: Project documentation

📐 Risk Calculation Formulae

Attendance Risk (%):

Calculates the deficit when attendance is below 75%:

max(0, (75 - Attendance) / 75 * 100)

Assessment Risk (%):

Calculates the deficit when marks are below 50:

max(0, (50 - Current Marks) / 50 * 100)

Trend Risk (%):

Measures the drop between previous and current marks:

max(0, (Previous Marks - Current Marks) / 50 * 100)

Total Risk Percentage:

Total Risk = (0.4 * Attendance Risk) + (0.4 * Assessment Risk) + (0.2 * Trend Risk)

📊 Risk Categories

HIGH Risk: Total Risk >= 70%

MEDIUM Risk: Total Risk between 35% and 69%

LOW Risk: Total Risk < 35%

🚀 Setup and Execution

Install Flask

Run: pip install flask

Run Application

Run: python app.py

Open in Browser

Navigate to: http://127.0.0.1:5000/
