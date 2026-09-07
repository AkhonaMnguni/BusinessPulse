from business_sentinel.analytics.supplier_analysis import supplier_average


def summarize(rows: list[dict]) -> dict[str, float]:
    return supplier_average(rows)
