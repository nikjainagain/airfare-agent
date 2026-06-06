import urllib.request

def check_sales():
    url = "https://www.delta.com/us/en/flight-deals/united-states-flights"

    try:
        response = urllib.request.urlopen(url, timeout=10)
        html = response.read().decode("utf-8").lower()

        keywords = ["sale", "deal", "offer", "discount", "tampa", "tpa"]

        if any(k in html for k in keywords):
            return "Delta: Possible sale or offer detected (DTW→TPA keywords found)."
        else:
            return "Delta: No sale detected for DTW→TPA."

    except Exception as e:
        return f"Delta: Error checking sale → {e}"

