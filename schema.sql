CREATE TABLE IF NOT EXISTS students (
    student_id TEXT PRIMARY KEY,
    full_name TEXT NOT NULL,
    program TEXT DEFAULT 'IIPS',
    semester INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS risk_evaluations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    attendance REAL NOT NULL,
    current_marks REAL NOT NULL,
    previous_marks REAL NOT NULL,
    attendance_risk REAL NOT NULL,
    assessment_risk REAL NOT NULL,
    trend_risk REAL NOT NULL,
    risk_score REAL NOT NULL,
    risk_percentage REAL NOT NULL,
    risk_level TEXT NOT NULL,
    evaluated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_risk_student_id ON risk_evaluations(student_id);