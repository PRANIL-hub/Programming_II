"""
def question_4():
    OPEN the file "name.txt" for reading AS in_file
    READ the entire content of in_file INTO text
    STRIP whitespace and newlines from text
    CLOSE in_file
    PRINT "Greetings " + text + "!"
END FUNCTION

CALL question_4()

"""
def question_4():
    """
        Reads the content of 'name.txt', strips whitespace/newlines,
        and greets the user with the read name.
        """
    in_file = open("name.txt", "r")
    text = in_file.read().strip()  # .strip() removes any newline or extra spaces
    in_file.close()
    print(f"Greetings {text}!")
question_4()

"""
def question_5():
ask the user to enter the filename
ask the user to enter the threshold (as a float)

Open the file for reading
Set total_count to 0
Set greater_count to 0

For each line in the file:
    Convert line to float
    Increment total_count
    If number > threshold:
        Increment greater_count
Close the file
Calculate percentage = (greater_count / total_count) * 100
Print the number of values greater than threshold with percentage and total"""


def question_5():
    """
        Reads a user-specified file containing floating-point numbers (one per line),
        then counts and reports how many values are greater than a user-specified threshold,
        along with the percentage.
        """
    filename = input("Filename: ").strip()
    threshold = float(input("Threshold: "))

    print("Processing...")

    in_file = open(filename, 'r')
    total_count = 0
    greater_count = 0

    for line in in_file:
        number = float(line)
        total_count += 1
        if number > threshold:
            greater_count += 1

    in_file.close()

    percentage = (greater_count / total_count) * 100
    print(
        f"{greater_count} out of {total_count} ({percentage:.1f}%) values in {filename} are greater than {threshold}.")
question_5()

"""def question_6
    ask user for input_filename
    ask user for output_filename
    ask user for search_string

    OPEN input_filename for reading AS in_file
    OPEN output_filename for writing AS out_file

    FOR each line IN in_file
        IF search_string IS IN line THEN
            WRITE line TO out_file
        END IF
    END FOR

    CLOSE in_file
    CLOSE out_file

    PRINT confirmation message with search_string and output_filename
END FUNCTION

CALL question_6
"""
def question_6():
    """
        Asks for an input file, output file, and search string.
        Copies lines from the input file to the output file only if they contain the search string.
        """
    input_filename = input("Input file name: ").strip()
    output_filename = input("Output file name: ").strip()
    search_string = input("Search string: ").strip()

    in_file = open(input_filename, 'r')
    out_file = open(output_filename, 'w')

    for line in in_file:
        if search_string in line:
            out_file.write(line)

    in_file.close()
    out_file.close()

    print(f"Lines containing '{search_string}' were written to '{output_filename}'.")
question_6()
