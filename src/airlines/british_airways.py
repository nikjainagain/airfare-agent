import urllib.request
from utils.keyword_scoring import score_text
from utils.price_extract import extract_price

def check_sales():
    url = "https://www.britishairways.com/en-in/offers/flights"

    keyword_groups = {
        "core": {"sale": 2, "offer": 2, "discount": 2},
        "airline": {"world sale": 4, "global sale": 4, "flight sale": 4},
        "route": {"mumbai": 5, "bom": 5, "london": 5, "lhr": 5}
    }

    PRICE_THRESHOLD = 35000  # INR

    try:
        response = urllib.request.urlopen(url, timeout=10)
        html = response.read().decode("utf-8")

        score, hits = score_text(html, keyword_groups)

        if score < 10:
            return None

        price = extract_price(html)

        if price and price < PRICE_THRESHOLD:
            return f"BA BOM→EU/NYC sale: ₹{price} (score {score})"

        return None

    except Exception as e:
        return f"BA error: {e}"


