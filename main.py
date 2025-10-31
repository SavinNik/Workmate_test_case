import csv
import argparse
from tabulate import tabulate
from reports.generate_reports import generate_report


def read_csv_files(file_paths: list):
    """Чтение csv файлов и возврат списка словарей"""
    for file_path in file_paths:
        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield row

def parse_args():
    """Парсинг аргументов командной строки"""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--files",
        nargs="*",
        required=True,
        help="Пути к csv файлам"
    )

    parser.add_argument(
        "--report",
        required=True,
        choices=["average-rating"],
        help="Тип отчета"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    data = list(read_csv_files(file_paths=args.files))
    report = generate_report(report_type=args.report, data=data)
    if report:
        print(tabulate(
            report,
            headers="keys",
            tablefmt="grid",
            floatfmt=".2f"
        ))
    else:
        print("Данные для отчета не найдены")


if __name__ == '__main__':
    main()

