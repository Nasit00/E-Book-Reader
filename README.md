# E-Book Store & Reader

This is a console-based Python application that simulates a simple e-book store. It allows users to browse books, purchase them, view transaction history, and read purchased books through a simple, built-in e-book reader.

[cite_start]This project demonstrates key Object-Oriented Programming (OOP) principles, including Abstraction, Inheritance, and Composition[cite: 15].

## :books: Features

* **List Books:** View all available books in the store.
* **Purchase Books:** "Purchase" a book, which registers the user and records the transaction.
* **View Transactions:** See a complete history of all book purchases.
* **List Users:** View all registered users.
* **Read E-Book:** If a user has purchased a book, they can read it in a console-based reader. The reader supports:
    * Opening the book to the first page.
    * Navigating to the next page.
    * Navigating to the previous page.
    * Closing the book.

## :computer: How to Run

1.  Ensure all `.py` files are in the same directory.
2.  Create the e-book content file named `python.txt` (or another name matching a purchased book title). The content should use `@@@` as a page separator.
3.  Run the main application from your terminal:
    ```bash
    python main.py
    ```
4.  Follow the on-screen menu prompts.

## :classical_building: OOP Concepts Demonstrated

* **Abstraction:** An abstract base class `Item` (`abcItem.py`) defines a common interface (`get_info`) that all item-like objects must implement.
* **Inheritance:** The `Book` and `User` classes both inherit from the abstract `Item` class, providing their own concrete implementations of `get_info`.
* **Composition:**
    * The `Store` class *has* a `BookList` and a `UserList`.
    * `BookList` *has* a list of `Book` objects.
    * `UserList` *has* a list of `User` objects.
* **Encapsulation:** Classes like `User` use properties (getters/setters) to control access to their attributes and enforce validation (e.g., ID must be a positive integer).

## :dividers: File Structure

```
E-Book Reader/
│
[cite_start]├─ abcItem.py      # Abstract Class (Abstraction) [cite: 15]
[cite_start]├─ user.py         # User class inherits Item(Inheritance) [cite: 15]
[cite_start]├─ userlist.py     # UserList has list of users(Composition) [cite: 15]
[cite_start]├─ book.py         # Book class inherits Item(Inheritance) [cite: 15]
[cite_start]├─ booklist.py     # BookList has list of books(Composition) [cite: 15]
[cite_start]├─ transaction.py  # Transaction class [cite: 15]
[cite_start]├─ purchase.py     # Purchase class [cite: 15]
[cite_start]├─ store.py        # Store class [cite: 15, 16]
├─ reader.py       # E-Book reader class
├─ app.py          # Main application menu and logic
[cite_start]└─ main.py         # Main menu program (Entry Point) [cite: 16]
```