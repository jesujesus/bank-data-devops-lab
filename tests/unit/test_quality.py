import pandas as pd

from bank_data.quality.transaction_rules import add_quality_columns


def test_marks_valid_and_invalid_rows() -> None:
    df = pd.DataFrame(
        [
            {
                "transaction_id": "TX001",
                "customer_id": "C001",
                "account_id": "A001",
                "transaction_date": "2026-08-01",
                "transaction_type": "TRANSFER",
                "amount": 100.0,
                "currency": "PEN",
                "status": "APPROVED",
            },
            {
                "transaction_id": "TX002",
                "customer_id": "C002",
                "account_id": "A002",
                "transaction_date": "2026-08-01",
                "transaction_type": "PAYMENT",
                "amount": -10.0,
                "currency": "PEN",
                "status": "APPROVED",
            },
        ]
    )

    result = add_quality_columns(
        df,
        allowed_currencies={"PEN", "USD"},
        allowed_statuses={"APPROVED", "REJECTED", "PENDING"},
    )

    assert bool(result.loc[0, "is_valid"]) is True
    assert bool(result.loc[1, "is_valid"]) is False
    assert "amount_not_positive" in result.loc[1, "quality_error"]
