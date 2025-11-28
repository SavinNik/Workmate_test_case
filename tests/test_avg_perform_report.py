import pytest
from reports.generate_reports import generate_report


def test_generate_avg_perform_report_empty():
    assert generate_report("performance", []) == []


def test_generate_avg_perform_report_multiple_positions(mix_data):
    result = generate_report("performance", mix_data)
    assert len(result) == 3
    assert result[0]["position"] == "DevOps"
    assert result[1]["position"] == "Backend Developer"
    assert result[2]["position"] == "Frontend Developer"
    assert abs(result[0]["performance"] - 4.9) < 0.001
    assert abs(result[1]["performance"] - 4.7) < 0.001
    assert abs(result[2]["performance"] - 4.6) < 0.001


def test_generate_avg_perform_report_invalid_performance(invalid_data):
    result = generate_report("performance", invalid_data)
    assert len(result) == 1
    assert result[0]["position"] == "Backend Developer"
    assert abs(result[0]["performance"] - 4.8) < 0.001


def test_generate_report_unknown_type():
    with pytest.raises(ValueError, match="Неверный тип отчета"):
        generate_report("test", [])


@pytest.mark.parametrize("data, expected_pos, expected_perf", [
    ([{"name": "A", "position": "Backend", "completed_tasks": "1", "performance": "4.5", "skills": "X", "team": "Y", "experience_years": "1"}], "Backend", 4.5),
    ([{"name": "A", "position": "Backend", "completed_tasks": "1", "performance": "4.5", "skills": "X", "team": "Y", "experience_years": "1"},
      {"name": "B", "position": "Backend", "completed_tasks": "1", "performance": "4.7", "skills": "X", "team": "Y", "experience_years": "1"}], "Backend", 4.6),
])
def test_generate_avg_perform_report_parametrize(data, expected_pos, expected_perf):
    result = generate_report("performance", data)
    assert len(result) == 1
    assert result[0]["position"] == expected_pos
    assert abs(result[0]["performance"] - expected_perf) < 0.001
