"""Program to classify score result."""

import random


def main():
    """Ask user for score, print result, then print result for random score."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f} is {determine_result(random_score)}")


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