import csv
from pathlib import Path

from app.aliases import CsvFile
from app.logger import logger


def read_csv_files(paths: list[str]) -> CsvFile:
    result: CsvFile = []

    for raw_path in paths:
        file_path = Path(raw_path)
        logger.info(f"Processing path: {raw_path}")

        if file_path.suffix.lower() != ".csv":
            raise ValueError(f"Invalid file extension (expected .csv): {raw_path}")

        if not file_path.is_file():
            raise FileNotFoundError(f"File not found: {raw_path}")
        try:
            with open(file_path, "r", newline="") as file:
                reader = csv.DictReader(file)
                rows: CsvFile = list(reader)
                result.extend(rows)
                logger.info(f"Read {len(rows) + 1} rows from {raw_path}")
        except OSError as e:
            raise OSError(f"Error reading file {raw_path}: {e}")

    return result
