
import re
import pytest
from hypothesis import given, strategies as st
from movie_tickets import parse_seat, total_price, average_rating


# 1. parse_seat: valid seats must contain one letter followed by a positive number.
@given(st.text())
def test_parse_seat_validates_input(seat):
    if re.fullmatch(r"[A-Za-z][1-9][0-9]*", seat):
        result = parse_seat(seat)
        assert result[0] == seat[0].upper()
        assert result[1] == int(seat[1:])
    else:
        with pytest.raises(ValueError):
            parse_seat(seat)


def test_parse_seat_rejects_none():
    with pytest.raises(ValueError):
        parse_seat(None)


# 2. total_price: prices must be non-negative integers.
@given(st.lists(st.integers(min_value=-1000, max_value=1000), min_size=1))
def test_total_price_validates_input(prices):
    prices_csv = ",".join(str(price) for price in prices)

    if any(price < 0 for price in prices):
        with pytest.raises(ValueError):
            total_price(prices_csv)
    else:
        expected = round(sum(prices) * 1.18, 2)
        assert total_price(prices_csv) == expected


def test_total_price_rejects_none():
    with pytest.raises(ValueError):
        total_price(None)


# 3. average_rating: ratings must be integers from 1 to 5.
@given(st.lists(st.integers(min_value=0, max_value=10), min_size=1))
def test_average_rating_validates_input(ratings):
    ratings_text = " ".join(str(rating) for rating in ratings)

    if any(rating < 1 or rating > 5 for rating in ratings):
        with pytest.raises(ValueError):
            average_rating(ratings_text)
    else:
        expected = round(sum(ratings) / len(ratings), 1)
        assert average_rating(ratings_text) == expected


def test_average_rating_rejects_none():
    with pytest.raises(ValueError):
        average_rating(None)
