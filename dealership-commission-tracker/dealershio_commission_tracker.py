# CarSale class to represent each individual car sale
class CarSale:
    def __init__(self, car_model, price, salesperson):
        """
        Initialize a car sale record.
        
        Parameters:
            car_model (str): Name/model of the car sold
            price (float/int): Selling price in USD
            salesperson (str): Name of the salesperson who made the sale
        """
        self.car_model = car_model
        self.price = price
        self.salesperson = salesperson
    
    def commission(self):
        """
        Calculate the commission for this sale according to the rules:
        - Base commission: 8% of the price on ALL sales
        - Bonus: + extra 2% commission if price > $50,000
        → Total = 10% when price > 50,000, otherwise 8%
        
        Returns:
            float: Commission amount earned from this sale
        """
        base_commission = self.price * 0.08
        
        if self.price > 50000:
            bonus_commission = self.price * 0.02      # extra 2% bonus
            return base_commission + bonus_commission
        else:
            return base_commission
    
    def __str__(self):
        """
        String representation for nice printing of each sale.
        Shows model, price, salesperson, and commission earned.
        """
        return (f"Car model: {self.car_model:<15} | "
                f"Price: ${self.price:>10,.2f} | "
                f"Salesperson: {self.salesperson:<8} | "
                f"Commission: ${self.commission():>10,.2f}")


# Sample sales data (you can add more entries here)
sales = [
    CarSale("Kia K4",       22290, "Mike"),
    CarSale("Honda Civic",  26490, "Brenda"),
    CarSale("Honda Accord", 30980, "Mike"),
    CarSale("Nissan Sentra",23900, "Thomas"),
    CarSale("Toyota RAV4",  50200, "Mike")   # This one triggers the 2% bonus
]

# --- Main program / report generation ---

# Step 1: Print individual sales report
print("=== Individual Sales Report ===")
print("-" * 80)
for sale in sales:
    print(sale)
print("-" * 80)

# Step 2: Calculate total commissions per salesperson
total_commissions = {}

for sale in sales:
    salesperson = sale.salesperson
    # Use .get() to safely add commission (0 if salesperson not seen yet)
    total_commissions[salesperson] = total_commissions.get(salesperson, 0) + sale.commission()

# Step 3: Print total commissions summary
print("\n=== Total Commissions by Salesperson ===")
print("-" * 50)
for salesperson in sorted(total_commissions):  # sorted alphabetically
    total = total_commissions[salesperson]
    print(f"Salesperson: {salesperson:<8} → Total Commission: ${total:>10,.2f}")

print("\nTotal sales processed:", len(sales))
