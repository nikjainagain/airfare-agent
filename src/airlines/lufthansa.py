import urllib.request
from utils.keyword_scoring import score_text

def check_sales():
    url = "https://www.lufthansa.com/in/en/flight-deals"

    keyword_groups = {
        "core": {
            "sale": 2, "offer": 2, "discount": 2, "deal": 2, "promo": 2
        },
        "airline": {
            "companion": 4, "global sale": 4, "europe special": 4,
            "saver fare": 3, "premium economy": 3, "business class": 3,
            "best price": 3
        },
        "route": {
            "mumbai": 5, "bom": 5,
            "frankfurt": 5, "fra": 5,
            "munich": 5, "muc": 5,
            "new york": 5, "jfk": 5
        }
    }

    try:
        response = urllib.request.urlopen(url, timeout=10)
        html = response.read().decode("utf-8")

        score, hits = score_text(html, keyword_groups)

        if score >= 10:
            return f"Lufthansa SALE detected (score {score}, hits: {hits})"
        else:
            return f"Lufthansa: No sale (score {score})"

    except Exception as e:
        return f"Lufthansa: Error → {e}"


