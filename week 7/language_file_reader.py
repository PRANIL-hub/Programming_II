"""CP1404/CP5632 Practical 07
Reads programming languages from a CSV file and stores them in objects
"""

from programming_language import ProgrammingLanguage

def main():
    languages = load_languages("languages.csv")
    for language in languages:
        print(language)


def load_languages(filename):
    """Load programming languages from a CSV file."""
    languages = []
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split(',')
            name, typing, reflection_str, year, pointer_str = parts
            reflection = reflection_str == "Yes"
            pointer_arithmetic = pointer_str == "Yes"
            language = ProgrammingLanguage(name, typing, reflection, int(year), pointer_arithmetic)
            languages.append(language)
    return languages


if __name__ == '__main__':
    main()
