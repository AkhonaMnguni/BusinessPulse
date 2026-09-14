# def supplier_average(rows: list[dict]) -> dict[str, float]:
#     grouped: dict[str, list[float]] = {}
#     for row in rows:
#         grouped.setdefault(row.get("supplier_id", "unknown"), []).append(float(row.get("amount", 0)))
#     return {supplier: sum(values) / len(values) for supplier, values in grouped.items()}


import pandas as pd

from .anomaly_detection import percentage_change


class SupplierAnalyzer:
    """
    Analyses supplier behaviour.

    Methods
    -------
    supplier_spend()
        Calculates total supplier expenditure.

    supplier_growth()
        Calculates supplier spending growth.

    price_variance()
        Compares supplier prices against peer prices.

    branch_concentration()
        Measures supplier dependence on one branch.
    """

    def supplier_spend(self, invoices):
        return (
            invoices
            .groupby("supplier_id")["total_amount"]
            .sum()
            .reset_index(name="total_spend")
        )

    def supplier_growth(
        self,
        previous_spend,
        current_spend,
    ):
        return percentage_change(
            previous_spend,
            current_spend,
        )

    def price_variance(
        self,
        current_price,
        peer_median,
    ):
        if peer_median == 0:
            return 0.0

        return (
            (current_price - peer_median)
            / peer_median
        ) * 100

    def branch_concentration(
        self,
        supplier_invoices,
    ):
        total = supplier_invoices["total_amount"].sum()

        if total == 0:
            return 0.0

        branch_totals = (
            supplier_invoices
            .groupby("branch_id")["total_amount"]
            .sum()
        )

        largest_branch = branch_totals.max()

        return (
            largest_branch / total
        ) * 100
