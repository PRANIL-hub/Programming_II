"""CP1404/CP5632 Practical 07
Read, display, add, and save guitars
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Main program."""
    guitars = load_guitars(FILENAME)
    display_guitars(guitars)

    print("\nAdd new guitars:")
    guitars += get_new_guitars()

    guitars.sort()
    display_guitars(guitars, "Sorted Guitars")

    save_guitars(FILENAME, guitars)
    print(f"\nGuitars saved to {FILENAME}")


def load_guitars(filename):
    """Load guitars from a file."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name, year, cost = parts
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def get_new_guitars():
    """Prompt user to enter new guitars."""
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to a file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def display_guitars(guitars, heading="Guitars"):
    """Display all guitars."""
    print(f"\n{heading}:")
    for guitar in guitars:
        print(guitar)


if __name__ == '__main__':
    main()
