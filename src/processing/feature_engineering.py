import pandas as pd

from src.utils.logger import setup_logger

logger = setup_logger()


def add_total_games(df):

    logger.info("Adding total games feature")

    df["Total Games"] = df["Wins"] + df["Losses"]

    return df


def add_goal_difference_ratio(df):

    logger.info("Adding goal difference ratio feature")

    df["Goal Difference Ratio"] = (
        df["+/-"] / df["Total Games"]
    )

    return df


def add_winning_category(df):

    logger.info("Adding winning category feature")

    df["Team Category"] = pd.cut(
        df["Win %"],
        bins=[0, 0.5, 0.75, 1],
        labels=["Weak", "Average", "Elite"]
    )

    return df


def add_goals_per_game(df):

    logger.info("Adding goals per game feature")

    df["Goals Per Game"] = (
        df["Goals For"] / df["Total Games"]
    )

    return df


def engineer_features(df):

    logger.info("Starting feature engineering")

    df = add_total_games(df)

    df = add_goal_difference_ratio(df)

    df = add_winning_category(df)

    df = add_goals_per_game(df)

    logger.info("Feature engineering completed")

    return df