from business_sentinel.risk.scoring import risk_score


def test_score_is_bounded():
    assert risk_score([80, 120]) == 100
    assert risk_score([]) == 0
