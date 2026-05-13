def safe_int(tag):
    try:
        return int(tag.text.strip()) if tag and tag.text.strip() else None
    except ValueError:
        return None


def safe_float(tag):
    try:
        return float(tag.text.strip()) if tag and tag.text.strip() else None
    except ValueError:
        return None


def safe_text(tag):
    return tag.text.strip() if tag else None