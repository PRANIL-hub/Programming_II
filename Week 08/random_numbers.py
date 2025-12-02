import random

quantity = int(input("How many random numbers: "))
maximum = int(input("Maximum number: "))

numbers = [random.randint(0, maximum) for _ in range(quantity)]
print("The numbers are:", numbers)

print("The minimum is", min(numbers))
print("The maximum is", max(numbers))

random_choice = random.choice(numbers)
print("A randomly chosen number is", random_choice)

reversed_numbers = numbers[::-1]
print("The numbers reversed are", reversed_numbers)

sorted_numbers = sorted(numbers)
print("The numbers sorted are", sorted_numbers)


