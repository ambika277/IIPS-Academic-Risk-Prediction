def calculate_risk(attendance, current_marks, previous_marks):
    # 1. Attendance Risk (% risk)
    attendance_risk = max(0.0, (75 - attendance) / 75 * 100) if attendance < 75 else 0.0

    # 2. Assessment Risk (% risk)
    assessment_risk = max(0.0, (50 - current_marks) / 50 * 100) if current_marks < 50 else 0.0

    # 3. Trend Risk (% risk)
    marks_diff = previous_marks - current_marks
    trend_risk = max(0.0, min(100.0, (marks_diff / 50) * 100)) if marks_diff > 0 else 0.0

    # 4. Total Risk Percentage
    risk_percentage = (0.4 * attendance_risk) + (0.4 * assessment_risk) + (0.2 * trend_risk)

    # 5. Risk Category
    if risk_percentage >= 70.0:
        risk_level = "HIGH"
    elif risk_percentage >= 35.0:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    # Provide BOTH risk_score and risk_percentage to prevent any KeyError
    return {
        "attendance_risk": attendance_risk,
        "assessment_risk": assessment_risk,
        "trend_risk": trend_risk,
        "risk_score": risk_percentage / 100.0,
        "risk_percentage": risk_percentage,
        "risk_level": risk_level
    }

if __name__ == "__main__":
    res = calculate_risk(68, 42, 48)
    print("Test calculation:", res)