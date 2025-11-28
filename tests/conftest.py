import pytest
from typing import List

from reports.models import EmployeeData


@pytest.fixture
def mix_data() -> List[EmployeeData]:
    return [
        {
            "name": "Ivan Ivanov",
            "position": "Backend Developer",
            "completed_tasks": "45",
            "performance": "4.8",
            "skills": "Python, Django, ",
            "team": "API team",
            "experience_years": "5"
        },
        {
            "name": "Petr Petrov",
            "position": "Frontend Developer",
            "completed_tasks": "38",
            "performance": "4.6",
            "skills": "React, TypeScript",
            "team": "Web team",
            "experience_years": "4"
        },
        {
            "name": "Anna Lee",
            "position": "Backend Developer",
            "completed_tasks": "40",
            "performance": "4.6",
            "skills": "Python, FastAPI",
            "team": "API team",
            "experience_years": "3"
        },
        {
            "name": "Vasiliy Vasiliev",
            "position": "DevOps",
            "completed_tasks": "52",
            "performance": "4.9",
            "skills": "AWS, K8s",
            "team": "Infra team",
            "experience_years": "6"
        }
    ]


@pytest.fixture
def invalid_data() -> List[EmployeeData]:
    return [
        {
            "name": "Ivan Ivanov",
            "position": "Backend Developer",
            "completed_tasks": "45",
            "performance": "4.8",
            "skills": "Python, Django, ",
            "team": "API team",
            "experience_years": "5"
        },
        {
            "name": "X",
            "position": "Backend Developer",
            "completed_tasks": "1",
            "performance": "invalid",
            "skills": "A",
            "team": "B",
            "experience_years": "2"
        },
        {
            "name": "Y",
            "position": "",
            "completed_tasks": "1",
            "performance": "4.5",
            "skills": "Z",
            "team": "Q",
            "experience_years": "1"
        }
    ]
