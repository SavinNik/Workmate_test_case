import pytest
from reports import generate_report, generate_average_rating_report


def test_generate_report_with_invalid_type():
    """Тестирование генерации отчета с неверным типом отчета"""
    with pytest.raises(ValueError, match="Неверный тип отчета"):
        generate_report("invalid", [])

def test_generate_average_rating_report_basic():
    """Тестирование генерации отчета среднего рейтинга"""
    test_data = [
        {"brand": "Apple", "rating": "4.5"},
        {"brand": "Samsung", "rating": "4.2"},
        {"brand": "Xiaomi", "rating": "4.0"},
        {"brand": "Apple", "rating": "4.8"},
        {"brand": "Samsung", "rating": "4.6"}
    ]

    result = generate_average_rating_report(test_data)

    assert len(result) == 3
    assert result[0]["brand"] == "Apple"
    assert result[0]["rating"] == 4.65
    assert result[1]["brand"] == "Samsung"
    assert result[1]["rating"] == 4.40
    assert result[2]["brand"] == "Xiaomi"
    assert result[2]["rating"] == 4.00

def test_generate_average_rating_report_empty_data():
    """Тестирование генерации отчета среднего рейтинга с пустым списком данных"""
    result = generate_average_rating_report([])
    assert result == []

def test_generate_average_rating_report_missing_fields():
    """Тестирование генерации отчета среднего рейтинга с отсутствующими полями"""
    test_data = [
        {"brand": "Apple"},
        {"rating": "4.5"},
        {},
        {"brand": "Samsung", "rating": "invalid"},
        {"brand": "Xiaomi", "rating": "3.5"}
    ]

    result = generate_average_rating_report(test_data)
    assert len(result) == 1
    assert result[0]["brand"] == "Xiaomi"
    assert result[0]["rating"] == 3.5



