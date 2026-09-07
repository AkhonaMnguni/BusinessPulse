from business_sentinel.etl.validate import validate_transactions


def test_validation_quarantines_negative_amounts():
    result = validate_transactions([{"amount": -1, "quantity": 1}])
    assert result.valid == []
    assert len(result.invalid) == 1
