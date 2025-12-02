"""
def question_1
    DEFINE data_strings as a list of strings containing values with '=' and '%'

    FOR each string s in data_strings DO
        FIND the position of '=' in s and store as eq_index
        FIND the position of '%' in s and store as percent_index

        EXTRACT substring from s starting after eq_index up to before percent_index
        REMOVE any leading/trailing spaces from substring and store as number_str

        CONVERT number_str to a float and store as value
        PRINT value
    END FOR
END question_1

"""
def question_1():
    """
        Extracts and prints the numeric values as floats from a list of strings,
        where each string contains a value between '=' and '%' characters.
        """
    data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                    "Something else that's very important = 9.2%", "x = 42%"]

    for s in data_strings:
        # Find the index of '='
        eq_index = s.index('=')
        # Find the index of '%'
        percent_index = s.index('%')

        # Extract substring between '=' and '%', strip spaces
        number_str = s[eq_index + 1:percent_index].strip()

        value = float(number_str)
        print(value)

question_1()
"""
def question_2
    SET CURRENT_YEAR to 2025

    PROMPT user to enter DOB in "dd/mm/yyyy" format and store in dob

    SPLIT dob by '/' and get the last element as year_str
    CONVERT year_str to an integer birth_year

    CALCULATE age_next_year as (CURRENT_YEAR + 1) - birth_year

    PRINT "You were born in " + birth_year
    PRINT "You will turn " + age_next_year + " in " + (CURRENT_YEAR + 1)
END question_2
"""

def question_2():
    """
        Asks the user for their date of birth in 'dd/mm/yyyy' format,
        extracts the birth year, and calculates the user's age next year
        based on the current year constant.
        """
    CURRENT_YEAR = 2025

    dob = input("DOB (dd/mm/yyyy): ")

    # Extract the year (last part after last '/')
    year_str = dob.split('/')[-1]
    birth_year = int(year_str)

    age_next_year = CURRENT_YEAR + 1 - birth_year

    print(f"You were born in {birth_year}.")
    print(f"You will turn {age_next_year} in {CURRENT_YEAR + 1}.")
question_2()

"""
def question_3
    ask user to enter subject code and remove extra spaces

    WHILE subject_code is not blank DO
        SET discipline_code to first two characters of subject_code
        IF subject_code length > 2 THEN
            SET year_level_char to third character of subject_code
        ELSE
            SET year_level_char to empty string

        IF year_level_char is a digit THEN
            CONVERT year_level_char to integer year_level

            IF discipline_code equals "CP" THEN
                SET it_string to " IT"
            ELSE
                SET it_string to empty string

            IF year_level equals 1 THEN
                SET year_string to "first-year"
            ELSE IF year_level equals 2 THEN
                SET year_string to "second-year"
            ELSE IF year_level equals 3 THEN
                SET year_string to "third-year"
            ELSE
                SET year_string to "Masters or other"

            PRINT "That is a " + year_string + it_string + " subject."
        ELSE
            PRINT "Invalid subject code format."

        PROMPT user to enter subject code and remove extra spaces
    END WHILE
END question_3

"""
def question_3():
    """
       Continuously prompts the user to enter JCU subject codes until a blank entry is made.
       For each subject code, determines and prints the year level and whether it is an IT subject.
       Validates the subject code format and handles invalid inputs.
       """
    subject_code = input("Enter subject code: ").strip()

    while subject_code != "":
        discipline_code = subject_code[:2]
        year_level_char = subject_code[2] \
        if len(subject_code) > 2\
        else ""

        if year_level_char.isdigit():
            year_level = int(year_level_char)

            it_string = " IT" if discipline_code == "CP" else ""

            if year_level == 1:
                year_string = "first-year"
            elif year_level == 2:
                year_string = "second-year"
            elif year_level == 3:
                year_string = "third-year"
            else:
                year_string = "Masters or other"

            print(f"That is a {year_string}{it_string} subject.")

        else:
            print("Invalid subject code format.")

        subject_code = input("Enter subject code: ").strip()
question_3()