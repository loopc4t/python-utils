class CarSale:
    """Single car sale record."""

    def __init__(self, car_model, price, salesperson):
        self.car_model = car_model
        self.price = price
        self.salesperson = salesperson

    def commission(self):
        """8% commission, raised to 10% for cars over $50,000."""
        rate = 0.10 if self.price > 50000 else 0.08
        return self.price * rate

    def __str__(self):
        return (f"Car model: {self.car_model:<15} | "
                f"Price: ${self.price:>10,.2f} | "
                f"Salesperson: {self.salesperson:<8} | "
                f"Commission: ${self.commission():>10,.2f}")


sales = [
    CarSale("Kia K4",        22290, "Mike"),
    CarSale("Honda Civic",   26490, "Brenda"),
    CarSale("Honda Accord",  30980, "Mike"),
    CarSale("Nissan Sentra", 23900, "Thomas"),
    CarSale("Toyota RAV4",   50200, "Mike"),
]

print("=== Individual Sales Report ===")
print("-" * 80)
for sale in sales:
    print(sale)
print("-" * 80)

# Accumulate commissions per salesperson
totals = {}
for sale in sales:
    totals[sale.salesperson] = totals.get(sale.salesperson, 0) + sale.commission()

print("\n=== Total Commissions by Salesperson ===")
print("-" * 50)
for person in sorted(totals):
    print(f"Salesperson: {person:<8} → Total Commission: ${totals[person]:>10,.2f}")

print("\nTotal sales processed:", len(sales))
