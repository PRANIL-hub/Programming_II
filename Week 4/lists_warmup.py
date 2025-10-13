"""
CP1404/CP5632 Practical - Lists "warm-up"
Suggested solution
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# What values do the following expressions have?
print(numbers[0])          # 3
print(numbers[-1])         # 2
print(numbers[3])          # 1
print(numbers[:-1])        # [3, 1, 4, 1, 5, 9]
print(numbers[3:4])        # [1]
print(5 in numbers)        # True
print(7 in numbers)        # False
print("3" in numbers)      # False
print(numbers + [6, 5, 3]) # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Modify the list as required
numbers[0] = "ten"
numbers[-1] = 1
print(numbers[2:])         # All elements except first two
print(9 in numbers)        # Check if 9 is an element
