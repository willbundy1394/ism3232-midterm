"""Part 3: Report for Ridgeline Tool Rental"""

from business_rules import (
    calculate_quote,
    needs_pickup_inspection,
    total_quoted,
    largest_rental,
    format_rental_line,
    required_deposit,
)

rentals = [
    {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
    {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
    {"customer": "Chowdhury", "daily_rate": 85.00, "days": 4, "contractor": False},
    {"customer": "Dvorak", "daily_rate": 120.00, "days": 10, "contractor": False},
    {"customer": "Eastman", "daily_rate": 210.00, "days": 8, "contractor": True},
    {"customer": "Fujita", "daily_rate": 250.00, "days": 4, "contractor": False},
    {"customer": "Garza", "daily_rate": 95.00, "days": 5, "contractor": True},
    {"customer": "Hughes", "daily_rate": 200.00, "days": 7, "contractor": False},
]

print("Ridgeline Tool Rental - Rental Report")

deposit_count = 0
inspection_count = 0

for rental in rentals:
    quote = calculate_quote(rental['daily_rate'], rental['days'], rental.get('contractor', False))
    deposit = required_deposit(quote)
    inspection = needs_pickup_inspection(rental['days'], quote)

    if deposit:
        deposit_count += 1
    if inspection:
        inspection_count += 1  

    print(format_rental_line(rental['customer'], quote, deposit, inspection))

    total = total_quoted(rentals)
    count = len(rentals)
    average = total / count if count > 0 else 0.0
    largest = largest_rental(rentals)

print(f"Total Rentals: {count}")
print(f"Total Quoted: ${total:.2f}")
print(f"Average Quote: ${average:.2f}")
print(f"Largest Quote: {largest}")
print(f"Deposits Required: {deposit_count}")
print(f"Inspections Required: {inspection_count}")







