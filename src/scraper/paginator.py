from src.scraper.parser import create_soup


def get_total_pages(html):
    soup = create_soup(html)

    pages = soup.select("ul.pagination li a")

    page_numbers = []

    for page in pages:
        text = page.text.strip()

        if text.isdigit():
            page_numbers.append(int(text))

    return max(page_numbers, default=1)


def build_page_params(page_num, query=None):
    params = {
        "page_num": page_num
    }

    if query:
        params["q"] = query

    return params