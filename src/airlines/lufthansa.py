import urllib.request

def check_sales():
    url = "https://www.lufthansa.com/in/en/flight-deals"

    try:
        response = urllib.request.urlopen(url, timeout=10)
        html = response.read().decode("utf-8").lower()

        keywords = [
            "sale", "offer", "discount", "deal",
            "mumbai", "bom",
            "frankfurt", "fra",
            "munich", "muc",
            "new york", "jfk"
        ]

        if any(k in html for k in keywords):
            return "Lufthansa: Possible sale detected for BOM→Europe/NYC."
        else:
            return "Lufthansa: No sale detected for BOM routes."

    except Exception as e:
        return f"Lufthansa: Error checking sale → {e}"

