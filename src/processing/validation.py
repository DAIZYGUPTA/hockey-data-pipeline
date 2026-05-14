import pandas as pd

from src.utils.logger import setup_logger

logger = setup_logger()


def check_missing_values(df):
    missing = df.isnull().sum()

    logger.info("Checking missing values")

    return missing


def check_duplicates(df):
    duplicates = df.duplicated().sum()

    logger.info(f"Duplicate rows found: {duplicates}")

    return duplicates


def validate_win_percentage(df):
    invalid_rows = df[df["Win %"] > 1]

    logger.info(
        f"Invalid win percentage rows: {len(invalid_rows)}"
    )

    return invalid_rows


def validate_dataset(df):

    logger.info("Starting dataset validation")

    validation_results = {
        "missing_values": check_missing_values(df),
        "duplicate_rows": check_duplicates(df),
        "invalid_win_percentage": validate_win_percentage(df)
    }

    logger.info("Dataset validation completed")

    return validation_results