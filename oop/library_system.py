# library_system.py

class Book:
    """Base class for books with common attributes."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Digital book with file size in KB."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Physical book with a page count."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Composition: Library manages a collection of Book (and subclass) instances."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a Book (or subclass) instance to the library."""
        if not isinstance(book, Book):
            raise TypeError("add_book expects an instance of Book or its subclasses")
        self.books.append(book)

    def list_books(self):
        """Prints details of each book using each class's __str__ (polymorphism)."""
        for book in self.books:
            print(str(book))
