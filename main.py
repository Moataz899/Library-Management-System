class Person:
    def __init__(self):
        while True:
            self.name = str(input("Please Enter Your Name: "))
            if len(self.name) > 0 and all(c.isalpha() or c.isspace() for c in self.name):
                break
            else:
                print("Please enter a valid name (letters only and non-empty).")
        
        while True:
            self.email = str(input("Please Enter Your Email: ").strip())
            if "@" in self.email and len(self.email) > 0:
                break
            else:
                print("Please enter a valid email (must contain '@' and non-empty).")

        while True:
            try:
                self.phoneNumber = int(input("Please Enter Your Phone Number: "))
                break
            except ValueError:
                print("Please enter a valid phone number (digits only).")

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Phone Number: {self.phoneNumber}")

class Librarian(Person):
    def __init__(self):
        super().__init__()
        self.libraryId = input("Please Enter Your Library ID: ")

    def display_info(self):
        print(f"Librarian Info: Name: {self.name}, Email: {self.email}, Phone Number: {self.phoneNumber}, Library ID: {self.libraryId}")
        print("//" * 15)

    def add_book(self, library, book):
        if book not in library.books:
            library.books.append(book)
            print(f"Book '{book.title}' added.")
        else:
            print(f"Book '{book.title}' already exists.")

    def remove_book(self, library, book):
        if book in library.books:
            library.books.remove(book)
            if book in library.borrowed_books:
                library.borrowed_books.remove(book)
            print(f"Book '{book.title}' removed.")
        else:
            print(f"Book '{book.title}' not found.")

    def add_member(self, library, member):
        if member not in library.members:
            library.members.append(member)
            print(f"Member '{member.name}' added.")
        else:
            print(f"Member '{member.name}' already exists.")

    def remove_member(self, library, member):
        if member in library.members:
            library.members.remove(member)
            print(f"Member '{member.name}' removed.")
        else:
            print(f"Member '{member.name}' not found.")

    def display_books(self, library):
        print("Library Books:")
        library.display_books()
        print("//" * 15)

    def display_members(self, library):
        print("Library Members:")
        library.display_members()
        print("//" * 15)

class Member(Person):
    def __init__(self):
        super().__init__()
        self.memberId = input("Please Enter Your Member ID: ").strip()
        self.borrowed_books = []

    def display_info(self):
        print(f"Member Info: Name: {self.name}, Email: {self.email}, Phone Number: {self.phoneNumber}, Member ID: {self.memberId}")
        
    def borrow_book(self, library, book):
        if book in library.books and book.available:
            if book not in self.borrowed_books:
                book.available = False
                self.borrowed_books.append(book)
                library.borrowed_books.append(book)  
                print(f"Book '{book.title}' borrowed.")
            else:
                print(f"Book '{book.title}' already borrowed.")
        else:
            print(f"Book '{book.title}' not available.")

    def return_book(self, library, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            library.borrowed_books.remove(book)
            print(f"Book '{book.title}' returned.")
        else:
            print(f"You haven't borrowed '{book.title}'.")

    def display_borrowed_books(self):
        if not self.borrowed_books:
            print("No borrowed books.")
        else:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                book.display_info()
        print("//" * 15)

class Book:
    def __init__(self, title, author, isbn):
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip()
        self.available = True

    def display_info(self):
        availability = "Available" if self.available else "Not Available"
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Availability: {availability}")

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_books = []
        self.returned_books = []

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display_info()

    def display_members(self):
        if not self.members:
            print("No members in the library.")
        else:
            for member in self.members:
                member.display_info()

    def display_borrowed_books(self):
        if not self.borrowed_books:
            print("No borrowed books.")
        else:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                book.display_info()

    def display_returned_books(self):
        if not self.returned_books:
            print("No returned books.")
        else:
            print("Returned Books:")
            for book in self.returned_books:
                book.display_info()

    def search_books(self, title=None, author=None):
        found_books = [book for book in self.books if 
                       (title and title.lower() in book.title.lower()) or 
                       (author and author.lower() in book.author.lower())]
        if not found_books:
            print("No books found.")
        else:
            print("Search Results:")
            for book in found_books:
                book.display_info()

    def filter_borrowed_books_by_member(self, member):
        borrowed_books = [book for book in self.borrowed_books if book in member.borrowed_books]
        if not borrowed_books:
            print(f"No books borrowed by member '{member.name}'.")
        else:
            print(f"Books borrowed by member '{member.name}':")
            for book in borrowed_books:
                book.display_info()

library = Library()

librarian1 = Librarian()
librarian1.display_info()

book1 = Book("Python", "John Doe", "123")
book2 = Book("Java", "Jane Smith", "456")
book3 = Book("C++", "Alice Johnson", "789")
book4 = Book("R", "Robert Brown", "101112")

librarian1.add_book(library, book1)
librarian1.add_book(library, book2)
librarian1.add_book(library, book3)
librarian1.add_book(library, book4)

librarian1.display_books(library)

librarian1.remove_book(library, book4)
librarian1.display_books(library)

member1 = Member()
member2 = Member()

librarian1.add_member(library, member1)
librarian1.add_member(library, member2)
librarian1.display_members(library)

librarian1.remove_member(library, member2)
librarian1.display_members(library)

member3 = Member()
member3.display_info()

member3.borrow_book(library, book2)

library.display_borrowed_books()

member3.return_book(library, book2)
library.display_returned_books()

library.display_members()

library.search_books(title="Python")
library.search_books(author="Jane Smith")

library.filter_borrowed_books_by_member(member3)
