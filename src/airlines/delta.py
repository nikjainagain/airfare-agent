import urllib.request
from utils.keyword_scoring import score_text

def check_sales():
    url = "https://www.delta.com/us/en/flight-deals/united-states-flights"

    keyword_groups = {
        "core": {
            "sale": 2, "deal": 2, "offer": 2, "discount": 2,
            "promo": 2, "special fare": 2, "limited time": 2
        },
        "airline": {
            "flash sale": 4, "fare sale": 4, "getaway": 3,
            "low fare": 3, "domestic deals": 3
        },
        "route": {
            "tampa": 5, "tpa": 5, "detroit": 5, "dtw": 5
        }
    }

    try:
        response = urllib.request.urlopen(url, timeout=10)
        html = response.read().decode("utf-8")

        score, hits = score_text(html, keyword_groups)

        if score >= 8:
            return f"Delta SALE detected (score {score}, hits: {hits})"
        else:
            return f"Delta: No sale (score {score})"

    except Exception as e:
        return f"Delta: Error → {e}"

