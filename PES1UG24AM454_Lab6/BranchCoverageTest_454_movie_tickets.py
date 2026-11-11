
import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# ---------------- TICKET PRICE BRANCH TESTS ----------------

def test_invalid_seat():
    with pytest.raises(ValueError):
        ticket_price("vip", 25, 15, False)


def test_invalid_time_negative():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, -1, False)


def test_invalid_time_above_range():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, 24, False)


def test_morning_show():
    assert ticket_price("regular", 25, 10, False) == 100


def test_afternoon_show():
    assert ticket_price("regular", 25, 15, False) == 150


def test_evening_show():
    assert ticket_price("regular", 25, 20, False) == 180


def test_weekend_show():
    assert ticket_price("regular", 25, 15, True) == 190


def test_age_below_three():
    assert ticket_price("regular", 2, 15, False) == 0


def test_age_twelve():
    assert ticket_price("regular", 12, 15, False) == 75


def test_adult_age():
    assert ticket_price("regular", 30, 15, False) == 150


def test_senior_age():
    assert ticket_price("regular", 60, 15, False) == 75


# ---------------- GROUP DISCOUNT BRANCH TESTS ----------------

def test_no_tickets():
    with pytest.raises(ValueError):
        group_discount(0, False)


def test_one_ticket():
    assert group_discount(1, False) == 0


def test_five_tickets():
    assert group_discount(5, False) == 10


def test_ten_tickets():
    assert group_discount(10, False) == 15


def test_student_group_with_discount():
    assert group_discount(5, True) == 15


def test_student_group_without_discount():
    assert group_discount(2, True) == 0


# ---------------- SNACK COMBO BRANCH TESTS ----------------

def test_small_with_coupon():
    assert snack_combo("small", True) == 70


def test_small_without_coupon():
    assert snack_combo("small", False) == 120


def test_medium_with_coupon():
    assert snack_combo("medium", True) == 130


def test_medium_without_coupon():
    assert snack_combo("medium", False) == 180


def test_large_with_coupon():
    assert snack_combo("large", True) == 200


def test_large_without_coupon():
    assert snack_combo("large", False) == 250
