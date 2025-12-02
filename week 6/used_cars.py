"""Client program for car.py (used_cars)
"""
from car import Car


# existing example cars (if any) — add your own as needed
my_car = Car("MyCar", 20)
print(my_car)


# --- Modifications required by prac ---
# 1) Create a new Car object called "limo" initialised with 100 units of fuel.
limo = Car("Limo", 100)


# 2) Add 20 more units of fuel to this new car object using the add method.
# The method in this implementation is add_fuel()
limo.add_fuel(20)


# 3) Print the amount of fuel in the car.
print(f"Limo fuel after adding: {limo.fuel}")


# 4) Attempt to drive the car 115 km using the drive method.
km_driven, message = limo.drive(115)
print(message)


# 5) Print the car using __str__ to show final state
print(limo)