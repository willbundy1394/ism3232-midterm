"""Ridgeline Tool Rental Business Rules Tests"""

from business_rules import (
    calculate_quote,
    calculate_rental_cost,
    format_rental_line,
    get_rental_discount,
    largest_rental,
    needs_pickup_inspection,
    required_deposit,
    total_quoted,
)


def test_calculate_rental_cost():
    """Test the calculate_rental_cost function before any discount is applied"""
    assert calculate_rental_cost(50.00, 3) == 150.00


def test_get_rental_discount_tier_1_exact():
    """Test discount for tier 1 (3-6 days)"""
    assert get_rental_discount(3, contractor=False) == 0.10


def test_get_rental_discount_tier_1_below():
    """Test discount for Tier 1 (2 days)"""
    assert get_rental_discount(2, contractor=False) == 0.0


def test_get_rental_discount_tier_1_above():
    """Test discount for Tier 1 (4 days)"""
    assert get_rental_discount(4, contractor=False) == 0.10


def test_get_rental_discount_tier_2_exact():
    """Test discount for Tier 2 (7 days)"""
    assert get_rental_discount(7, contractor=False) == 0.20


def test_get_rental_discount_tier_2_below():
    """Test discount for Tier 2 (6 days)"""
    assert get_rental_discount(6, contractor=False) == 0.10


def test_get_rental_discount_tier_2_above():
    """Test discount for Tier 2 (10 days)"""
    assert get_rental_discount(10, contractor=False) == 0.20


def test_get_rental_discount_contractor_min_discount():
    """Test discount for contractor with 2 days (minimum contractor discount)"""
    assert get_rental_discount(2, contractor=True) == 0.10


def test_calculate_quote_below_waiver_fee_limit():
    """Test quote calculation for 2 days (below waiver fee limit)"""
    assert round(calculate_quote(60.00, 2, contractor=False), 2) == 145.00


def test_calculate_quote_above_waiver_fee_limit():
    """Test quote calculation for 4 days (above waiver fee limit)"""
    assert round(calculate_quote(60.00, 4, contractor=False), 2) == 216.00


def test_required_deposit_true():
    """Test required_deposit function for quote above deposit limit"""
    assert required_deposit(1500.00) == True


def test_required_deposit_false():
    """Test required_deposit function for quote below deposit limit"""
    assert required_deposit(1000.00) == False


def test_needs_pickup_inspection_true():
    """Test needs_pickup_inspection function for 6 days and quote above inspection quote limit"""
    assert needs_pickup_inspection(6, 900.00) == True


def test_needs_pickup_inspection_false_days():
    """Test needs_pickup_inspection function for 4 days and quote above inspection quote limit"""
    assert needs_pickup_inspection(4, 900.00) == False


def test_needs_pickup_inspection_false_quote():
    """Test needs_pickup_inspection function for 6 days and quote below inspection quote limit"""
    assert needs_pickup_inspection(6, 700.00) == False


def test_total_quoted():
    """Test total_quoted function for a list of rentals"""
    rentals = [
        {"daily_rate": 60.00, "days": 2, "contractor": False},
        {"daily_rate": 60.00, "days": 4, "contractor": False},
        {"daily_rate": 60.00, "days": 7, "contractor": True},
    ]
    assert round(total_quoted(rentals), 2) == 697.00


def test_largest_rental():
    """Test largest_rental returns the customer of the rental with the largest quote"""
    rentals = [
        {"customer": "Alice", "daily_rate": 60.00, "days": 2, "contractor": False},
        {"customer": "Bob", "daily_rate": 60.00, "days": 4, "contractor": False},
        {"customer": "Charlie", "daily_rate": 60.00, "days": 7, "contractor": True},
    ]
    assert largest_rental(rentals) == "Charlie"


def test_largest_rental_tie():
    """Test largest_rental returns the first customer in case of a tie"""
    rentals = [
        {"customer": "Alice", "daily_rate": 60.00, "days": 4, "contractor": False},
        {"customer": "Bob", "daily_rate": 60.00, "days": 4, "contractor": False},
    ]
    assert largest_rental(rentals) == "Alice"


def test_largest_rental_empty():
    """Test largest_rental returns an empty string for an empty list"""
    rentals = []
    assert largest_rental(rentals) == ""


def test_format_rental_line():
    """Test format_rental_line formats string output correctly"""
    result = format_rental_line("Alice", 150.00, deposit=True, inspection=False)
    assert result == "Alice: $150.00 | deposit: yes | inspection: no"
