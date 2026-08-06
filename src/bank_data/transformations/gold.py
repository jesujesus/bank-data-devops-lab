from __future__ import annotations

import pandas as pd


def daily_summary(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame(
            columns=["transaction_date", "currency", "transaction_count", "total_amount"]
        )

    result = (
        df.groupby(["transaction_date", "currency"], as_index=False)
        .agg(
            transaction_count=("transaction_id", "count"),
            total_amount=("amount", "sum"),
        )
        .sort_values(["transaction_date", "currency"])
        .reset_index(drop=True)
    )

    return result
