import pandas as pd

from bank_data.transformations.silver import build_silver


def test_silver_separates_valid_and_rejected_rows() -> None:
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
                "amount": 20.0,
                "currency": "EUR",
                "status": "APPROVED",
            },
        ]
    )

    valid, rejected = build_silver(
        df,
        allowed_currencies={"PEN", "USD"},
        allowed_statuses={"APPROVED", "REJECTED", "PENDING"},
    )

    assert len(valid) == 1
    assert len(rejected) == 1
