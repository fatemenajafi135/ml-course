"""
Week 1 Homework: Library Management System
===========================================

Rules:
- Only built-in Python
- No external libraries
- Fill all parts with your own code

Goal:
Build a simple library system with basic book management features.

Object contract (this is what every method below must set up / rely on —
the classes only work together if everyone uses these exact attribute
names):

    Book instance:
        .title: str
        .author: str
        .year: int
        .available: bool   # True = can be borrowed, False = already out

    User instance:
        .name: str
        .borrowed_books: list[Book]   # books this user currently has out

    Library instance (already set up for you in __init__):
        .books: list[Book]
        .users: list[User]

Design note: Library.borrow_book / return_book take a user_name and a
book_title (strings from the menu, see run() below), then look up the
matching User/Book objects and delegate to User.borrow_book / Book.borrow.
Keep the "find the object" logic in Library, and the "change my own
state" logic in Book/User, don't reach into another object's internals
from the wrong class.
"""


# ------------------------------------------
# Book Class
# ------------------------------------------
class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        """Set self.title, self.author, self.year, and self.available.

        Args:
            title: e.g. "Clean Code"
            author: e.g. "Robert C. Martin"
            year: e.g. 2008

        A freshly created book must start as available (True), nobody
        has borrowed it yet.

        WORKED EXAMPLE, this one is done for you. Use it as the pattern
        (signature, docstring, TODO -> real code) for every method below.
        """
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self) -> bool:
        """Mark the book as borrowed, if it's available.

        Returns:
            True and sets self.available = False, if the book was available.
            False (and leaves state unchanged), if it was already borrowed.
        """
        # TODO
        pass

    def return_book(self) -> None:
        """Mark the book as available again.

        Returns:
            None. Sets self.available = True.
        """
        # TODO
        pass

    def display(self) -> None:
        """Print the book's info on one line.

        Returns:
            None. e.g.:
            Clean Code by Robert C. Martin (2008) - Available
        """
        # TODO
        pass


# ------------------------------------------
# User Class
# ------------------------------------------
class User:
    def __init__(self, name: str) -> None:
        """Set self.name and self.borrowed_books (start empty).

        Args:
            name: e.g. "Alice"
        """
        # TODO
        pass

    def borrow_book(self, book: Book) -> bool:
        """Try to borrow `book`; track it if successful.

        Args:
            book: a Book instance (not just a title string).
                  Call book.borrow()  don't set book.available directly.

        Returns:
            True and appends `book` to self.borrowed_books, if book.borrow()
            succeeded.
            False, if the book was already unavailable.
        """
        # TODO
        pass

    def return_book(self, book: Book) -> None:
        """Return a book this user previously borrowed.

        Args:
            book: a Book instance that should currently be in
                  self.borrowed_books. Call book.return_book() and remove
                  it from the list.

        Returns:
            None.
        """
        # TODO
        pass

    def display(self) -> None:
        """Print the user's name and how many books they currently have out.

        Returns:
            None. e.g.:
            Alice (2 books borrowed)
        """
        # TODO
        pass


