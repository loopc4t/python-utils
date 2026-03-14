# Dealership Commission Tracker

A lightweight Python program for tracking car sales and automatically calculating salesperson commissions based on tiered commission rules.

---

## Features

- Logs individual car sales with model, price, and salesperson
- Calculates commissions automatically using a tiered rate system
- Generates a formatted per-sale report
- Summarizes total commissions earned per salesperson

---

## Commission Rules

| Sale Price | Commission Rate |
|---|---|
| $50,000 or under | 8% |
| Over $50,000 | 10% (8% base + 2% bonus) |

---

## Sample Output

```
=== Individual Sales Report ===
--------------------------------------------------------------------------------
Car model: Kia K4           | Price: $    22,290.00 | Salesperson: Mike     | Commission: $  1,783.20
Car model: Honda Civic      | Price: $    26,490.00 | Salesperson: Brenda   | Commission: $  2,119.20
Car model: Honda Accord     | Price: $    30,980.00 | Salesperson: Mike     | Commission: $  2,478.40
Car model: Nissan Sentra    | Price: $    23,900.00 | Salesperson: Thomas   | Commission: $  1,912.00
Car model: Toyota RAV4      | Price: $    50,200.00 | Salesperson: Mike     | Commission: $  5,020.00
--------------------------------------------------------------------------------

=== Total Commissions by Salesperson ===
--------------------------------------------------
Salesperson: Brenda   → Total Commission: $  2,119.20
Salesperson: Mike     → Total Commission: $  9,281.60
Salesperson: Thomas   → Total Commission: $  1,912.00

Total sales processed: 5
```

---

## Usage

**Requirements:** Python 3.x — no external libraries needed.

Run directly with:

```bash
python dealership_tracker.py
```

To add sales, append a new `CarSale` entry to the `sales` list:

```python
CarSale("Ford Mustang", 62000, "Brenda")  # Over $50k — triggers bonus rate
```

---

## Project Structure

```
CarSale (class)
├── __init__()     # Stores car model, price, and salesperson
├── commission()   # Calculates commission based on tiered rules
└── __str__()      # Formats the sale for readable output

sales (list)       # Collection of CarSale instances
total_commissions  # Dict aggregating commissions per salesperson
```

---

## License

Free to use and modify.
