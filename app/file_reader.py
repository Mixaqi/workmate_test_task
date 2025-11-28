import csv
from pathlib import Path

CsvRow = dict[str, str]
CsvFile = list[CsvRow]


def read_csv_files(paths: list[str]) -> CsvFile:
    result: CsvFile = []

    for path in paths:
        file_path = Path(path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {path}")

        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            rows: CsvFile = list(reader)
            result.extend(rows)

    return result
