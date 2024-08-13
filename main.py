class Person:
    def __init__(self, name, email, password, phone_number):
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Phone Number: {self.phone_number}")


class Librarian(Person):
    def __init__(self, name, email, password, phone_number, library_id):
        super().__init__(name, email, password, phone_number)
        self.library_id = library_id

    def display_info(self):
        super().display_info()
        print(f"Library ID: {self.library_id}")
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
       

    def display_members(self, library):
        print("Library Members:")
        library.display_members()
        


class Member(Person):
    def __init__(self, name, email, password, phone_number, member_id):
        super().__init__(name, email, password, phone_number)
        self.member_id = member_id
        self.borrowed_books = []

    def display_info(self):
        super().display_info()
        print(f"Member ID: {self.member_id}")
        print("//" * 15)

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
            library.returned_books.append(book)
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


class SignUp:
    def __init__(self, library):
        self.library = library

    def register_person(self):
        while True:
            user_type = input("Are you a Librarian or a Member? (Enter 'Librarian' or 'Member'): ").strip().lower()
            if user_type not in ['librarian', 'member']:
                print("Invalid input. Please enter 'Librarian' or 'Member'.")
                continue

            name = input("Please Enter Your Name: ").strip()
            email = input("Please Enter Your Email: ").strip()
            password = input("Please Enter Your Password: ").strip()
            phone_number = input("Please Enter Your Phone Number: ").strip()

            if user_type == 'librarian':
                library_id = input("Please Enter Your Library ID: ").strip()
                new_librarian = Librarian(name, email, password, phone_number, library_id)
                self.library.librarians.append(new_librarian)
                print("Librarian registered successfully.")
                return new_librarian

            elif user_type == 'member':
                member_id = input("Please Enter Your Member ID: ").strip()
                new_member = Member(name, email, password, phone_number, member_id)
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


class LibraryManagementSystem:
    def __init__(self):
        self.library = Library()
        self.sign_up = SignUp(self.library)
        self.sign_in = SignIn(self.library)

    def run(self):
        while True:
            print("\nLibrary Management System")
            print("1. Sign Up")
            print("2. Sign In")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                user = self.sign_up.register_person()

            elif choice == "2":
                user = self.sign_in.authenticate()
                if user:
                    if isinstance(user, Librarian):
                        self.librarian_actions(user)
                    elif isinstance(user, Member):
                        self.member_actions(user)

            elif choice == "3":
                print("Exiting the system.")
                break

            else:
                print("Invalid choice. Please choose again.")

    def librarian_actions(self, librarian):
        while True:
            print("\nLibrarian Actions:")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Add Member")
            print("4. Remove Member")
            print("5. Display Books")
            print("6. Display Members")
            print("7. Exit")
            choice = input("Choose an action: ")

            if choice == "1":
                title = input("Enter the title of the book: ").strip()
                author = input("Enter the author of the book: ").strip()
                isbn = input("Enter the ISBN of the book: ").strip()
                book = Book(title, author, isbn)
                librarian.add_book(self.library, book)

            elif choice == "2":
                title = input("Enter the title of the book to remove: ").strip()
                book = next((b for b in self.library.books if b.title.lower() == title.lower()), None)
                if book:
                    librarian.remove_book(self.library, book)
                else:
                    print(f"No book found with title '{title}'.")

            elif choice == "3":
                name = input("Enter the name of the member: ").strip()
                email = input("Enter the email of the member: ").strip()
                password = input("Enter the password of the member: ").strip()
                phone_number = input("Enter the phone number of the member: ").strip()
                member_id = input("Enter the member ID: ").strip()
                member = Member(name, email, password, phone_number, member_id)
                librarian.add_member(self.library, member)

            elif choice == "4":
                email = input("Enter the email of the member to remove: ").strip()
                member = next((m for m in self.library.members if m.email == email), None)
                if member:
                    librarian.remove_member(self.library, member)
                else:
                    print(f"No member found with email '{email}'.")

            elif choice == "5":
                librarian.display_books(self.library)

            elif choice == "6":
                librarian.display_members(self.library)

            elif choice == "7":
                print("Exiting Librarian Actions.")
                break

            else:
                print("Invalid choice. Please choose again.")

    def member_actions(self, member):
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
                book = next((b for b in self.library.books if b.title.lower() == title.lower()), None)
                if book:
                    member.borrow_book(self.library, book)
                else:
                    print(f"No book found with title '{title}'.")

            elif choice == "2":
                title = input("Enter the title of the book to return: ").strip()
                book = next((b for b in member.borrowed_books if b.title.lower() == title.lower()), None)
                if book:
                    member.return_book(self.library, book)
                else:
                    print(f"No borrowed book found with title '{title}'.")

            elif choice == "3":
                member.display_borrowed_books()

            elif choice == "4":
                title = input("Enter the title to search for: ").strip()
                self.library.search_books(title=title)

            elif choice == "5":
                print("Exiting Member Actions.")
                break

            else:
                print("Invalid choice. Please choose again.")


system = LibraryManagementSystem()
system.run()

