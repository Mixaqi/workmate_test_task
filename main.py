from app.cli import setup_cli_parser
from app.file_reader import read_csv_files
from app.logger import logger
from app.registry import REPORTS
from app.report import print_report


def main() -> None:
    try:
        args = setup_cli_parser()
        rows = read_csv_files(args.files)
        if not rows:
            logger.warning("No correct data")
            return
        report_entry = REPORTS[args.report]
        report_data = report_entry.func(rows)
        print_report(report_data, headers=report_entry.headers)
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()
