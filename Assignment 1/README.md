# CP1404 Assignment 1 – Books to Read 1.0  
_By Pranil Dhakal_

##  About the Program
This program is an **interactive book list manager** that allows users to:
- View all books (sorted by author and title)
- Add new unread books
- Mark unread books as completed
- Save their progress to a CSV file

The program helps users track the books they want to read and those they have finished.  
It uses **functions**, **lists**, **file I/O**, and **error checking**, following the **CP1404 coding standards**.

---

##  Features
- Reads book data from `books.csv` at startup
- Displays books neatly aligned, marking unread books with a `*`
- Allows users to add and complete books with full validation
- Saves all changes to `books.csv` on exit
- Handles invalid inputs gracefully using exception handling

---

##  Sample `books.csv`
```csv
Developing the Leader Within You,John Maxwell,225,u
The 360 Degree Leader,John Maxwell,369,c
In Search of Lost Time,Marcel Proust,93,u
Starting Out with Python,Tony Gaddis,744,c
