from __future__ import annotations

import argparse
import logging
from pathlib import Path

import pandas as pd

from bank_data.common.config import load_config
from bank_data.transformations.gold import daily_summary
from bank_data.transformations.silver import build_silver


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def run_pipeline(
    input_path: Path,
    output_path: Path,
    config_path: Path,
) -> None:
    logger.info("Iniciando procesamiento del archivo: %s", input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"No existe el archivo de entrada: {input_path}")

    config = load_config(config_path)

    allowed_currencies = set(config["currency_allowed"])
    allowed_statuses = set(config["status_allowed"])

    source_df = pd.read_csv(input_path)

    logger.info("Registros recibidos: %s", len(source_df))

    valid_df, rejected_df = build_silver(
        source_df,
        allowed_currencies=allowed_currencies,
        allowed_statuses=allowed_statuses,
    )

    gold_df = daily_summary(valid_df)

    silver_path = output_path / "silver"
    rejected_path = output_path / "rejected"
    gold_path = output_path / "gold"

    silver_path.mkdir(parents=True, exist_ok=True)
    rejected_path.mkdir(parents=True, exist_ok=True)
    gold_path.mkdir(parents=True, exist_ok=True)

    valid_df.to_csv(silver_path / "transactions.csv", index=False)
    rejected_df.to_csv(rejected_path / "transactions.csv", index=False)
    gold_df.to_csv(gold_path / "daily_summary.csv", index=False)

    logger.info("Registros válidos: %s", len(valid_df))
    logger.info("Registros rechazados: %s", len(rejected_df))
    logger.info("Pipeline finalizado correctamente")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Procesa transacciones bancarias ficticias."
    )

    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Ruta del archivo CSV de entrada.",
    )

    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Directorio de salida.",
    )

    parser.add_argument(
        "--config",
        default=Path("config/dev.json"),
        type=Path,
        help="Archivo de configuración.",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    run_pipeline(
        input_path=args.input,
        output_path=args.output,
        config_path=args.config,
    )


if __name__ == "__main__":
    main()