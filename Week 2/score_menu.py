"""Menu-driven score program."""

def main():
    """Run the score menu program."""
    score = get_valid_score()
    choice = ''
    while choice != 'Q':
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input(">>> ").upper()
        if choice == 'G':
            score= get_valid_score()
        elif choice == 'P':
            print(determine_result(score))
        elif choice == 'S':
            print('*' * int(score))
        elif choice == 'Q':
            print("Farewell.")
        else:
            print("Invalid choice")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score


def determine_result(score):
    """Determine the result based on score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()