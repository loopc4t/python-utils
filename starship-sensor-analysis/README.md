# Starship Sensor Analysis

A terminal-based Python program that simulates a starship's sensor system — input detected celestial bodies, and get a formatted analysis report sorted by volume.

---

## Features

- Interactive input for 3 detected space objects
- Input validation with re-prompting on invalid entries
- Calculates circular scan area (2D projection) and spherical volume per object
- Sorts results by volume, largest to smallest
- Displays a clean, aligned sensor report

---

## Calculations

| Metric             | Formula      |
| ------------------ | ------------ |
| Circular Scan Area | π × r²       |
| Object Volume      | 4/3 × π × r³ |

Radius can be in any consistent unit (km, AU, etc.) — units are not enforced.

---

## Sample Output

```
=== Space Object Scanner ===
Enter data for 3 detected celestial objects

Object #1:
  Name: Mars
  Radius: 3389.5

Object #2:
  Name: Europa
  Radius: 1560.8

Object #3:
  Name: Ceres
  Radius: 476.2

======================================================================
     SPACE OBJECTS SORTED BY VOLUME (largest to smallest)
======================================================================
Name                    Radius       Scan Area           Volume
----------------------------------------------------------------------
Mars               Radius:  3389.50  Scan area: 36,117,547.45  Volume: 163,115,017,200.56
Europa             Radius:  1560.80  Scan area:  7,655,984.23  Volume:  15,931,009,173.20
Ceres              Radius:   476.20  Scan area:    712,521.66  Volume:    451,810,847.23
----------------------------------------------------------------------
Total objects processed: 3
```

---

## Usage

**Requirements:** Python 3.x — uses only the built-in `math` module.

Run with:

```bash
python starship_sensor.py
```

You'll be prompted to enter a name and radius for each of 3 detected objects.

---

## Validation Rules

| Field  | Rule                          |
| ------ | ----------------------------- |
| Name   | Cannot be empty or whitespace |
| Radius | Must be a positive number     |

Invalid entries re-prompt without crashing the program.

---

## Project Structure

```
SpaceObject (class)
├── __init__()          # Validates and stores name and radius
├── circular_scan()     # Returns π × r²
├── object_volume()     # Returns 4/3 × π × r³
└── __str__()           # Formats object row for the report

main()                  # Handles input loop, sorting, and report output
```

---

## License

Free to use and modify.
