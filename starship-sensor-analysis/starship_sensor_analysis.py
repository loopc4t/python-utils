import math


class SpaceObject:
    """
    Represents a spherical space object (planet, moon, asteroid, etc.)
    with basic geometric calculations.
    """

    def __init__(self, name, radius):
        """
        Initialize a space object.

        Args:
            name (str): Name of the celestial body
            radius (float): Radius in arbitrary units (e.g. km)
                           Must be positive.
        """
        if radius <= 0:
            raise ValueError(
                f"Radius must be positive. Got {radius} for {name}")

        self.name = name.strip()          # Remove accidental leading/trailing spaces
        self.radius = float(radius)       # Ensure it's a float

    def circular_scan(self):
        """
        Calculate the area of a circular scan (projection) of the object.
        This is simply the area of a circle with the object's radius.

        Returns:
            float: Area in square units (π × r²)
        """
        return math.pi * (self.radius ** 2)

    def object_volume(self):
        """
        Calculate the volume of the spherical object.

        Returns:
            float: Volume in cubic units (4/3 × π × r³)
        """
        return (4 / 3) * math.pi * (self.radius ** 3)

    def __str__(self):
        """
        Human-readable string representation.
        Formats numbers nicely with 2 decimal places.
        """
        scan_area = self.circular_scan()
        volume = self.object_volume()

        return (
            f"{self.name:<18} "
            f"Radius: {self.radius:>8.2f}  "
            f"Scan area: {scan_area:>12,.2f}  "
            f"Volume: {volume:>14,.2f}"
        )


def main():
    """
    Main program flow:
    - Collects 3 space objects from user
    - Sorts them by volume (largest to smallest)
    - Prints formatted report
    """
    print("=== Space Object Scanner ===")
    print("Enter data for 3 detected celestial objects\n")

    obj_list = []

    for i in range(1, 4):
        print(f"Object #{i}:")
        while True:
            try:
                name = input("  Name: ").strip()
                if not name:
                    print("  Name cannot be empty. Try again.")
                    continue

                radius_input = input("  Radius: ").strip()
                radius = float(radius_input)

                if radius <= 0:
                    print("  Radius must be positive. Try again.")
                    continue

                obj = SpaceObject(name, radius)
                obj_list.append(obj)
                print()  # blank line between objects
                break

            except ValueError:
                print("  Invalid number. Please enter a valid positive number.\n")

    if not obj_list:
        print("No valid objects entered. Exiting.")
        return

    # Sort by volume descending (largest first)
    sorted_objects = sorted(
        obj_list, key=lambda obj: obj.object_volume(), reverse=True)

    # Print header
    print("\n" + "=" * 70)
    print("     SPACE OBJECTS SORTED BY VOLUME (largest to smallest)")
    print("=" * 70)
    print(f"{'Name':<18} {'Radius':>10}  {'Scan Area':>14}  {'Volume':>16}")
    print("-" * 70)

    # Print each object
    for obj in sorted_objects:
        print(obj)

    print("-" * 70)
    print(f"Total objects processed: {len(sorted_objects)}\n")


# ────────────────────────────────────────────────
#                     Run program
# ────────────────────────────────────────────────
if __name__ == "__main__":
    main()
