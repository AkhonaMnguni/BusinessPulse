from business_sentinel.analytics.anomaly_detection import flag_outliers


def test_flag_outliers():
    assert flag_outliers([10, 10, 10, 30]) == [3]
