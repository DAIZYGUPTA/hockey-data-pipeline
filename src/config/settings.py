import os

from dotenv import load_dotenv

load_dotenv()

SCRAPER_DELAY = int(
    os.getenv("SCRAPER_DELAY", 1)
)

USER_AGENT = os.getenv(
    "USER_AGENT",
    "Mozilla/5.0"
)

RAW_DATA_PATH = os.getenv(
    "RAW_DATA_PATH",
    "data/raw"
)

PROCESSED_DATA_PATH = os.getenv(
    "PROCESSED_DATA_PATH",
    "data/processed"
)

REPORTS_PATH = os.getenv(
    "REPORTS_PATH",
    "data/reports"
)