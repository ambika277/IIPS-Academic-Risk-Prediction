import sqlite3
from flask import Flask, render_template, request, jsonify
from risk_engine import calculate_risk

app = Flask(__name__)
DB_NAME = "academic_risk.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    with open("schema.sql", "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def save_record(student_id, full_name, semester, attendance, current_marks, previous_marks, result):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Insert or update student
    cursor.execute("""
        INSERT INTO students (student_id, full_name, semester)
        VALUES (?, ?, ?)
        ON CONFLICT(student_id) DO UPDATE SET 
            full_name = excluded.full_name,
            semester = excluded.semester
    """, (student_id, full_name, semester))

    # Insert evaluation record
    cursor.execute("""
        INSERT INTO risk_evaluations (
            student_id, attendance, current_marks, previous_marks,
            attendance_risk, assessment_risk, trend_risk,
            risk_score, risk_percentage, risk_level
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        student_id,
        attendance,
        current_marks,
        previous_marks,
        result["attendance_risk"],
        result["assessment_risk"],
        result["trend_risk"],
        result["risk_score"],
        result["risk_percentage"],
        result["risk_level"]
    ))
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json() or {}

        student_id = str(data.get("student_id", "IIPS001")).strip()
        full_name = str(data.get("full_name", "Student")).strip()
        semester = int(data.get("semester", 1))
        attendance = float(data.get("attendance", 0))
        current_marks = float(data.get("current_marks", 0))
        previous_marks = float(data.get("previous_marks", 0))

        # Compute risk
        result = calculate_risk(attendance, current_marks, previous_marks)

        # Save to SQLite
        save_record(student_id, full_name, semester, attendance, current_marks, previous_marks, result)

        return jsonify(result)
    except Exception as e:
        print("Error during /predict:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)