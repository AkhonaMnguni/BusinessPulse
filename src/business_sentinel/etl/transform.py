from datetime import date


def normalize_transactions(rows: list[dict]) -> list[dict]:
    normalized = []
    for row in rows:
        item = dict(row)
        item["amount"] = float(item.get("amount", 0))
        item["quantity"] = int(item.get("quantity", 0))
        if item.get("transaction_date"):
            item["transaction_date"] = date.fromisoformat(item["transaction_date"])
        normalized.append(item)
    return normalized
