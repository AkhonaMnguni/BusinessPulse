from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class ValidationResult:
    valid: list[dict]
    invalid: list[dict]


def validate_transactions(rows: list[dict]) -> ValidationResult:
    valid, invalid = [], []
    for row in rows:
        amount = row.get("amount", 0)
        quantity = row.get("quantity", 0)
        transaction_date = row.get("transaction_date")
        if amount < 0 or quantity <= 0 or (transaction_date and transaction_date > date.today()):
            invalid.append(row)
        else:
            valid.append(row)
    return ValidationResult(valid, invalid)
