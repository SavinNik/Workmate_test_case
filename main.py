import argparse
import csv
from pathlib import Path
from typing import List

from tabulate import tabulate

from reports.generate_reports import generate_report
from reports.models import EmployeeData


def read_csv_files(file_paths: List[str]) -> List[EmployeeData]:
    """Чтение csv файлов и возврат списка словарей"""
    data: List[EmployeeData] = []

    for file_path in file_paths:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        if not path.is_file():
            raise ValueError(f"Не является файлом: {file_path}")
        if not path.name.endswith(".csv"):
            raise TypeError("Файл должен быть с расширением .csv ")

        with open(path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                typed_row: EmployeeData = {
                    "name": row["name"],
                    "position": row["position"],
                    "completed_tasks": row["completed_tasks"],
                    "performance": row["performance"],
                    "skills": row["skills"],
                    "team": row["team"],
                    "experience_years": row["experience_years"]
                }
                data.append(typed_row)
    return data


def parse_args():
    """Парсинг аргументов командной строки"""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--files",
        nargs="*",
        required=True,
        help="Путь к csv файлам")

    parser.add_argument(
        "--report",
        required=True,
        choices=["performance"],
        help="Тип отчета")
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        data = read_csv_files(args.files)
    except (FileNotFoundError, ValueError, TypeError) as e:
        print(f"Ошибка при чтении файлов: {e}")
        return

    try:
        report_data = generate_report(args.report, data)
    except ValueError as e:
        print(f"Ошибка при формировании отчета: {e}")
        return

    if report_data:
        print(tabulate(
            report_data,
            headers="keys",
            tablefmt="grid",
            floatfmt=".2f")
        )
    else:
        print("Нет данных для формирования отчета")


if __name__ == "__main__":
    main()
