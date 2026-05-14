import pandas as pd

from src.utils.logger import setup_logger

logger = setup_logger()


def remove_duplicates(df):

    initial_rows = len(df)

    df = df.drop_duplicates()

    removed_rows = initial_rows - len(df)

    logger.info(f"Removed {removed_rows} duplicate rows")

    return df


def handle_missing_values(df):

    logger.info("Handling missing values")

    df = df.dropna()

    return df


def standardize_text(df):

    logger.info("Standardizing text columns")

    df["Name"] = df["Name"].str.strip()

    return df


def standardize_dtypes(df):

    logger.info("Standardizing datatypes")

    integer_columns = [
        "Year",
        "Wins",
        "Losses",
        "Goals For",
        "Goals Against",
        "+/-"
    ]

    for column in integer_columns:
        df[column] = df[column].astype(int)

    df["Win %"] = df["Win %"].astype(float)

    return df


def clean_dataset(df):

    logger.info("Starting dataset cleaning")

    df = remove_duplicates(df)

    df = handle_missing_values(df)

    df = standardize_text(df)

    df = standardize_dtypes(df)

    logger.info("Dataset cleaning completed")

    return df