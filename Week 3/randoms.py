"""
CP1404/CP5632 - Practical
Randoms
Demonstrate the use of random number generation functions.
"""

import random

# Line 1: Random integer between 5 and 20 inclusive
print("Random integer between 5 and 20:", random.randint(5, 20))
# Smallest possible: 5, Largest possible: 20

# Line 2: Random number between 3 and 10 with step of 2 (i.e. 3, 5, 7, or 9)
print("Random number between 3 and 10 with step 2:", random.randrange(3, 10, 2))
# Possible outcomes: 3, 5, 7, 9
# Smallest possible: 3, Largest possible: 9

# Line 3: Random floating-point number between 2.5 and 5.5
print("Random float between 2.5 and 5.5:", random.uniform(2.5, 5.5))
# Smallest possible: slightly more than 2.5, Largest possible: slightly less than 5.5
