from reports.average_rating_report import generate_average_rating_report

def generate_report(report_type, data):
    """Генерация отчетов"""
    if report_type == "average-rating":
        return generate_average_rating_report(data)
    # При необходимости можно добавить другие типы отчетов
    else:
        raise ValueError(f"Неверный тип отчета")