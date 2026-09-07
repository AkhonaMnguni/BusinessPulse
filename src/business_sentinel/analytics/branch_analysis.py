from business_sentinel.analytics.expense_analysis import spending_by_supplier


def spending_by_branch(rows: list[dict]) -> dict[str, float]:
    return {branch: total for branch, total in spending_by_supplier([{**row, "supplier_id": row.get("branch_id", "unknown")} for row in rows]).items()}
