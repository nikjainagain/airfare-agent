import urllib.request

def check_sales():
    url = "https://www.britishairways.com/en-in/offers/flights"

    core = ["sale", "offer", "discount", "deal", "promo"]
    ba_specific = ["world sale", "global sale", "flight sale", "special fares",
                   "lowest fares", "club world", "premium economy"]
    route_specific = ["mumbai", "bom", "london", "lhr", "new york", "jfk"]

    try:
        response = urllib.request.urlopen(url, timeout=10)
        html = response.read().decode("utf-8").lower()

        if any(k in html for k in core + ba_specific + route_specific):
            return "BA: Sale‑related keywords detected for BOM→Europe/NYC."
        else:
            return "BA: No sale detected for BOM routes."

    except Exception as e:
        return f"BA: Error checking sale → {e}"

