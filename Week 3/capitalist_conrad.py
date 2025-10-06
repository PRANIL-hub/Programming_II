"""
Capitalist Conrad - Stock Price Simulator (GPT-5 Version)
--------------------------------------------------------
Simulates the daily price changes of a volatile stock.

Rules:
- Starting price: $10.00
- 50% chance of increasing by 0–10%
- 50% chance of decreasing by 0–5%
- Stops if price goes above $1000 or below $0.01
- Results are printed to both the console and a file
"""

import random

# Constants
MAX_INCREASE = 0.1       # 10%
MAX_DECREASE = 0.05      # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_output.txt"


def simulate_stock():
    """Simulate stock price changes and save results to file."""
    price = INITIAL_PRICE
    day = 0

    # Use context manager to safely write to file
    with open(OUTPUT_FILE, "w") as file:
        print(f"Starting price: ${price:,.2f}")
        print(f"Starting price: ${price:,.2f}", file=file)

        # Loop until price goes out of the set range
        while MIN_PRICE <= price <= MAX_PRICE:
            day += 1
            # Randomly choose increase or decrease
            if random.choice([True, False]):
                price_change = random.uniform(0, MAX_INCREASE)
            else:
                price_change = random.uniform(-MAX_DECREASE, 0)

            price *= (1 + price_change)
            print(f"On day {day:3} price is: ${price:,.2f}")
            print(f"On day {day:3} price is: ${price:,.2f}", file=file)


# Run the simulator
simulate_stock()
