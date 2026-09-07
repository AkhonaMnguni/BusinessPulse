def risk_score(indicators: list[float]) -> int:
    """Return a bounded explainable score from 0-100."""
    if not indicators:
        return 0
    return max(0, min(100, round(sum(indicators) / len(indicators))))
