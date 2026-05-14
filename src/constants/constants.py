from src.config.settings import (
    RAW_DATA_PATH,
    PROCESSED_DATA_PATH,
    REPORTS_PATH
)

# Base scraping URL
BASE_URL = "https://www.scrapethissite.com/pages/forms/"

# HTML parser
HTML_PARSER = "lxml"

# Request timeout
REQUEST_TIMEOUT = 10

# Log file
LOG_FILE_PATH = "logs/pipeline.log"

# CSS selectors
TEAM_ROW_SELECTOR = "tr.team"

PAGINATION_SELECTOR = "ul.pagination li a"

# Default output filenames
DEFAULT_CSV_FILENAME = "teams.csv"

DEFAULT_PARQUET_FILENAME = "teams.parquet"