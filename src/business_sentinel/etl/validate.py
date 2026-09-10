# from dataclasses import dataclass
# from datetime import date


# @dataclass(frozen=True)
# class ValidationResult:
#     valid: list[dict]
#     invalid: list[dict]


# def validate_transactions(rows: list[dict]) -> ValidationResult:
#     valid, invalid = [], []
#     for row in rows:
#         amount = row.get("amount", 0)
#         quantity = row.get("quantity", 0)
#         transaction_date = row.get("transaction_date")
#         if amount < 0 or quantity <= 0 or (transaction_date and transaction_date > date.today()):
#             invalid.append(row)
#         else:
#             valid.append(row)
#     return ValidationResult(valid, invalid)



from dataclasses import dataclass, field
from datetime import datetime
from email import errors
from itertools import count
from unittest import result

import pandas as pd


@dataclass
class ValidationResult:
 valid: pd.DataFrame
 invalid: pd.DataFrame
 errors: dict = field(default_factory=dict)

 @property
 def total_records(self):
  return len(self.valid) + len(self.invalid)

 @property
 def valid_records(self):
    return len(self.valid)

 @property
 def invalid_records(self):
    return len(self.invalid)

 @property
 def quality_percentage(self):
    if self.total_records == 0:
        return 100.0

        return round(
            self.valid_records / self.total_records * 100,
            2,
 )


class DataValidator:
 """
 Performs business-data quality validation.

 Validation rules include:
 Missing identifiers
 Negative amounts
 Invalid quantities
 Future dates
 Invalid currencies
 Duplicate invoices

Invalid records are returned separately rather than discarded.
 """

 REQUIRED_COLUMNS = {
    "invoices": [
    "supplier_id",
    "invoice_number",
    "invoice_date",
    "total_amount",
    ],
    "sales": [
    "branch_id",
    "product_id",
    "sale_date",
    "quantity",
    "revenue",
    ],
    "inventory": [
    "branch_id",
    "product_id",
    "quantity",
    "transaction_date",
    ],
    }

def validate(self, df, dataset_name):
    result = df.copy()

    errors = {}

    required = self.REQUIRED_COLUMNS.get(
            dataset_name,
            [],
    )

    for column in required:
        if column not in result.columns:
            errors[f"missing_column_{column}"] = len(result)

        if "supplier_id" in result.columns:
            count = result["supplier_id"].isna().sum()
            if count:
                errors["missing_supplier_ids"] = int(count)

        if "branch_id" in result.columns:
            count = result["branch_id"].isna().sum()
            if count:
                errors["missing_branch_ids"] = int(count)

        if "total_amount" in result.columns:
            count = (result["total_amount"] < 0).sum()
            if count:
                errors["negative_amounts"] = int(count)

        if "quantity" in result.columns:
            count = (result["quantity"] <= 0).sum()
            if count:
                errors["invalid_quantities"] = int(count)

        date_columns = [
            "invoice_date",
            "sale_date",
            "transaction_date",
            "payment_date",
            "order_date",
            ]

    invalid_date_mask = pd.Series(
    False,
    index=result.index,
    )

    for column in date_columns:
            if column in result.columns:
                invalid_date_mask |= (
                result[column].isna()
                | (result[column] > pd.Timestamp.now())
                )

    if invalid_date_mask.any():
        errors["invalid_or_future_dates"] = int(
        invalid_date_mask.sum()
        )

    if "currency" in result.columns:
        invalid_currency = ~result["currency"].isin(
        ["ZAR", "R"]
        )

    if invalid_currency.any():
        errors["invalid_currencies"] = int(
        invalid_currency.sum()
    )

        duplicate_mask = pd.Series(
        False,
        index=result.index,
    )

    if {
    "supplier_id",
    "invoice_number",
    }.issubset(result.columns):
        duplicate_mask = result.duplicated(
        subset=[
    "supplier_id",
    "invoice_number",
    ],
    keep=False,
    )

    count = int(duplicate_mask.sum())

    if count:
        errors["duplicate_invoices"] = count

        invalid_mask = pd.Series(
        False,
        index=result.index,
    )

    if "supplier_id" in result.columns:
        invalid_mask |= result["supplier_id"].isna()

    if "branch_id" in result.columns:
        invalid_mask |= result["branch_id"].isna()

    if "total_amount" in result.columns:
        invalid_mask |= result["total_amount"] < 0

    if "quantity" in result.columns:
        invalid_mask |= result["quantity"] <= 0

        invalid_mask |= invalid_date_mask

        valid = result.loc[~invalid_mask].copy()
        invalid = result.loc[invalid_mask].copy()

    return ValidationResult(
    valid=valid,
    invalid=invalid,
    errors=errors,
    )