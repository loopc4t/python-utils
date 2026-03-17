class Product:
    """Grocery product with price, stock quantity, and total value calculation."""

    def __init__(self, name, price_per_unit, quantity):
        """
        Args:
            name (str): Product name.
            price_per_unit (float): Price per unit (must be positive).
            quantity (int): Units in stock (must be non-negative).
        """
        if not name.strip():
            raise ValueError("Product name cannot be empty")
        if price_per_unit <= 0:
            raise ValueError(f"Price must be positive. Got {price_per_unit} for {name}")
        if quantity < 0:
            raise ValueError(f"Quantity cannot be negative. Got {quantity} for {name}")

        self.name = name.strip()
        self.price_per_unit = float(price_per_unit)
        self.quantity = int(quantity)

    def total_value(self):
        """Stock value for this product: price × quantity."""
        return self.price_per_unit * self.quantity

    def __str__(self):
        """Formatted row for the inventory report."""
        return (
            f"{self.name:<20} "
            f"Price: ${self.price_per_unit:>7.2f}  "
            f"Qty: {self.quantity:>4}  "
            f"Total value: ${self.total_value():>10,.2f}"
        )


def collect_products(count=3):
    """Prompt the user to enter `count` products and return them as a list."""
    print("=== Grocery Inventory Manager ===")
    print(f"Enter details for {count} products\n")

    products = []

    for i in range(1, count + 1):
        print(f"Product #{i}:")
        while True:
            try:
                name = input("  Product name: ").strip()
                if not name:
                    print("  Name cannot be empty. Try again.")
                    continue

                price = float(input("  Price per unit ($): ").strip())
                qty = int(input("  Quantity in stock: ").strip())

                products.append(Product(name, price, qty))
                print()
                break

            except ValueError as e:
                # Distinguish conversion errors from our own validation errors
                if "could not convert" in str(e):
                    print("  Invalid number. Please enter valid numbers.\n")
                else:
                    print(f"  Error: {e}\n")

    return products


def print_report(products):
    """Print products sorted by total stock value, highest first."""
    sorted_products = sorted(products, key=lambda p: p.total_value(), reverse=True)
    grand_total = sum(p.total_value() for p in sorted_products)

    print("\n" + "=" * 65)
    print("          GROCERY INVENTORY REPORT")
    print("     (sorted by total stock value - highest first)")
    print("=" * 65)
    print(f"{'Product':<22} {'Unit Price':>12} {'Qty':>6} {'Total Value':>14}")
    print("-" * 65)

    for product in sorted_products:
        print(product)

    print("-" * 65)
    print(f"{'Grand Total Inventory Value':<50} ${grand_total:>10,.2f}")
    print(f"\nProducts in stock: {len(sorted_products)}\n")


def main():
    products = collect_products()
    if products:
        print_report(products)
    else:
        print("No valid products entered. Exiting.")


if __name__ == "__main__":
    main()
