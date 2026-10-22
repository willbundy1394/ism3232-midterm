# ISM3232 Midterm: Ridgeline Tool Rental

- **Name:** Will Bundy
- **Version:** ALPHA
- **Date:** October 23, 2026

## What This Program Does

The program created today was created to calculate equipment rental costs and generate a formatted report for the company Ridgeline Tool Rental. This program was designed to compute rental pricinng automatically based on the daily rates as well as how long the customer would be using said equipment. It also applies contractor or long term discounts, determines deposit requirements and flags if equipment needs a pickup inspection. 

## Business Rules

- Rental costs are calculated by multiplying the daily rate by the amount days rented 
- Discounts are applied based on the rental duration tiers as well as contractor status
- Quotes above a specific amount would trigger a mandatory security deposit
- Long rental durations or high quotes require a pickup inspection
- It adds up all the rentals on a customer's list to find the total price
- Looks through all the rentals and finds the most expensive one

## How to Run

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py

## How to Test

ruff format .
ruff check .
pytest -v 
There were a total of 20 tests written to verify the business rules

## Files in This Repository

- business_rules.py : This file contains the calculations and business rule functions for rentals, discounts and quotes
- main.py : This file executes the rental reporting script and prints the formatted customer outputs
- tests/test_business_rules.py : this file contains 20 tests that verify the busiess rules 
- tests/__init__.py : This file tells python that the test folder is a package 
- .gitignore : Hides all the unnecessary files from GitHub
- requirements.txt : Lists the extra tools such as pytest and ruff needed to run the project
- commands.md : Shows the history of command use within the terminal
- README.md : Explains how to use the project 

## AI Use Statement

I did not use Ai on this exam, all code was written and tested by me in VS Code.  
