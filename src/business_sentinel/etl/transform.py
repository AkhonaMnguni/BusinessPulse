# from datetime import date


# def normalize_transactions(rows: list[dict]) -> list[dict]:
#     normalized = []
#     for row in rows:
#         item = dict(row)
#         item["amount"] = float(item.get("amount", 0))
#         item["quantity"] = int(item.get("quantity", 0))
#         if item.get("transaction_date"):
#             item["transaction_date"] = date.fromisoformat(item["transaction_date"])
#         normalized.append(item)
#     return normalized




import pandas as pd
import numpy as np


class DataTransformer:
    """
    Cleans and standardises raw business data.

    Methods
    -------
    standardize_columns(df)
        Converts column names to snake_case.

    clean_strings(df)
        Removes unnecessary whitespace.

    convert_dates(df, columns)
        Converts columns to datetime.

    convert_numeric(df, columns)
        Converts financial/quantity fields to numeric.

    standardize_currency(df)
        Standardises currency values.

    remove_exact_duplicates(df)
        Removes identical records.
    """

    @staticmethod
    def standardize_columns(df):
        result = df.copy()

        result.columns = (
            result.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_", regex=False)
            .str.replace("-", "_", regex=False)
        )

        return result

    @staticmethod
    def clean_strings(df):
        result = df.copy()

        for column in result.select_dtypes(include=["object"]).columns:
            result[column] = result[column].apply(
                lambda value: value.strip()
                if isinstance(value, str)
                else value
            )

        return result

    @staticmethod
    def convert_dates(df, columns):
        result = df.copy()

        for column in columns:
            if column in result.columns:
                result[column] = pd.to_datetime(
                    result[column],
                    errors="coerce",
                )

        return result

    @staticmethod
    def convert_numeric(df, columns):
        result = df.copy()

        for column in columns:
            if column in result.columns:
                result[column] = pd.to_numeric(
                    result[column],
                    errors="coerce",
                )

        return result

    @staticmethod
    def standardize_currency(df):
        result = df.copy()

        if "currency" in result.columns:
            result["currency"] = (
                result["currency"]
                .astype(str)
                .str.upper()
                .str.strip()
            )

        return result

    @staticmethod
    def remove_exact_duplicates(df):
        return df.drop_duplicates().reset_index(drop=True)

    def transform(self, df):
        df = self.standardize_columns(df)
        df = self.clean_strings(df)

        df = self.convert_dates(
            df,
            [
                "invoice_date",
                "order_date",
                "sale_date",
                "transaction_date",
                "payment_date",
                "approved_at",
                "created_at",
            ],
        )

        df = self.convert_numeric(
            df,
            [
                "amount",
                "total_amount",
                "unit_price",
                "quantity",
                "revenue",
            ],
        )

        df = self.standardize_currency(df)
        df = self.remove_exact_duplicates(df)

        return df