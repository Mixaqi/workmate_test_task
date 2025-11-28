import pytest

from app.cli import setup_cli_parser


def test_setup_cli_parser_missing_required(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that setup_cli_parser raises SystemExit when required arguments are missed"""
    monkeypatch.setattr("sys.argv", ["main.py", "--report", "performance"])
    with pytest.raises(SystemExit):
        setup_cli_parser()

    monkeypatch.setattr("sys.argv", ["main.py", "--files", "data/file1.csv"])
    with pytest.raises(SystemExit):
        setup_cli_parser()
