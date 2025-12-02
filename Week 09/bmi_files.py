def main():
    """Run the BMI program: get user input, save BMIs to file, then display categories."""
    filename = input("Filename: ")
    number_of_people = int(input("Enter the number of people: "))
    save_bmis(number_of_people, filename)
    print()
    display_bmi_categories(filename)

def calculate_bmi(weight, height):
    """Calculate and return BMI given weight (kg) and height (m)."""
    return weight / (height ** 2)

def save_bmis(number_of_people, filename):
    """
       Collect height and weight for a number of people, calculate BMI for each,
       and save each BMI value on its own line in the given filename.
       """
    with open(filename, 'w') as file:
        for i in range(1, number_of_people + 1):
            print(f"Person {i}")
            height = float(input("Enter height (m): "))
            weight = float(input("Enter weight (kg): "))
            bmi = calculate_bmi(weight, height)
            file.write(f"{bmi}\n")

def display_bmi_categories(filename):
    """
        Read BMI values from the given file and print each BMI with its weight category.
        Categories: underweight, normal, overweight, obese.
        """
    print("\nBMI Categories")
    with open(filename, 'r') as file:
        for line in file:
            bmi = float(line.strip())
            if bmi < 18.5:
                category = "underweight"
            elif bmi < 25:
                category = "normal"
            elif bmi < 30:
                category = "overweight"
            else:
                category = "obese"
            print(f"BMI {bmi:.1f}, considered {category}")
main()
