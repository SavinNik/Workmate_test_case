from typing import List

from reports.models import EmployeeData, ReportData

from .average_performance_report import (AveragePerformanceReport,
                                         ReportGenerator)


def generate_report(
        report_type: str,
        data: List[EmployeeData]
) -> ReportData:
    """Генерация отчетов"""
    if report_type == "performance":
        gen: ReportGenerator = AveragePerformanceReport()
        return gen.generate(data)
    # Тут можно добавлять другие типы отчетов
    else:
        raise ValueError("Неверный тип отчета")
