class Product:
    """
    Represents a grocery product in the store inventory.
    Tracks name, unit price, stock quantity, and calculates total stock value.
    """

    def __init__(self, name, price_per_unit, quantity):
        """
        Initialize a product.

        Args:
            name (str): Product name (e.g., "Apple", "Milk")
            price_per_unit (float): Price for one unit (positive number)
            quantity (int): Number of units currently in stock (non-negative integer)
        """
        if not name.strip():
            raise ValueError("Product name cannot be empty")
        if price_per_unit <= 0:
            raise ValueError(
                f"Price per unit must be positive. Got {price_per_unit} for {name}")
        if quantity < 0:
            raise ValueError(
                f"Quantity cannot be negative. Got {quantity} for {name}")

        self.name = name.strip()
        self.price_per_unit = float(price_per_unit)
        self.quantity = int(quantity)

    def total_value(self):
        """
        Calculate the total monetary value of this product currently in stock.

        Returns:
            float: Total value = price_per_unit × quantity
        """
        return self.price_per_unit * self.quantity

    def __str__(self):
        """
        Return a nicely formatted string for display.
        Aligns columns for better readability in reports.
        """
        value = self.total_value()
        return (
            f"{self.name:<20} "
            f"Price: ${self.price_per_unit:>7.2f}  "
            f"Qty: {self.quantity:>4}  "
            f"Total value: ${value:>10,.2f}"
        )


def main():
    """
    Main program:
    - Collects information for 3 grocery products
    - Validates inputs
    - Sorts products by total inventory value (highest to lowest)
    - Prints a clean inventory report
    """
    print("=== Grocery Inventory Manager ===")
    print("Enter details for 3 products\n")

    products_list = []

    for i in range(1, 4):
        print(f"Product #{i}:")
        while True:
            try:
                name = input("  Product name: ").strip()
                if not name:
                    print("  Name cannot be empty. Try again.")
                    continue

                price_input = input("  Price per unit ($): ").strip()
                price = float(price_input)

                qty_input = input("  Quantity in stock: ").strip()
                qty = int(qty_input)

                product = Product(name, price, qty)
                products_list.append(product)
                print()  # blank line between products
                break

            except ValueError as e:
                if "could not convert" in str(e):
                    print("  Invalid number. Please enter valid numbers.\n")
                else:
                    print(f"  Error: {e}\n")

    if not products_list:
        print("No valid products entered. Exiting.")
        return

    # Sort by total value descending (most valuable stock first)
    sorted_products = sorted(
        products_list,
        key=lambda p: p.total_value(),
        reverse=True
    )

    # Print formatted report
    print("\n" + "=" * 65)
    print("          GROCERY INVENTORY REPORT")
    print("     (sorted by total stock value - highest first)")
    print("=" * 65)
    print(f"{'Product':<22} {'Unit Price':>12} {'Qty':>6} {'Total Value':>14}")
    print("-" * 65)

    for product in sorted_products:
        print(product)

    print("-" * 65)

    # Optional: show grand total inventory value
    grand_total = sum(p.total_value() for p in sorted_products)
    print(f"{'Grand Total Inventory Value':<50} ${grand_total:>10,.2f}")
    print(f"\nProducts in stock: {len(sorted_products)}\n")


# ────────────────────────────────────────────────
#                     Run program
# ────────────────────────────────────────────────
if __name__ == "__main__":
    main()
