def explain(indicators: dict[str, float], threshold: float = 60) -> list[str]:
    return [
        f"{name} contributed {value:.0f} points"
        for name, value in indicators.items()
        if value >= threshold
    ]
