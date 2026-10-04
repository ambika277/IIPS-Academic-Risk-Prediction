# IIPS Academic Risk Prediction System

An Object-Oriented Analysis and Design (OOAD) project designed to evaluate and predict academic risk levels for students based on attendance metrics and assessment performance trends.

---

## 📌 Features

- **Attendance Risk Evaluation:** Calculates risk based on standard attendance minimum thresholds.
- **Assessment Risk Analysis:** Measures performance deficit against passing benchmarks.
- **Trend Risk Detection:** Identifies deteriorating performance between sequential assessments.
- **Weighted Risk Scoring:** Generates an overall risk percentage and categorizes students into **LOW**, **MEDIUM**, or **HIGH** risk levels.
- **Database Persistence:** Automatically logs evaluations and student details into a local SQLite database.
- **Interactive UI:** User-friendly web portal powered by Flask and HTML5.

---

## 🏗️ Project Architecture

```text
OOAD-Lab-Assignment/
├── app.py               # Flask backend & routing
├── risk_engine.py       # Core prediction algorithms & risk scoring logic
├── schema.sql           # Database schema & table definitions
├── templates/
│   └── index.html       # Frontend interface
└── README.md            # Project documentation

🧮 Risk Calculation LogicThe system evaluates academic risk using three primary metrics:Attendance Risk:$$\text{Attendance Risk} = \max\left(0, \frac{75 - \text{Attendance}}{75} \times 100\right)$$(Applies when attendance is below $75\%$)Assessment Risk:$$\text{Assessment Risk} = \max\left(0, \frac{50 - \text{Current Marks}}{50} \times 100\right)$$(Applies when current score is below $50$ marks)Trend Risk:$$\text{Trend Risk} = \max\left(0, \min\left(100, \frac{\text{Previous Marks} - \text{Current Marks}}{50} \times 100\right)\right)$$(Triggers when previous marks exceed current marks)Overall Risk Formula:$$\text{Total Risk} = (0.4 \times \text{Attendance Risk}) + (0.4 \times \text{Assessment Risk}) + (0.2 \times \text{Trend Risk})$$⚙️ Installation & SetupPrerequisitesPython 3.8+ installed on your system.1. Clone the RepositoryBashgit clone [https://github.com/ambika277/IIPS-Academic-Risk-Prediction.git](https://github.com/ambika277/IIPS-Academic-Risk-Prediction.git)
cd IIPS-Academic-Risk-Prediction
2. Install DependenciesBashpip install flask
3. Run the ApplicationBashpython app.py
4. Access the Web AppOpen your browser and navigate to:Plaintext[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
🗄️ Database DesignThe database schema (schema.sql) contains two main relational tables:students: Stores student identifier, full name, semester, and timestamp.risk_evaluations: Stores each calculated risk assessment, individual metric scores, and final category classifications linked via foreign key
