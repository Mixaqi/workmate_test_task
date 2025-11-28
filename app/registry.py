from typing import Any, Callable, NamedTuple

from app.report import CsvFile, calculate_report_performance_average


class Report(NamedTuple):
    func: Callable[[CsvFile], Any]
    key_column: str
    value_column: str
    headers: list[str]


REPORTS: dict[str, Report] = {
    "performance": Report(
        func=lambda rows: calculate_report_performance_average(
            rows, key_column="position", value_column="performance"
        ),
        key_column="position",
        value_column="performance",
        headers=["Position", "Performance"],
    )
}
