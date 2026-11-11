
import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# ---------------- TICKET PRICE TESTS ----------------

def test_invalid_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("vip", 25, 15, False)


def test_invalid_show_hour_above_range():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 24, False)


def test_invalid_show_hour_below_range():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, -1, False)


def test_regular_afternoon():
    assert ticket_price("regular", 25, 15, False) == 150


def test_morning_discount():
    assert ticket_price("regular", 25, 10, False) == 100


def test_evening_weekend_price():
    assert ticket_price("premium", 25, 20, True) == 320


def test_child_below_three():
    assert ticket_price("regular", 2, 15, False) == 0


def test_child_discount():
    assert ticket_price("premium", 10, 15, False) == 125


# ---------------- GROUP DISCOUNT TESTS ----------------

def test_zero_tickets():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_large_student_group():
    assert group_discount(10, True) == 20


def test_medium_group():
    assert group_discount(5, False) == 10


def test_small_group():
    assert group_discount(2, False) == 0


# ---------------- SNACK COMBO TESTS ----------------

def test_small_combo_with_coupon():
    assert snack_combo("small", True) == 70


def test_medium_combo_without_coupon():
    assert snack_combo("medium", False) == 180


def test_large_combo_with_coupon():
    assert snack_combo("large", True) == 200
