import pandas as pd

from src.utils.logger import setup_logger

logger = setup_logger()


def dataset_overview(df):

    logger.info("Generating dataset overview")

    overview = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns)
    }

    return overview


def generate_summary_statistics(df):

    logger.info("Generating summary statistics")

    return df.describe()


def top_teams_by_wins(df, top_n=10):

    logger.info("Finding top teams by wins")

    top_teams = (
        df.groupby("Name")["Wins"]
        .mean()
        .sort_values(ascending=False)
        .head(top_n)
    )

    return top_teams


def yearly_win_trends(df):

    logger.info("Analyzing yearly win trends")

    yearly_trends = (
        df.groupby("Year")["Wins"]
        .mean()
    )

    return yearly_trends


def correlation_analysis(df):

    logger.info("Generating correlation matrix")

    numeric_df = df.select_dtypes(include=["number"])

    return numeric_df.corr()


def perform_eda(df):

    logger.info("Starting exploratory data analysis")

    eda_results = {
        "overview": dataset_overview(df),
        "summary_statistics": generate_summary_statistics(df),
        "top_teams": top_teams_by_wins(df),
        "yearly_trends": yearly_win_trends(df),
        "correlations": correlation_analysis(df)
    }

    logger.info("EDA completed")

    return eda_results