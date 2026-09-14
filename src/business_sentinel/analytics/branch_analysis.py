# from business_sentinel.analytics.expense_analysis import spending_by_supplier


# def spending_by_branch(rows: list[dict]) -> dict[str, float]:
#     return {branch: total for branch, total in spending_by_supplier([{**row, "supplier_id": row.get("branch_id", "unknown")} for row in rows]).items()}


class BranchAnalyzer:
    """
    Performs branch-level business analysis.
    """

    def branch_spend(self, invoices):
        return (
            invoices
            .groupby("branch_id")["total_amount"]
            .sum()
            .reset_index(name="total_spend")
        )

    def branch_sales(self, sales):
        return (
            sales
            .groupby("branch_id")["revenue"]
            .sum()
            .reset_index(name="total_revenue")
        )

    def expense_to_sales_ratio(
        self,
        expenditure,
        sales,
    ):
        """
        Formula:

            Expense-to-Sales Ratio =
                Total Expenses / Total Sales × 100
        """

        if sales == 0:
            return 0.0

        return (
            expenditure / sales
        ) * 100
