"""
CP1404/CP5632 Assignment 1 - Books to Read 1.0
Student Name: Pranil Dhakal
Description:
An interactive book list program that lets users manage books to read and mark completed ones.
"""

import csv

# Constants
FILENAME = "books.csv"
STATUS_UNREAD = "u"
STATUS_COMPLETED = "c"


def main():
    """Main function to run the Books To Read program."""
    print("Books To Read 1.0 by Pranil Dhakal")
    books = load_books(FILENAME)
    print(f"{len(books)} books loaded.")

    while True:
        print_menu()
        choice = input(">>> ").strip().lower()
        if choice == "d":
            display_books(books)
        elif choice == "a":
            add_book(books)
        elif choice == "c":
            complete_book(books)
        elif choice == "q":
            save_books(FILENAME, books)
            print(f"{len(books)} books saved to {FILENAME}")
            print('"So many books, so little time. Frank Zappa"')
            break
        else:
            print("Invalid menu choice")


def print_menu():
    """Display the main menu."""
    print("\nMenu:")
    print("D - Display books")
    print("A - Add a new book")
    print("C - Complete a book")
    print("Q - Quit")


def load_books(filename):
    """Load books from the CSV file into a list of lists."""
    books = []
    try:
        with open(filename, "r", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            for row in reader:
                row[2] = int(row[2])  # convert pages to integer
                books.append(row)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty book list.")
    return books


def save_books(filename, books):
    """Save the list of books back to the CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for book in books:
            writer.writerow(book)


def display_books(books):
    """Display all books, sorted by author then title."""
    if not books:
        print("No books found.")
        return

    books.sort(key=lambda b: (b[1], b[0]))  # sort by author then title
    unread_books = [book for book in books if book[3] == STATUS_UNREAD]
    total_pages_unread = sum(book[2] for book in unread_books)

    title_width = max(len(book[0]) for book in books)
    author_width = max(len(book[1]) for book in books)

    for i, book in enumerate(books, start=1):
        star = "*" if book[3] == STATUS_UNREAD else " "
        print(f"{star}{i}. {book[0]:<{title_width}} by {book[1]:<{author_width}}  {book[2]:>3} pages")

    if unread_books:
        print(f"You still need to read {total_pages_unread} pages in {len(unread_books)} books.")
    else:
        print("No books left to read. Why not add a new book?")


def add_book(books):
    """Add a new unread book to the list."""
    title = get_non_empty_string("Title: ")
    author = get_non_empty_string("Author: ")
    pages = get_positive_int("Number of Pages: ")

    new_book = [title, author, pages, STATUS_UNREAD]
    books.append(new_book)
    print(f"{title} by {author} ({pages} pages) added.")


def complete_book(books):
    """Mark a book as completed."""
    unread_books = [book for book in books if book[3] == STATUS_UNREAD]
    if not unread_books:
        print("No unread books - well done!")
        return

    display_books(books)
    while True:
        try:
            choice = input("Enter the number of a book to mark as completed\n>>> ")
            book_number = int(choice)
            if book_number <= 0:
                print("Number must be > 0")
                continue
            if book_number > len(books):
                print("Invalid book number")
                continue

            selected_book = books[book_number - 1]
            if selected_book[3] == STATUS_COMPLETED:
                print("That book is already completed")
            else:
                selected_book[3] = STATUS_COMPLETED
                print(f"{selected_book[0]} by {selected_book[1]} completed!")
            break
        except ValueError:
            print("Invalid input - please enter a valid number")


def get_non_empty_string(prompt):
    """Prompt the user for a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input can not be blank")


def get_positive_int(prompt):
    """Prompt the user for a positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Number must be > 0")
        except ValueError:
            print("Invalid input - please enter a valid number")


if __name__ == "__main__":
    main()
