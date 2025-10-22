"""
Emails
Estimate: 25 minutes
Actual:  minutes
"""

def main():
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation != "" and confirmation != "y":
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    print("\nStored details:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    """Extract name from email address."""
    prefix = email.split('@')[0]
    parts = prefix.replace('.', ' ').split()
    name = " ".join(parts).title()
    return name

if __name__ == "__main__":
    main()
