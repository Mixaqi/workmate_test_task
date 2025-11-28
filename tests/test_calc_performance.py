from app.report import calculate_report_performance


def test_calculate_avg_performance():
    rows = [
        {"position": "Backend developer", "performance": "10"},
        {"position": "Frontend developer", "performance": "15"},
        {"position": "Backend developer", "performance": "20"},
    ]
    result = calculate_report_performance(rows=rows)

    assert result == {
        "Backend developer": 15,
        "Frontend developer": 15,
    }
