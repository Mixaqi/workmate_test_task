from collections import defaultdict
from tabulate import tabulate

CsvRow = dict[str, str]
CsvFile = list[CsvRow]


def calculate_report_performance(
    rows: CsvFile, key_column: str, value_column: str
) -> dict[str, float]:
    totals_by_position: defaultdict[str, float] = defaultdict(float)
    counts_by_position: defaultdict[str, int] = defaultdict(int)

    for row in rows:
        position = row[key_column].strip()
        try:
            value = float(row[value_column])
        except ValueError:
            continue

        totals_by_position[position] += value
        counts_by_position[position] += 1

    performance_by_position = {
        pos: totals_by_position[pos] / counts_by_position[pos]
        for pos in totals_by_position
    }
    return performance_by_position


def print_report(data_dict: dict[str, float], headers: tuple[str, str]) -> None:
    table_data = list(data_dict.items())
    print(tabulate(table_data, headers=headers))
