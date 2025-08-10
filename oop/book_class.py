# book_class.py

class Book:
    """
    Simple Book class demonstrating Python magic methods:
    - __init__: constructor
    - __del__: destructor (prints when object is deleted)
    - __str__: readable string for users
    - __repr__: official string representation that can recreate the object
    """

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Called when the object is garbage-collected; print title as required
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        # Friendly string representation
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        # Official representation that can be used to recreate the object
        return f"Book('{self.title}', '{self.author}', {self.year})"
