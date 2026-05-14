import time

from src.constants.constants import BASE_URL
from src.config.config import SCRAPER_DELAY

from src.utils.logger import setup_logger

from src.scraper.fetcher import (
    create_session,
    fetch_page
)

from src.scraper.parser import parse_html

from src.scraper.paginator import (
    get_total_pages,
    build_page_params
)

from src.scraper.storage import (
    save_raw_html,
    create_dataframe,
    save_csv,
    save_parquet
)

from src.processing.validation import validate_dataset

from src.processing.cleaning import clean_dataset

from src.processing.feature_engineering import engineer_features

from src.analysis.eda import perform_eda

from src.visualization.plots import generate_visual_reports


logger = setup_logger()


def run_pipeline(query=None):

    logger.info("Pipeline started")

    # Create HTTP session
    session = create_session()

    # Fetch first page
    first_page_params = build_page_params(
        page_num=1,
        query=query
    )

    first_page_html = fetch_page(
        session=session,
        url=BASE_URL,
        params=first_page_params
    )

    # Handle failed request
    if not first_page_html:
        logger.error("Failed to fetch first page")
        return

    # Detect total pages
    total_pages = get_total_pages(first_page_html)

    logger.info(f"Total pages detected: {total_pages}")

    # Master dataset list
    all_data = []

    # Pagination loop
    for page_num in range(1, total_pages + 1):

        logger.info(f"Processing page {page_num}")

        # Build params
        params = build_page_params(
            page_num=page_num,
            query=query
        )

        # Fetch page
        html = fetch_page(
            session=session,
            url=BASE_URL,
            params=params
        )

        # Skip failed pages
        if not html:
            logger.warning(f"Skipping page {page_num}")
            continue

        # Save raw HTML
        filename = f"page_{page_num}.html"

        if query:
            filename = f"{query}_page_{page_num}.html"

        save_raw_html(html, filename)

        # Parse page data
        parsed_data = parse_html(html)

        # Extend master dataset
        all_data.extend(parsed_data)

        logger.info(
            f"Collected {len(parsed_data)} records from page {page_num}"
        )

        # Respectful scraping delay
        time.sleep(SCRAPER_DELAY)

    # Create DataFrame
    df = create_dataframe(all_data)

    logger.info(f"Initial dataset shape: {df.shape}")

    # =========================
    # Validation
    # =========================

    validation_results = validate_dataset(df)

    logger.info("Validation Results:")

    logger.info(
        f"Duplicate Rows: "
        f"{validation_results['duplicate_rows']}"
    )

    # =========================
    # Cleaning
    # =========================

    df = clean_dataset(df)

    logger.info(f"Cleaned dataset shape: {df.shape}")

    # =========================
    # Feature Engineering
    # =========================

    df = engineer_features(df)

    logger.info("Feature engineering completed")

    # =========================
    # Exploratory Data Analysis
    # =========================

    eda_results = perform_eda(df)

    logger.info("EDA completed")

    print("\nDataset Overview:")
    print(eda_results["overview"])

    print("\nTop Teams:")
    print(eda_results["top_teams"])

    # =========================
    # Visualization
    # =========================

    generate_visual_reports(eda_results)

    logger.info("Visualization reports generated")

    # =========================
    # Save Final Processed Data
    # =========================

    csv_filename = "teams.csv"
    parquet_filename = "teams.parquet"

    if query:
        csv_filename = f"{query}_teams.csv"
        parquet_filename = f"{query}_teams.parquet"

    save_csv(df, csv_filename)

    save_parquet(df, parquet_filename)

    logger.info("Processed datasets saved")

    logger.info(f"Final records collected: {len(df)}")

    logger.info("Pipeline completed successfully")

    return df


if __name__ == "__main__":

    # Example:
    # query=None → scrape all teams
    # query="Boston" → filtered scraping

    df = run_pipeline(query=None)

    print("\nFinal Dataset Preview:\n")

    print(df.head())