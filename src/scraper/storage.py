import os
import pandas as pd

from src.constants.constants import (
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH
)


def create_directories():
    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)


def save_raw_html(html, filename):
    create_directories()

    filepath = os.path.join(RAW_DATA_PATH, filename)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(html)


def create_dataframe(data):
    return pd.DataFrame(data)


def save_csv(df, filename):
    create_directories()

    filepath = os.path.join(PROCESSED_DATA_PATH, filename)

    df.to_csv(filepath, index=False)


def save_parquet(df, filename):
    create_directories()

    filepath = os.path.join(PROCESSED_DATA_PATH, filename)

    df.to_parquet(filepath, index=False)