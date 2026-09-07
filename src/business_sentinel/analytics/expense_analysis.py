from collections import defaultdict


def spending_by_supplier(rows: list[dict]) -> dict[str, float]:
    totals = defaultdict(float)
    for row in rows:
        totals[row.get("supplier_id", "unknown")] += float(row.get("amount", 0))
    return dict(totals)
