"""
Wimbledon Data Processing
Estimate: 40 minutes
Actual:  minutes
"""

FILENAME = "wimbledon.csv"

def main():
    records = load_data(FILENAME)
    champion_to_count = count_champions(records)
    countries = extract_countries(records)

    print("Wimbledon Champions:")
    for champion, wins in champion_to_count.items():
        print(f"{champion:20} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

def load_data(filename):
    """Read data from the file into a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header
        records = [line.strip().split(",") for line in in_file]
    return records

def count_champions(records):
    """Count how many times each champion has won."""
    champion_to_count = {}
    for record in records:
        champion = record[2]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    return champion_to_count

def extract_countries(records):
    """Extract a set of unique countries from the data."""
    countries = {record[1] for record in records}
    return countries

if __name__ == "__main__":
    main()