# ------------------------------------------
# Library Class
# ------------------------------------------
class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []
        self.users: list[User] = []

    # ---------- Book Management ----------

    def add_book(self, book: Book) -> None:
        """Add a Book object to self.books.

        Args:
            book: a Book instance (already constructed by the caller).

        Returns:
            None.
        """
        # TODO
        pass

    def remove_book(self, title: str) -> None:
        """Remove the book with this title from self.books, if present.

        Args:
            title: e.g. "Clean Code". If no book matches, do nothing
                   (don't raise an error).

        Returns:
            None.
        """
        # TODO
        pass

    def search_book(self, title: str) -> Book | None:
        """Find the book with this title.

        Args:
            title: e.g. "Clean Code"

        Returns:
            The matching Book instance, or None if not found.
        """
        # TODO
        pass

    def show_all_books(self) -> None:
        """Print every book in the library (call book.display() on each).

        Returns:
            None.
        """
        # TODO
        pass

    def show_available_books(self) -> None:
        """Print only the books where available is True.

        Returns:
            None.
        """
        # TODO
        pass

    # ---------- User Management ----------

    def add_user(self, user: User) -> None:
        """Add a User object to self.users.

        Args:
            user: a User instance (already constructed by the caller).

        Returns:
            None.
        """
        # TODO
        pass

    def search_user(self, name: str) -> User | None:
        """Find the user with this name.

        Args:
            name: e.g. "Alice"

        Returns:
            The matching User instance, or None if not found.
        """
        # TODO
        pass

    # ---------- Borrow / Return ----------

    def borrow_book(self, user_name: str, book_title: str) -> None:
        """Look up the user and book by name/title, then borrow.

        Args:
            user_name: e.g. "Alice" passed to search_user.
            book_title: e.g. "Clean Code" passed to search_book.

        Returns:
            None. Should print a message for each outcome:
            - user or book not found
            - book already unavailable
            - success (delegate the actual borrowing to
              user.borrow_book(book), don't reimplement the logic here)
        """
        # TODO
        pass

    def return_book(self, user_name: str, book_title: str) -> None:
        """Look up the user and book by name/title, then return.

        Args:
            user_name: e.g. "Alice" passed to search_user.
            book_title: e.g. "Clean Code" passed to search_book.

        Returns:
            None. Print a message if user/book not found; otherwise
            delegate to user.return_book(book).
        """
        # TODO
        pass

    # ---------- File Handling ----------

    def save_books(self, filename: str) -> None:
        """Save self.books to a file, one book per record.

        Args:
            filename: e.g. "library.json". Use the built-in `json` module
                      to write a list of dicts, each with keys
                      "title", "author", "year", "available".

        Returns:
            None.
        """
        # TODO
        pass

    def load_books(self, filename: str) -> None:
        """Load books from a file previously written by save_books.

        Args:
            filename: e.g. "library.json". Read the JSON list of dicts
                      and rebuild Book instances from it, replacing (or
                      extending, your choice, but be consistent)
                      self.books.

        Returns:
            None.
        """
        # TODO
        pass


# ------------------------------------------
# User Interface
# ------------------------------------------
def print_menu():
    print("\n========== Library Management ==========")
    print("Available commands:")
    print("  add_book")
    print("  remove_book")
    print("  search_book")
    print("  show_all_books")
    print("  show_available_books")
    print("  add_user")
    print("  search_user")
    print("  borrow_book")
    print("  return_book")
    print("  save_books")
    print("  load_books")
    print("  exit")


def run(library):
    while True:
        print_menu()

        command = input("\nCommand: ").strip().lower()

        match command:

            case "add_book":
                title = input("Title: ")
                author = input("Author: ")
                year = int(input("Year: "))

                book = Book(title, author, year)
                library.add_book(book)

            case "remove_book":
                title = input("Title: ")
                library.remove_book(title)

            case "search_book":
                title = input("Title: ")
                result = library.search_book(title)

                if result:
                    result.display()
                else:
                    print("Book not found.")

            case "show_all_books":
                library.show_all_books()

            case "show_available_books":
                library.show_available_books()

            case "add_user":
                name = input("User name: ")

                user = User(name)
                library.add_user(user)

            case "search_user":
                name = input("User name: ")
                result = library.search_user(name)

                if result:
                    result.display()
                else:
                    print("User not found.")

            case "borrow_book":
                user_name = input("User name: ")
                book_title = input("Book title: ")

                library.borrow_book(user_name, book_title)

            case "return_book":
                user_name = input("User name: ")
                book_title = input("Book title: ")

                library.return_book(user_name, book_title)

            case "save_books":
                filename = input("File name: ")
                library.save_books(filename)

            case "load_books":
                filename = input("File name: ")
                library.load_books(filename)

            case "exit":
                print("Goodbye!")
                break

            case _:
                print("Unknown command.")


# ------------------------------------------
# Main
# ------------------------------------------
if __name__ == "__main__":

    # Create a library
    library = Library()

    # Create some books
    clean_code = Book("Clean Code", "Robert C. Martin", 2008)
    python_crash_course = Book("Python Crash Course", "Eric Matthes", 2023)

    # Create a user
    alice = User("Alice")

    # Add data to the library
    library.add_book(clean_code)
    library.add_book(python_crash_course)
    library.add_user(alice)

    # Example method calls
    library.show_all_books()
    library.search_book("Clean Code")

    # Start the application
    run(library)
