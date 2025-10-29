import csv


def read_csv_files(file_paths: list):
    for file_path in file_paths:
        with open(file_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield row

