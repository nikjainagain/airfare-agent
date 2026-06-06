import urllib.request

def check_sales():
    url = "https://www.delta.com/us/en/flight-deals/united-states-flights"

    core = ["sale", "deal", "offer", "discount", "promo", "special fare", "limited time"]
    delta_specific = ["flash sale", "fare sale", "getaway", "low fare", "domestic deals"]
    route_specific = ["tampa", "tpa", "detroit", "dtw"]

    try:
        response = urllib.request.urlopen(url, timeout=10)
        html = response.read().decode("utf-8").lower()

        if any(k in html for k in core + delta_specific + route_specific):
            return "Delta: Sale‑related keywords detected for DTW→TPA."
        else:
            return "Delta: No sale detected for DTW→TPA."

    except Exception as e:
        return f"Delta: Error checking sale → {e}"

