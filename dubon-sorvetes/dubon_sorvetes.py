import csv
from collections import defaultdict

"""
Define the daily commission for each Dubon salesperson
"""

# Create the commission rate of 10% by sale
COMMISSION_RATE = 0.1

# Store the total revenue in a float number
total_revenue = 0.0

bonuses = defaultdict(float)

# Fetch CSV table wth daily sales by each salesperson
with open("dubon_sales.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        price = float(row["price"])
        bonuses[row["salesperson"]] += price * COMMISSION_RATE
        total_revenue += price


print(f"Total revenue: {total_revenue:.2f}\n")
print("=== Comissão total para cada vendedor ===")
for salesperson, bonus in bonuses.items():
    print(f"{salesperson}: R${bonus:.2f}")


