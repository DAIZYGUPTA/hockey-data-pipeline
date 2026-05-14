import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from src.config.config import REQUEST_TIMEOUT, MAX_RETRIES
from src.utils.logger import setup_logger
from src.config.settings import USER_AGENT

logger = setup_logger()


def create_session():
    session = requests.Session()

    retries = Retry(
        total=MAX_RETRIES,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504]
    )

    adapter = HTTPAdapter(max_retries=retries)

    session.mount("http://", adapter)
    session.mount("https://", adapter)

    return session


def fetch_page(session, url, params=None):
    try:
        response = session.get(
            url,
            headers = {
    "User-Agent": USER_AGENT 
},
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        logger.info(f"Successfully fetched page: {response.url}")

        return response.text

    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        return None