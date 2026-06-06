from airlines import (
    delta,
    emirates,
    etihad,
    aegean,
    lufthansa,
    british_airways,
    qatar,
    turkish,
)

from alerts.email_alert import send_email


def main():
    print("Checking airline sales...\n")

    scrapers = {
        "Delta": delta.check_sales,
        "Emirates": emirates.check_sales,
        "Etihad": etihad.check_sales,
        "Aegean": aegean.check_sales,
        "Lufthansa": lufthansa.check_sales,
        "British Airways": british_airways.check_sales,
        "Qatar Airways": qatar.check_sales,
        "Turkish Airlines": turkish.check_sales,
    }

    sale_hits = []

    for airline, scraper in scrapers.items():
        try:
            result = scraper()

            print(f"{airline}: {result}")

            # NEW LOGIC: only add if scraper returned a real sale
            if result:
                sale_hits.append(f"{airline}: {result}")

        except Exception as e:
            print(f"{airline}: Error running scraper → {e}")

    # Only send email if at least one sale is detected
    if sale_hits:
        email_body = "\n".join(sale_hits)
        send_email(
            subject="Flash Sale Detected!",
            body=email_body
        )
        print("\nEmail sent because a sale was detected.")
    else:
        print("\nNo sales detected. No email sent.")
