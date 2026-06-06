import urllib.request

def check_sales():
    url = "https://www.britishairways.com/en-in/offers/flights"

    try:
        response = urllib.request.urlopen(url, timeout=10)
        html = response.read().decode("utf-8").lower()

        keywords = [
            "sale", "offer", "discount", "deal",
            "mumbai", "bom",
            "london", "lhr",
            "new york", "jfk"
        ]

        if any(k in html for k in keywords):
            return "BA: Possible sale detected for BOM→Europe/NYC."
        else:
            return "BA: No sale detected for BOM routes."

    except Exception as e:
        return f"BA: Error checking sale → {e}"
