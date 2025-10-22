"""
CP1404/CP5632 Practical - State Names
"""

STATE_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

def main():
    print("Welcome to the State Name Lookup Program")
    state_code = input("Enter short state: ").strip().upper()
    while state_code != "":
        try:
            print(f"{state_code} is {STATE_NAMES[state_code]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").strip().upper()

    print("\nAll States:")
    for code, name in STATE_NAMES.items():
        print(f"{code:3} is {name}")

if __name__ == "__main__":
    main()
