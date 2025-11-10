"""CP1404/CP5632 Practical 07
Guitar class example
"""

class Guitar:
    """Represent a guitar object."""

    def __init__(self, name, year, cost):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Compare guitars by year for sorting."""
        return self.year < other.year

    def is_vintage(self):
        """Return True if the guitar is 50 years or older."""
        return 2025 - self.year >= 50
