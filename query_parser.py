def parse_query(query: str) -> dict:
    query = query.lower()
    price_limit = 100000
    keywords = []

    if "battery" in query:
        keywords.append("battery")
    if "remote work" in query or "remote" in query:
        keywords.append("remote")
    if "lightweight" in query:
        keywords.append("lightweight")

    return {
        "category": "laptop",
        "price": price_limit,
        "features": keywords
    }