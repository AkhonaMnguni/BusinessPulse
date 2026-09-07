def flag_outliers(values: list[float], multiplier: float = 2.0) -> list[int]:
    if not values:
        return []
    average = sum(values) / len(values)
    return [index for index, value in enumerate(values) if value > average * multiplier]
