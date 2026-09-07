from datetime import date

from business_sentinel.etl.transform import normalize_transactions


def test_normalize_transactions_casts_types():
    result = normalize_transactions([{"amount": "12.5", "quantity": "2", "transaction_date": "2026-01-01"}])
    assert result[0]["amount"] == 12.5
    assert result[0]["quantity"] == 2
    assert result[0]["transaction_date"] == date(2026, 1, 1)
