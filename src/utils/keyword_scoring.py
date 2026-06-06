def score_text(html, keyword_groups):
    """
    keyword_groups = {
        "core": {"sale": 2, "offer": 2, ...},
        "airline": {"flash sale": 4, ...},
        "route": {"tampa": 5, "tpa": 5, ...}
    }
    """

    html = html.lower()
    total_score = 0
    hits = []

    for group_name, group_keywords in keyword_groups.items():
        for keyword, weight in group_keywords.items():
            if keyword in html:
                total_score += weight
                hits.append((keyword, weight))

    return total_score, hits
