# Terminal Record: Ridgeline Tool Rental

## 1. Building the project

mkdir ism3232-midterm
cd ism3232-midterm
git init
git branch -M main
git remote add origin https://github.com/willbundy1394/ism3232-midterm.git
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
pip freeze > requirements.txt
echo ".venv/" > gitignore
echo "__pychache__/" >> gitignore
touch business_rules.py main.py commands.md README.md
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
git commit -, "Part 1 Project Setup"
git push -u origin main

## 2. The virtual environment

/Users/zooweemama/ism3232-midterm/.venv/bin/python3

This output shows that the path is inside the .venv directory which means that the virtual environment is active.

## 3. The project structure

.
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── gitignore
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

After running tree -L 2 the folder that is on my computer but not in the github is the .venv folder. This folder doesnt get uploaded because the .gitignore file blocks it

## 4. Every function and test

business_rules.py
15:def calculate_rental_cost(daily_rate: float, days: int) -> float:
19:def get_rental_discount(days: int, contractor: bool = False) -> float:
32:def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
45:def required_deposit(quote: float) -> bool:
49:def needs_pickup_inspection(days: int, quote: float) -> bool:
53:def total_quoted(rentals: list) -> float:
60:def largest_rental(rentals: list) -> str:
73:def format_rental_line(customer: str, quote: float, deposit: bool, inspection: bool) -> str:

tests/test_business_rules.py
13:def test_calculate_rental_cost():
17:def test_get_rental_discount_tier_1_exact():
21:def test_get_rental_discount_tier_1_below():
25:def test_get_rental_discount_tier_1_above():
29:def test_get_rental_discount_tier_2_exact():
33:def test_get_rental_discount_tier_2_below():
37:def test_get_rental_discount_tier_2_above():
41:def test_get_rental_discount_contractor_min_discount():
45:def test_calculate_quote_below_waiver_fee_limit():
49:def test_calculate_quote_above_waiver_fee_limit():
53:def test_required_deposit_true():
57:def test_required_deposit_false():
61:def test_needs_pickup_inspection_true():
65:def test_needs_pickup_inspection_false_days():
69:def test_needs_pickup_inspection_false_quote():
73:def test_total_quoted():
82:def test_largest_rental():
91:def test_largest_rental_tie():
99:def test_largest_rental_empty():
104:def test_format_rental_line():

the business_rules.py defines 8 functions and the other folder named tests/test_business_rules.py defines 20 tests

## 5. Which files print

main.py 

main.py is the only file that shows up because this file runs the report while business_rules.py only does the math part

## 6. The commit history

817d4d2 (HEAD -> main, origin/main) Part 4: Ridgeline Tool Rental Business Rules Tests
46668d1 Part 3: Report for Ridgeline Tool Rental
52c5dbe Update Business Rules and Calculations
8ccbf5b Update Business Rules and Calculations
04714c5 Part 2: Business Rules and Calculations
f659ad3 Part 1 Project Setup

There were 6 commits at that point