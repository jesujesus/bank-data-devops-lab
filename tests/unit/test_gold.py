import pandas as pd

from bank_data.transformations.gold import daily_summary


def test_daily_summary_groups_amounts() -> None:
    df = pd.DataFrame(
        [
            {
                "transaction_id": "TX001",
                "transaction_date": "2026-08-01",
                "currency": "PEN",
                "amount": 100.0,
            },
            {
                "transaction_id": "TX002",
                "transaction_date": "2026-08-01",
                "currency": "PEN",
                "amount": 50.0,
            },
        ]
    )

    result = daily_summary(df)

    assert result.loc[0, "transaction_count"] == 2
    assert result.loc[0, "total_amount"] == 150.0
