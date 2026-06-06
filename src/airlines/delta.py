import urllib.request
from utils.keyword_scoring import score_text
from utils.price_extract import extract_price

def check_sales():
    url = "https://www.delta.com/us/en/flight-deals/united-states-flights"

    keyword_groups = {
        "core": {"sale": 2, "deal": 2, "offer": 2, "discount": 2},
        "airline": {"flash sale": 4, "fare sale": 4, "getaway": 3},
        "route": {"tampa": 5, "tpa": 5, "detroit": 5, "dtw": 5}
    }

    PRICE_THRESHOLD = 150  # USD

    try:
        response = urllib.request.urlopen(url, timeout=10)
        html = response.read().decode("utf-8")

        score, hits = score_text(html, keyword_groups)

        if score < 8:
            return None  # no sale

        price = extract_price(html)

        if price and price < PRICE_THRESHOLD:
            return f"Delta DTW→TPA sale: ${price} (score {score})"

        return None

    except Exception as e:
        return f"Delta error: {e}"

