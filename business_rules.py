"""Part 2: Business Rules and Calculations"""

DAILY_RATE_MULTIPLIER = 1.0
DISCOUNT_TIER_1_DAYS = 3
DISCOUNT_TIER_2_DAYS = 7
DISCOUNT_TIER_1_RATE = 0.10
DISCOUNT_TIER_2_RATE = 0.20
MIN_CONTRACTOR_DISCOUNT = 0.10
WAIVER_FEE = 25.00
WAIVER_FEE_LIMIT = 150.00
DEPOSIT_LIMIT = 1000.00
PICKUP_INSPECTION_DAYS_LIMIT = 5
PICKUP_INSPECTION_QUOTE_LIMIT = 800.00

def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Returns the rental cost before any discount"""
    return daily_rate * days

def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Returns the discount rate as a decimal, so 10% is 0.10"""
    discount = 0.0
    if days >= DISCOUNT_TIER_2_DAYS:
        discount = DISCOUNT_TIER_2_RATE
    elif days >= DISCOUNT_TIER_1_DAYS:
        discount = DISCOUNT_TIER_1_RATE

    if contractor and discount <  MIN_CONTRACTOR_DISCOUNT:
        discount = MIN_CONTRACTOR_DISCOUNT

    return discount

def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    """Returns the quote for one rental: the discounted cost, plusg waiver fee if applicable. It must call your first 2 functions"""
    rental_cost = calculate_rental_cost(daily_rate, days)
    discount_rate = get_rental_discount(days, contractor)
    discounted_cost = rental_cost * (1 - discount_rate)

    waiver_fee = 0.0
    if discounted_cost < WAIVER_FEE_LIMIT:
        discounted_cost += WAIVER_FEE

    total_quote = discounted_cost + waiver_fee
    return total_quote

def needs_pickup_inspection(days: int, quote: float) -> bool:
    """Returns True if the rental needs a pickup inspection, False otherwise"""
    return days >= PICKUP_INSPECTION_DAYS_LIMIT and quote > PICKUP_INSPECTION_QUOTE_LIMIT

def total_quoted(rentals: list) -> float:
    """Returns the sum of the quotes for every rental in the list. It must use a for loop that calls calculate_quote."""
    total = 0.0
    for rental in rentals:
        total += calculate_quote(rental['daily_rate'], rental['days'], rental.get('contractor', False))
    return total

def largest_rental(rentals: list) -> str:
    """Returns the customer of the rental with the largest quote. If two are tied for largest, it returns the one that comes first in the list. An empty list should return an empty string. It must use a for loop that calls calculate_quote."""
    if not rentals:
        return ""
    largest_quote = 0.0
    largest_rental_name = ""
    for rental in rentals:
        quote = calculate_quote(rental['daily_rate'], rental['days'], rental.get('contractor', False))
        if quote > largest_quote:
            largest_quote = quote
            largest_rental_name = rental['name']   
    return largest_rental_name

def format_rental_line(customer: str, quote: float, deposit: bool, inspection: bool) -> str:
    """Returns one line of report, such as Alverez: $145.00 | deposit: no | inspection: no. Each True/False value is shown as yes or no, and the amount always has two decimal places"""
    deposit_str = "Yes" if deposit else "No"
    inspection_str = "Yes" if inspection else "No"
    return f"{customer}: ${quote:.2f} | deposit: {deposit_str.lower()} | inspection: {inspection_str.lower()}"

