# Grocery Store Inventory Manager

A terminal-based Python program for managing and reporting on grocery store inventory. Enter product details interactively and get a clean, sorted report of your stock value.

---

## Features

- Interactive input for up to 3 grocery products
- Input validation with helpful error messages
- Calculates total stock value per product
- Sorts inventory by total value (highest to lowest)
- Displays a formatted summary report with grand total

---

## Sample Output

```
=== Grocery Inventory Manager ===
Enter details for 3 products

Product #1:
  Product name: Apple
  Price per unit ($): 0.99
  Quantity in stock: 150

Product #2:
  Product name: Milk
  Price per unit ($): 3.49
  Quantity in stock: 60

Product #3:
  Product name: Cheese
  Price per unit ($): 5.99
  Quantity in stock: 40

=================================================================
          GROCERY INVENTORY REPORT
     (sorted by total stock value - highest first)
=================================================================
Product                Unit Price    Qty     Total Value
-----------------------------------------------------------------
Cheese                  Price: $   5.99  Qty:   40  Total value: $    239.60
Milk                    Price: $   3.49  Qty:   60  Total value: $    209.40
Apple                   Price: $   0.99  Qty:  150  Total value: $    148.50
-----------------------------------------------------------------
Grand Total Inventory Value                        $    597.50

Products in stock: 3
```

---

## Usage

**Requirements:** Python 3.x — no external libraries needed.

Run with:

```bash
python grocery_inventory.py
```

You will be prompted to enter details for 3 products one at a time.

---

## Validation Rules

| Field | Rule |
|---|---|
| Product name | Cannot be empty or whitespace |
| Price per unit | Must be a positive number |
| Quantity | Must be a non-negative whole number |

Any invalid input triggers a clear error message and re-prompts — the program won't crash.

---

## Project Structure

```
Product (class)
├── __init__()      # Validates and stores name, price, and quantity
├── total_value()   # Returns price × quantity
└── __str__()       # Formats product row for the report

main()              # Handles input loop, sorting, and report output
```

---

## License

Free to use and modify.

