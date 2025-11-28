from pathlib import Path

from app.aliases import CsvFile
from app.file_reader import read_csv_files


def test_read_single_csv_file(tmp_path: Path) -> None:
    """Test reading a single CSV file
    Creates a temp CSV file with one row and checks that read_csv_file parses it into
    a list of dicts
    """
    file1 = tmp_path / "file1.csv"
    file1.write_text("position,performance\nDev,5.0")
    rows: CsvFile = read_csv_files([str(file1)])
    assert len(rows) == 1
    assert rows[0]["position"] == "Dev"
    assert rows[0]["performance"] == "5.0"


def test_read_multiple_csv_file(tmp_path: Path) -> None:
    """Test reading multiple CSV files
    Creates two temporary CSV files, reads them together, and checks correctness
    """
    file1 = tmp_path / "file1.csv"
    file2 = tmp_path / "file2.csv"
    file1.write_text("position, performance\nFrontEnd Dev, 5.0")
    file2.write_text("position,performance\nQA Engineer,4.5")

    rows: CsvFile = read_csv_files([str(file1), str(file2)])
    assert len(rows) == 2
    positions = [r["position"] for r in rows]
    assert "FrontEnd Dev" in positions
    assert "QA Engineer" in positions
