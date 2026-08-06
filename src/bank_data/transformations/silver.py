from __future__ import annotations

import pandas as pd

from bank_data.quality.transaction_rules import add_quality_columns


def build_silver(
    df: pd.DataFrame,
    allowed_currencies: set[str],
    allowed_statuses: set[str],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    enriched = add_quality_columns(df, allowed_currencies, allowed_statuses)

    valid = (
        enriched[enriched["is_valid"]]
        .drop_duplicates(subset=["transaction_id"], keep="last")
        .copy()
    )

    rejected = enriched[~enriched["is_valid"]].copy()

    return valid, rejected
