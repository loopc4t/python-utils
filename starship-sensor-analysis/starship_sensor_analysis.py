import math


class SpaceObject:
    """Spherical celestial body with geometric calculations (volume, scan area)."""

    def __init__(self, name, radius):
        """
        Args:
            name (str): Name of the celestial body.
            radius (float): Radius in km (must be positive).
        """
        if radius <= 0:
            raise ValueError(f"Radius must be positive. Got {radius} for {name}")

        self.name = name.strip()
        self.radius = float(radius)

    def circular_scan(self):
        """Cross-sectional area of the object: π × r²."""
        return math.pi * (self.radius ** 2)

    def object_volume(self):
        """Volume of the sphere: 4/3 × π × r³."""
        return (4 / 3) * math.pi * (self.radius ** 3)

    def __str__(self):
        """Formatted row for the report table."""
        return (
            f"{self.name:<18} "
            f"Radius: {self.radius:>8.2f}  "
            f"Scan area: {self.circular_scan():>12,.2f}  "
            f"Volume: {self.object_volume():>14,.2f}"
        )


def collect_objects(count=3):
    """Prompt the user to enter `count` space objects and return them as a list."""
    print("=== Space Object Scanner ===")
    print(f"Enter data for {count} detected celestial objects\n")

    objects = []

    for i in range(1, count + 1):
        print(f"Object #{i}:")
        while True:
            try:
                name = input("  Name: ").strip()
                if not name:
                    print("  Name cannot be empty. Try again.")
                    continue

                radius = float(input("  Radius: ").strip())
                if radius <= 0:
                    print("  Radius must be positive. Try again.")
                    continue

                objects.append(SpaceObject(name, radius))
                print()
                break

            except ValueError:
                print("  Invalid number. Please enter a valid positive number.\n")

    return objects


def print_report(objects):
    """Print objects sorted by volume, largest first."""
    sorted_objects = sorted(objects, key=lambda o: o.object_volume(), reverse=True)

    print("\n" + "=" * 70)
    print("     SPACE OBJECTS SORTED BY VOLUME (largest to smallest)")
    print("=" * 70)
    print(f"{'Name':<18} {'Radius':>10}  {'Scan Area':>14}  {'Volume':>16}")
    print("-" * 70)

    for obj in sorted_objects:
        print(obj)

    print("-" * 70)
    print(f"Total objects processed: {len(sorted_objects)}\n")


def main():
    objects = collect_objects()
    if objects:
        print_report(objects)
    else:
        print("No valid objects entered. Exiting.")


if __name__ == "__main__":
    main()
