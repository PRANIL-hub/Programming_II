"""CP1401 - Practical 8 - Debugging."""

# Debug program 1 - friends' names
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(1, len(names)):
    print(f"{i}. {names[i]}")
last_number = len(names)
print(f"The last name (number {last_number}) is {names[last_number]}")
#
# # Problem(s) for program 1:
# # ?
# # in line 6 the range parameter does not includes last element of the list
# # Fixed code for program 1:
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(len(names)):
    print(f"{i+1}. {names[i]}")
last_number = len(names)
print(f"The last name (number {last_number}) is {names[last_number-1]}")



# Debug program 2 - title-casing country names
countries = ("australia", "new zeaLAND", "India")
for i in range(len(countries)):
    countries[i] = countries[i].title()
print(countries)  # country names should be in title-case now

# Problem(s) for program 2:
# ?
#elements cannot be assigned to a tuple like in line 27 countries[i]
# Fixed code for program 2:
countries = ("australia", "new zeaLAND", "India")
countries_list = list(countries)
for i in range(len(countries_list)):
    countries_list[i] = countries[i].title()
print(countries)  # country names should be in title-case now