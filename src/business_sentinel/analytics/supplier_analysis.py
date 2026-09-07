def supplier_average(rows: list[dict]) -> dict[str, float]:
    grouped: dict[str, list[float]] = {}
    for row in rows:
        grouped.setdefault(row.get("supplier_id", "unknown"), []).append(float(row.get("amount", 0)))
    return {supplier: sum(values) / len(values) for supplier, values in grouped.items()}
