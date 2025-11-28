import pytest

from app.aliases import CsvFile
from app.report import calculate_report_performance_average


def test_calculate_report_performance_average_normal() -> None:
    """Example test with normal function behavior

    Verifies that the function correctly computes the average performance
    for each position when all values are valid numeric strings.

    """
    rows = [
        {"position": "DevOps", "performance": "5.0"},
        {"position": "DevOps", "performance": "3.0"},
        {"position": "QA", "performance": "4.0"},
    ]
    result = calculate_report_performance_average(rows, "position", "performance")
    assert result == {"DevOps": 4.0, "QA": 4.0}


def test_calculate_report_performance_average_invalid_value() -> None:
    """Example test that raises ValueError

    Verifies that the function raises a ValueError with an invalid performance
    """
    rows = [
        {"position": "DevOps", "performance": "5.0"},
        {"position": "DevOps", "performance": "abc"},
    ]
    with pytest.raises(ValueError):
        calculate_report_performance_average(rows, "position", "performance")


def test_calculate_report_performance_average_empty() -> None:
    """Example test with empty input

    Verifies that the function returns an empty dictionary
    """
    rows: CsvFile = []
    result = calculate_report_performance_average(rows, "position", "performance")
    assert result == {}
