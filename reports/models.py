from typing import List, TypedDict


class EmployeeData(TypedDict):
    name: str
    position: str
    completed_tasks: str
    performance: str
    skills: str
    team: str
    experience_years: str


class PositionPerformance(TypedDict):
    position: str
    performance: float


ReportData = List[PositionPerformance]
