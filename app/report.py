from collections import defaultdict

from tabulate import tabulate

from app.aliases import CsvFile
from app.logger import logger


def calculate_report_performance_average(
    rows: CsvFile, key_column: str, value_column: str
) -> dict[str, float]:
    totals_by_position: defaultdict[str, float] = defaultdict(float)
    counts_by_position: defaultdict[str, int] = defaultdict(int)

    for row in rows:
        position = row[key_column].strip()
        try:
            value = float(row[value_column])
        except ValueError as e:
            raise e

        totals_by_position[position] += value
        counts_by_position[position] += 1
    
    if not totals_by_position:
        logger.warning("No correct data")
        return {}
    

    performance_by_position = {
        pos: totals_by_position[pos] / counts_by_position[pos]
        for pos in totals_by_position
    }
    logger.info(f"Calculated performance for {len(performance_by_position)} positions")
    return performance_by_position


def print_report(data_dict: dict[str, float], headers: list[str]) -> None:
    table_data = list(data_dict.items())
    print(tabulate(table_data, headers=headers))
