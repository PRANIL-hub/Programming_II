"""
Program to determine score status.
0–49 = Bad
50–89 = Passable
90–100 = Excellent
Anything else = Invalid
"""

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
