# from collections import defaultdict


# def spending_by_supplier(rows: list[dict]) -> dict[str, float]:
#     totals = defaultdict(float)
#     for row in rows:
#         totals[row.get("supplier_id", "unknown")] += float(row.get("amount", 0))
#     return dict(totals)

import pandas as pd

from .anomaly_detection import (
    percentage_change,
    z_score,
)


class ExpenseAnalyzer:
    """
    Performs historical expenditure analysis.

    Methods
    -------
    monthly_spend()
        Aggregates expenditure by month.

    growth_rate()
        Calculates expenditure growth.

    detect_spike()
        Detects abnormal expenditure increases.
    """

    def monthly_spend(
        self,
        invoices,
        date_column="invoice_date",
        amount_column="total_amount",
    ):
        df = invoices.copy()

        df[date_column] = pd.to_datetime(
            df[date_column],
            errors="coerce",
        )

        df["month"] = df[date_column].dt.to_period("M")

        return (
            df.groupby("month")[amount_column]
            .sum()
            .reset_index(name="monthly_spend")
        )

    def growth_rate(self, previous, current):
        return percentage_change(
            previous,
            current,
        )

    def detect_spike(
        self,
        historical_values,
        current_value,
        threshold=2.0,
    ):
        score = z_score(
            current_value,
            historical_values.mean(),
            historical_values.std(),
        )

        return {
            "z_score": score,
            "is_anomaly": abs(score) >= threshold,
        }
