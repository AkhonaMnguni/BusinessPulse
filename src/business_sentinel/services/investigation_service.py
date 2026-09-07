def next_action(score: int) -> str:
    if score >= 80:
        return "priority_review"
    if score >= 60:
        return "review"
    return "monitor"
