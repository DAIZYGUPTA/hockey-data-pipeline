from bs4 import BeautifulSoup

from src.utils.helpers import (
    safe_int,
    safe_float,
    safe_text
)


def create_soup(html):
    return BeautifulSoup(html, "lxml")


def parse_team_row(row):
    return {
        "Name": safe_text(row.select_one("td.name")),
        "Year": safe_int(row.select_one("td.year")),
        "Wins": safe_int(row.select_one("td.wins")),
        "Losses": safe_int(row.select_one("td.losses")),
        "Win %": safe_float(row.select_one("td.pct")),
        "Goals For": safe_int(row.select_one("td.gf")),
        "Goals Against": safe_int(row.select_one("td.ga")),
        "+/-": safe_int(row.select_one("td.diff"))
    }


def parse_html(html):
    soup = create_soup(html)

    rows = soup.select("tr.team")

    data = []

    for row in rows:
        parsed_row = parse_team_row(row)
        data.append(parsed_row)

    return data