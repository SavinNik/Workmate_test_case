import csv
import argparse
from tabulate import tabulate


def read_csv_files(file_paths: list):
    """Чтение csv файлов и возврат списка словарей"""
    for file_path in file_paths:
        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield row

def parse_args():
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

print(tabulate(
    read_csv_files(["data/products1.csv", "data/products2.csv"]),
    headers="keys",
    tablefmt="grid",
    floatfmt=".2f"
))