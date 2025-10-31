# Анализ рейтинга брендов

## Начало работы

Склонируйте репозиторий:
```bash
git clone https://github.com/yourusername/brand-rating-analysis.git
```
Создайте виртуальное окружение и установите зависимости:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Запуск скрипта
### Положите csv файлы в папку `data`

Для создания отчета по одному csv файлу используйте команду:
```bash
python main.py --files data/ваш_файл.csv --report average-rating
```

Для создания отчета по всем csv файлам используйте команду:

```bash
python main.py --files data/*.csv --report average-rating
```

## Тестирование
Для тестирования используйте команду:
```bash
python -m pytest --cov tests/
```

## Добавление нового типа отчета
1. В файле `main.py` в функцию parse_args() добавьте новый тип отчета в список `choices`:

```python
parser.add_argument(
    "--report",
    required=True,
    choices=["average-rating", "new-report-type"], # Добавьте новый тип отчета
    help="Тип отчета"
)
```
2. В папке `reports` создайте файл `new_report.py` и добавьте в него функцию `generate_new_report_type(data)`:

```python
def generate_new_report_type(data):
    # Реализация нового типа отчета
```

3. В файле `reports/generate_reports.py` в функцию generate_report() добавьте выполнение нового типа отчета:

```python
def generate_report(report_type, data):
    if report_type == "average-rating":
        return generate_average_rating_report(data)
    elif report_type == "new-report-type": # Добавьте новый тип отчета
        return generate_new_report_type(data)
    else:
        raise ValueError(f"Неверный тип отчета")
```