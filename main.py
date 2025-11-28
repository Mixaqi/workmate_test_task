from app.registry import REPORTS
from app.file_reader import read_csv_files
from app.report import print_report
from app.cli import setup_cli_parser


def main() -> None:
    args = setup_cli_parser()
    rows = read_csv_files(args.files)
    report_entry = REPORTS[args.report]
    report_data = report_entry.func(rows)
    print_report(report_data, headers=report_entry.headers)


if __name__ == "__main__":
    main()
