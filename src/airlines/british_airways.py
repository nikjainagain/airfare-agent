import urllib.request
from utils.keyword_scoring import score_text

def check_sales():
    url = "https://www.britishairways.com/en-in/offers/flights"

    keyword_groups = {
        "core": {
            "sale": 2, "offer": 2, "discount": 2, "deal": 2, "promo": 2
        },
        "airline": {
            "world sale": 4, "global sale": 4, "flight sale": 4,
            "special fares": 3, "lowest fares": 3,
            "club world": 3, "premium economy": 3
        },
        "route": {
            "mumbai": 5, "bom": 5,
            "london": 5, "lhr": 5,
            "new york": 5, "jfk": 5
        }
    }

    try:
        response = urllib.request.urlopen(url, timeout=10)
        html = response.read().decode("utf-8")

        score, hits = score_text(html, keyword_groups)

        if score >= 10:
            return f"BA SALE detected (score {score}, hits: {hits})"
        else:
            return f"BA: No sale (score {score})"

    except Exception as e:
        return f"BA: Error → {e}"

