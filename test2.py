class Person:
    def __init__(self):
        while True:
            self.name = input("Please Enter Your Name: ")
            if len(self.name) > 0 and all(c.isalpha() or c.isspace() for c in self.name):
                break
            else:
                print("Please enter a valid name (letters only and non-empty).")
        
        while True:
            self.email = input("Please Enter Your Email: ").strip()
            if "@" in self.email and len(self.email) > 0:
                break
            else:
                print("Please enter a valid email (must contain '@' and non-empty).")
        
        self.password = input("Please Enter Your Password: ").strip()

        while True:
            try:
                self.phoneNumber = int(input("Please Enter Your Phone Number: "))
                break
            except ValueError:
                print("Please enter a valid phone number (digits only).")

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Phone Number: {self.phoneNumber}")

class SignUp:
    def __init__(self, library):
        self.library = library

    def register_person(self):
        while True:
            user_type = input("Are you a Librarian or a Member? (Enter 'Librarian' or 'Member'): ").strip().lower()
            if user_type not in ['librarian', 'member']:
                print("Invalid input. Please enter 'Librarian' or 'Member'.")
                continue

            if user_type == 'librarian':
                new_librarian = Librarian()
                self.library.librarians.append(new_librarian)
                print("Librarian registered successfully.")
                return new_librarian

            if user_type == 'member':
                new_member = Member()
                self.library.members.append(new_member)
                print("Member registered successfully.")
                return new_member

class SignIn:
    def __init__(self, library):
        self.library = library

    def authenticate(self):
        email = input("Please Enter Your Email: ").strip()
        password = input("Please Enter Your Password: ").strip()

        for librarian in self.library.librarians:
            if librarian.email == email and librarian.password == password:
                print("Librarian signed in successfully.")
                return librarian

        for member in self.library.members:
            if member.email == email and member.password == password:
                print("Member signed in successfully.")
                return member

        print("Invalid credentials. Please try again.")
        return None

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
            library.returned_books.append(book)  # Added to returned_books
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
        self.librarians = []
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

# Main execution

library = Library()

sign_up = SignUp(library)
user = sign_up.register_person()

if isinstance(user, Librarian):
    librarian = user

    book1 = Book("Python", "John Doe", "123")
    book2 = Book("Java", "Jane Smith", "456")
    book3 = Book("C++", "Alice Johnson", "789")
    book4 = Book("R", "Robert Brown", "101112")

    librarian.add_book(library, book1)
    librarian.add_book(library, book2)
    librarian.add_book(library, book3)
    librarian.add_book(library, book4)

    librarian.display_books(library)

    librarian.remove_book(library, book4)
    librarian.display_books(library)

    member1 = Member()
    member2 = Member()

    librarian.add_member(library, member1)
    librarian.add_member(library, member2)
    librarian.display_members(library)

    librarian.remove_member(library, member2)
    librarian.display_members(library)

    member3 = Member()
    member3.borrow_book(library, book2)

    library.display_borrowed_books()

    member3.return_book(library, book2)

    library.display_returned_books()

elif isinstance(user, Member):
    member = user
    member.display_info()

    while True:
        print("\nMember Actions:")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. Display Borrowed Books")
        print("4. Search Books")
        print("5. Exit")

        choice = input("Choose an action: ")

        if choice == "1":
            title = input("Enter the title of the book to borrow: ").strip()
            book = next((b for b in library.books if b.title.lower() == title.lower()), None)
            if book:
                member.borrow_book(library, book)
            else:
                print(f"No book found with title '{title}'.")

        elif choice == "2":
            title = input("Enter the title of the book to return: ").strip()
            book = next((b for b in member.borrowed_books if b.title.lower() == title.lower()), None)
            if book:
                member.return_book(library, book)
            else:
                print(f"No borrowed book found with title '{title}'.")

        elif choice == "3":
            member.display_borrowed_books()

        elif choice == "4":
            title = input("Enter the title to search for: ").strip()
            library.search_books(title=title)

        elif choice == "5":
            print("Exiting Member Actions.")
            break

        else:
            print("Invalid choice. Please choose again.")
