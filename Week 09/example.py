filename = input("Enter filename: ").strip()

total = 0.0
count = 0

# Open the file for reading
in_file = open(filename, 'r')

for line in in_file:
    score = float(line)
    total += score
    count += 1

    print(f"Score = {score:6.1f}   Total so far = {total:7.1f}")
# Close the file after reading
in_file.close()

average = total / count

print(f"Average = {average:.1f}")