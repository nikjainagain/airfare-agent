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

    results = []

    for airline, scraper in scrapers.items():
        try:
            result = scraper()
            line = f"{airline}: {result}"
            print(line)
            results.append(line)
        except Exception as e:
            error_line = f"{airline}: Error running scraper → {e}"
            print(error_line)
            results.append(error_line)

    # Build email body
    email_body = "\n".join(results)

    # Send email
    send_email(
        subject="Daily Airline Sales Report",
        body=email_body
    )


if __name__ == "__main__":
    main()

          
