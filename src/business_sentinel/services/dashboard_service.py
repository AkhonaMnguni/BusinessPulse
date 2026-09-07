def dashboard_summary(cases: list[dict]) -> dict[str, int]:
    return {
        "total_cases": len(cases),
        "open_cases": sum(case.get("status") == "open" for case in cases),
        "high_risk_cases": sum(case.get("score", 0) >= 80 for case in cases),
    }
