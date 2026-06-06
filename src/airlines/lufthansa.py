import urllib.request

def check_sales():
    url = "https://www.lufthansa.com/in/en/flight-deals"

    core = ["sale", "offer", "discount", "deal", "promo"]
    lh_specific = ["companion", "global sale", "europe special", "saver fare",
                   "premium economy", "business class", "best price"]
    route_specific = ["mumbai", "bom", "frankfurt", "fra", "munich", "muc", "new york", "jfk"]

    try:
        response = urllib.request.urlopen(url, timeout=10)
        html = response.read().decode("utf-8").lower()

        if any(k in html for k in core + lh_specific + route_specific):
            return "Lufthansa: Sale‑related keywords detected for BOM→Europe/NYC."
        else:
            return "Lufthansa: No sale detected for BOM routes."

    except Exception as e:
        return f"Lufthansa: Error checking sale → {e}"


