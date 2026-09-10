# def flag_outliers(values: list[float], multiplier: float = 2.0) -> list[int]:
#     if not values:
#         return []
#     average = sum(values) / len(values)
#     return [index for index, value in enumerate(values) if value > average * multiplier]




import numpy as np
import pandas as pd


def percentage_change(previous, current):
    """
    Calculates percentage change.

    Formula:

        Percentage Change =
            ((Current - Previous) / Previous) × 100

    Example:

        Previous = 3,000,000
        Current  = 9,000,000

        ((9,000,000 - 3,000,000) / 3,000,000) × 100
        = 200%

    Returns 0 when previous is zero and current is also zero.
    Returns infinity when previous is zero but current is non-zero.
    """

    if previous == 0:
        if current == 0:
            return 0.0

        return float("inf")

    return ((current - previous) / previous) * 100


def z_score(value, mean, std):
    """
    Calculates a standardised Z-score.

    Formula:

        Z = (X - μ) / σ

    Where:

        X  = observed value
        μ  = population mean
        σ  = standard deviation

    Interpretation:

        Z ≈ 0
            close to normal behaviour

        |Z| >= 2
            potentially unusual

        |Z| >= 3
            strongly unusual
    """

    if std == 0 or pd.isna(std):
        return 0.0

    return (value - mean) / std


def rolling_mean(series, window=3):
    """
    Calculates a rolling/moving average.

    Formula:

        MA_t =
        (X_t + X_t-1 + ... + X_t-(n-1)) / n

    Parameters
    ----------
    series:
        Time-ordered numerical observations.

    window:
        Number of observations used.
    """

    return series.rolling(
        window=window,
        min_periods=1,
    ).mean()


def median_variance(current, median):
    """
    Calculates percentage difference from a peer median.

    Formula:

        ((Current - Median) / Median) × 100
    """

    if median == 0:
        return 0.0

    return ((current - median) / median) * 100


class StatisticalAnomalyDetector:

    def expense_z_score(self, historical_values, current_value):
        values = np.asarray(
            historical_values,
            dtype=float,
        )

        mean = np.mean(values)
        std = np.std(values)

        return z_score(
            current_value,
            mean,
            std,
        )

    def price_variance(self, current_price, peer_prices):
        median = float(
            np.median(
                np.asarray(peer_prices, dtype=float)
            )
        )

        variance = median_variance(
            current_price,
            median,
        )

        return {
            "peer_median": median,
            "variance_percentage": variance,
        }
