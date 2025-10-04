"""Program to get a valid password and print stars."""

MIN_LENGTH = 4  # you can change this


def main():
    """Get password and print stars."""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    """Get a password meeting the minimum length."""
    password = input(f"Enter a password (at least {min_length} characters): ")
    while len(password) < min_length:
        print("Password too short.")
        password = input(f"Enter a password (at least {min_length} characters): ")
    return password


def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print('*' * len(password))


main()