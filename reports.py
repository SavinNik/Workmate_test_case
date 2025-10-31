from collections import defaultdict

def generate_average_rating_report(data):
    """Генерация отчета среднего рейтинга"""
    brand_ratings = defaultdict(list)

    for row in data:
        brand = row.get("brand")
        rating = row.get("rating")
        if not brand or not rating:
            continue

        try:
            rating = float(rating)
            brand_ratings[brand].append(rating)
        except ValueError:
            continue

    result = []
    for brand, ratings in brand_ratings.items():
        avg_rating = sum(ratings) / len(ratings)
        result.append({
            "brand": brand,
            "rating": avg_rating
        })
    result.sort(key=lambda x: x["rating"], reverse=True)

    return result

def generate_report(report_type, data):
    """Генерация отчетов"""
    if report_type == "average-rating":
        return generate_average_rating_report(data)
    # При необходимости можно добавить другие типы отчетов
    else:
        raise ValueError(f"Неверный тип отчета")