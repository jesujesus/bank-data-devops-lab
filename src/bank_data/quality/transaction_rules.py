from __future__ import annotations

import pandas as pd


REQUIRED_COLUMNS = {
    "transaction_id",
    "customer_id",
    "account_id",
    "transaction_date",
    "transaction_type",
    "amount",
    "currency",
    "status",
}


def validate_schema(df: pd.DataFrame) -> None:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas obligatorias: {sorted(missing)}")


def add_quality_columns(
    df: pd.DataFrame,
    allowed_currencies: set[str],
    allowed_statuses: set[str],
) -> pd.DataFrame:
    validate_schema(df)

    result = df.copy()
    result["amount"] = pd.to_numeric(result["amount"], errors="coerce")

    result["is_valid"] = (
        result["transaction_id"].notna()
        & result["customer_id"].notna()
        & result["account_id"].notna()
        & result["amount"].gt(0)
        & result["currency"].isin(allowed_currencies)
        & result["status"].isin(allowed_statuses)
    )

    result["quality_error"] = ""

    result.loc[result["transaction_id"].isna(), "quality_error"] += "missing_transaction_id;"
    result.loc[result["amount"].isna(), "quality_error"] += "invalid_amount;"
    result.loc[result["amount"].le(0), "quality_error"] += "amount_not_positive;"
    result.loc[~result["currency"].isin(allowed_currencies), "quality_error"] += "invalid_currency;"
    result.loc[~result["status"].isin(allowed_statuses), "quality_error"] += "invalid_status;"

    return result
