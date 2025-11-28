from collections import defaultdict
from typing import List, Protocol

from .models import EmployeeData, ReportData


class ReportGenerator(Protocol):
    def generate(self, data: List[EmployeeData]) -> ReportData: ...


class AveragePerformanceReport:
    """Класс для отчета средней эффективности сотрудников"""
    def generate(self, data: List[EmployeeData]) -> ReportData:
        position_performance = defaultdict(list)

        for row in data:
            position = row.get("position")
            performance = row.get("performance")
            if not position or not performance:
                continue

            try:
                performance = float(performance)
                position_performance[position].append(performance)
            except ValueError:
                continue

        result: ReportData = []
        for position, performance in position_performance.items():
            avg_performance = sum(performance) / len(performance)
            result.append({
                "position": position,
                "performance": avg_performance
            })
        result.sort(key=lambda x: x["performance"], reverse=True)
        return result
