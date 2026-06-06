import re

def extract_price(html):
    """
    Extracts the first currency-like price from HTML.
    Works for USD ($199), INR (₹25,000), EUR (€350), etc.
    """
    html = html.replace(",", "")
    patterns = [
        r"\$([0-9]+)",          # $199
        r"₹\s*([0-9]+)",        # ₹25000
        r"eur\s*([0-9]+)",      # EUR 350
        r"€\s*([0-9]+)"         # €350
    ]

    for p in patterns:
        match = re.search(p, html.lower())
        if match:
            return int(match.group(1))

    return None
