# def inventory_variance(expected: float, actual: float) -> float:
#     return actual - expected


class InventoryAnalyzer:
    """
    Detects differences between expected and actual inventory.

    Formula:

        Expected Closing Inventory =
            Opening Inventory
            + Purchases
            - Sales

    Inventory Variance:

        Expected Inventory - Actual Inventory
    """

    def expected_inventory(
        self,
        opening_inventory,
        purchases,
        sales,
    ):
        return (
            opening_inventory
            + purchases
            - sales
        )

    def variance(
        self,
        expected_inventory,
        actual_inventory,
    ):
        return (
            expected_inventory
            - actual_inventory
        )

    def variance_percentage(
        self,
        expected_inventory,
        actual_inventory,
    ):
        if expected_inventory == 0:
            return 0.0

        return (
            abs(
                expected_inventory
                - actual_inventory
            )
            / expected_inventory
        ) * 100
 