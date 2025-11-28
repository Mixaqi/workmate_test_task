import argparse
from argparse import Namespace

from app.registry import REPORTS


def setup_cli_parser() -> Namespace:
    """
    Sets up and parses cmd args
    Returns:
        Namespace: An argparse Namespace object
    """
    parser = argparse.ArgumentParser(
        description="CSV Reporting Tool", allow_abbrev=False
    )
    parser.add_argument("--files", nargs="+", required=True, help="CSV files paths")
    parser.add_argument(
        "--report", required=True, choices=REPORTS.keys(), help="Report name"
    )
    return parser.parse_args()
