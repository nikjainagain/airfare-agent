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

    for airline, scraper in scrapers.items():
        try:
            result = scraper()
            print(f"{airline}: {result}")
        except Exception as e:
            print(f"{airline}: Error running scraper → {e}")


if __name__ == "__main__":
    main()
