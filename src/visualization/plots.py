import os
import matplotlib.pyplot as plt

from src.utils.logger import setup_logger

logger = setup_logger()


def create_reports_directory():

    os.makedirs("data/reports", exist_ok=True)


def plot_yearly_win_trends(yearly_trends):

    logger.info("Generating yearly win trends plot")

    create_reports_directory()

    plt.figure(figsize=(10, 6))

    yearly_trends.plot()

    plt.title("Average Wins Per Year")

    plt.xlabel("Year")

    plt.ylabel("Average Wins")

    plt.grid(True)

    filepath = "data/reports/yearly_win_trends.png"

    plt.savefig(filepath)

    plt.close()


def plot_top_teams(top_teams):

    logger.info("Generating top teams plot")

    create_reports_directory()

    plt.figure(figsize=(12, 6))

    top_teams.plot(kind="bar")

    plt.title("Top Teams by Average Wins")

    plt.xlabel("Team")

    plt.ylabel("Average Wins")

    plt.xticks(rotation=45)

    filepath = "data/reports/top_teams.png"

    plt.savefig(filepath)

    plt.close()


def plot_correlation_matrix(correlation_matrix):

    logger.info("Generating correlation matrix plot")

    create_reports_directory()

    plt.figure(figsize=(10, 8))

    plt.imshow(correlation_matrix)

    plt.colorbar()

    plt.xticks(
        range(len(correlation_matrix.columns)),
        correlation_matrix.columns,
        rotation=90
    )

    plt.yticks(
        range(len(correlation_matrix.columns)),
        correlation_matrix.columns
    )

    plt.title("Feature Correlation Matrix")

    filepath = "data/reports/correlation_matrix.png"

    plt.savefig(filepath)

    plt.close()


def generate_visual_reports(eda_results):

    logger.info("Generating visual reports")

    plot_yearly_win_trends(
        eda_results["yearly_trends"]
    )

    plot_top_teams(
        eda_results["top_teams"]
    )

    plot_correlation_matrix(
        eda_results["correlations"]
    )

    logger.info("Visual reports generated")