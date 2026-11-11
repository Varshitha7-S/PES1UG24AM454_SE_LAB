
import re


def parse_seat(seat):
    if not isinstance(seat, str):
        raise ValueError("Seat must be a string.")

    if not re.fullmatch(r"[A-Za-z][1-9][0-9]*", seat):
        raise ValueError("Invalid seat format. Use a letter followed by a positive number.")

    return seat[0].upper(), int(seat[1:])


def total_price(prices_csv):
    if not isinstance(prices_csv, str) or not prices_csv.strip():
        raise ValueError("Prices must be a non-empty comma-separated string.")

    try:
        prices = [int(p.strip()) for p in prices_csv.split(",")]
    except ValueError:
        raise ValueError("Prices must contain only integers.")

    if any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative.")

    return round(sum(prices) * 1.18, 2)


def average_rating(ratings):
    if not isinstance(ratings, str) or not ratings.strip():
        raise ValueError("Ratings must be a non-empty string.")

    try:
        values = [int(r) for r in ratings.split()]
    except ValueError:
        raise ValueError("Ratings must contain only integers.")

    if any(rating < 1 or rating > 5 for rating in values):
        raise ValueError("Ratings must be between 1 and 5.")

    return round(sum(values) / len(values), 1)


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    print("Row and Seat:", result)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    print("Total with GST:", result)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    print("Average Rating:", result)


if __name__ == "__main__":
    main()
