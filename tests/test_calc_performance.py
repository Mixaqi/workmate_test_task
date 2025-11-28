import pytest
from app.report import calculate_report_performance_average
from app.aliases import CsvFile

def test_calculate_report_performance_average_normal() -> None:
    rows = [
        {"position": "Dev", "performance": "5.0"},
        {"position": "Dev", "performance": "3.0"},
        {"position": "QA", "performance": "4.0"},
    ]
    result = calculate_report_performance_average(rows, "position", "performance")
    assert result == {"Dev": 4.0, "QA": 4.0}

def test_calculate_report_performance_average_invalid_value() -> None:
    rows = [
        {"position": "Dev", "performance": "5.0"},
        {"position": "Dev", "performance": "abc"},
    ]
    with pytest.raises(ValueError):
        calculate_report_performance_average(rows, "position", "performance")

def test_calculate_report_performance_average_empty() -> None:
    rows: CsvFile = []
    result = calculate_report_performance_average(rows, "position", "performance")
    assert result == {}

