import logging
import os

from src.constants.constants import LOG_FILE_PATH


def setup_logger():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger()