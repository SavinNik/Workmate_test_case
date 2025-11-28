# Анализ эффективности сотрудников

## Требования

- Python 3.10+
- Poetry (для управления зависимостями и виртуальным окружением)
- Tabulate (для вывода таблиц в консоль)

## Начало работы

Склонируйте репозиторий:
```bash
git clone https://github.com/SavinNik/Workmate_test_case
```
Создайте виртуальное окружение и установите зависимости:
```bash
poetry install
poetry shell
```
## Запуск скрипта
### Положите csv файлы в папку `data`

Для создания отчета по одному csv файлу используйте команду:
```bash
poetry run python3 main.py --files data/ваш_файл.csv --report performance
```

Для создания отчета по всем csv файлам используйте команду:
```bash
poetry run python3 main.py --files data/*.csv --report performance
```

## Тестирование
Для тестирования используйте команду:
```bash
poetry run python3 -m pytest -v
```
