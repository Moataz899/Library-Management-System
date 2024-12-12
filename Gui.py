import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class Person:
    def __init__(self, name, email, password, phone_number):
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def display_info(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone_number}"

class Librarian(Person):
    def __init__(self, name, email, password, phone_number, library_id):
        super().__init__(name, email, password, phone_number)
        self.library_id = library_id

    def display_info(self):
        return super().display_info() + f", Library ID: {self.library_id}"

class Member(Person):
    def __init__(self, name, email, password, phone_number, member_id):
        super().__init__(name, email, password, phone_number)
        self.member_id = member_id
        self.borrowed_books = set()

    def display_info(self):
        return super().display_info() + f", Member ID: {self.member_id}"

class Book:
    def __init__(self, title, author, isbn):
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip()
        self.available = True

    def display_info(self):
        availability = "Available" if self.available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Availability: {availability}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.librarians = []
        self.borrowed_books = set()

    def add_book(self, book):
        if not any(b.isbn == book.isbn for b in self.books):
            self.books.append(book)
            messagebox.showinfo("Success", f"Book '{book.title}' added.")
        else:
            messagebox.showerror("Error", f"Book '{book.title}' already exists.")

    def remove_book(self, isbn):
        book = next((b for b in self.books if b.isbn == isbn), None)
        if book:
            self.books.remove(book)
            self.borrowed_books.discard(book)
            messagebox.showinfo("Success", f"Book '{book.title}' removed.")
        else:
            messagebox.showerror("Error",f"Book with ISBN '{isbn}' not found.")

    def add_member(self, member):
        if not any(m.email == member.email for m in self.members):
            self.members.append(member)
            messagebox.showinfo("Success", f"Member '{member.name}' added.")
        else:
            messagebox.showerror("Error", f"Member '{member.name}' already exists.")

    def remove_member(self, email):
        member = next((m for m in self.members if m.email == email), None)
        if member:
            self.members.remove(member)
            messagebox.showinfo("Success", f"Member '{member.name}' removed.")
        else:
            messagebox.showerror("Error", f"No member found with email '{email}'.")

    def display_books(self):
        if not self.books:
            messagebox.showinfo("Library Books", "No books in the library.")
            return
        book_list = "\n".join([book.display_info() for book in self.books])
        self.display_large_info("Library Books", book_list)

    def display_members(self):
        if not self.members:
            messagebox.showinfo("Library Members", "No members in the library.")
            return
        member_list = "\n".join([member.display_info() for member in self.members])
        self.display_large_info("Library Members", member_list)

    def display_large_info(self, title, info):
        large_info_window = tk.Toplevel()
        large_info_window.title(title)
        large_info_window.geometry("600x400")  
        large_info_window.configure(bg="#f0f8ff")  
        
        text_area = tk.Text(large_info_window, wrap=tk.WORD, bg="#ffffff", fg="#000000")  
        text_area.insert(tk.END, info)
        text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        close_button = tk.Button(large_info_window, text="Close", command=large_info_window.destroy, bg="#4682b4", fg="#ffffff")  
        close_button.pack(pady=10)

    def search_books(self, title=None, author=None):
        found_books = [book for book in self.books if
                       (title and title.lower() in book.title.lower()) or
                       (author and author.lower() in book.author.lower())]
        if not found_books:
            messagebox.showinfo("Search Results", "No books found.")
        else:
            search 
            search_results = "\n".join([book.display_info() for book in found_books])
            self.display_large_info("Search Results", search_results)

class SignUp:
    def __init__(self, library):
        self.library = library

    def register_person(self, user_type):
        name = simpledialog.askstring("Sign Up", "Enter Your Name:")
        email = simpledialog.askstring("Sign Up", "Enter Your Email:")
        password = simpledialog.askstring("Sign Up", "Enter Your Password:", show='*')
        phone_number = simpledialog.askstring("Sign Up", "Enter Your Phone Number:")

        if user_type == 'librarian':
            library_id = simpledialog.askstring("Sign Up", "Enter Your Library ID:")
            new_librarian = Librarian(name, email, password, phone_number, library_id)
            self.library.librarians.append(new_librarian)
            messagebox.showinfo("Success", "Librarian registered successfully.")
            return new_librarian

        elif user_type == 'member':
            member_id = simpledialog.askstring("Sign Up", "Enter Your Member ID:")
            new_member = Member(name, email, password, phone_number, member_id)
            self.library.members.append(new_member)
            messagebox.showinfo("Success", "Member registered successfully.")
            return new_member

class SignIn:
    def __init__(self, library):
        self.library = library

    def authenticate(self):
        email = simpledialog.askstring("Sign In", "Enter Your Email:")
        password = simpledialog.askstring("Sign In", "Enter Your Password:", show='*')

        for librarian in self.library.librarians:
            if librarian.email == email and librarian.password == password:
                messagebox.showinfo("Success", "Librarian signed in successfully.")
                return librarian

        for member in self.library.members:
            if member.email == email and member.password == password:
                messagebox.showinfo("Success", "Member signed in successfully.")
                return member

        messagebox.showerror("Error", "Invalid credentials. Please try again.")
        return None

class LibraryManagementSystem:
    def __init__(self, root):
        self.library = Library()
        self.sign_up = SignUp(self.library)
        self.sign_in = SignIn(self.library)
        self.root = root
        self.root.title("Library Management System")

        self.main_menu()

    def main_menu(self):
        frame = ttk.Frame(self.root, padding="10 10 10 10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        title = ttk.Label(frame, text="Library Management System", font=("Arial", 16))
        title.grid(row=0, column=0, columnspan=3, pady=10)

        sign_up_button = ttk.Button(frame, text="Sign Up", command=self.sign_up_menu)
        sign_up_button.grid(row=1, column=0, pady=5, padx=5, sticky=tk.EW)

        sign_in_button = ttk.Button(frame, text="Sign In", command=self.sign_in_menu)
        sign_in_button.grid(row=1, column=1, pady=5, padx=5, sticky=tk.EW)

        exit_button = ttk.Button(frame, text="Exit", command=self.root.quit)
        exit_button.grid(row=1, column=2, pady=5, padx=5, sticky=tk.EW)

    def sign_up_menu(self):
        
        sign_up_window = tk.Toplevel(self.root)
        sign_up_window.title("Sign Up")

        ttk.Label(sign_up_window, text="Are you a Librarian or a Member?").pack(pady=10)

        librarian_button = ttk.Button(sign_up_window, text="Librarian", command=lambda: self.handle_sign_up("librarian", sign_up_window))
        librarian_button.pack(padx=20, pady=5, fill=tk.X)

        member_button = ttk.Button(sign_up_window, text="Member", command=lambda: self.handle_sign_up("member", sign_up_window))
        member_button.pack(padx=20, pady=5, fill=tk.X)

    def handle_sign_up(self, user_type, window):
        window.destroy()
        user = self.sign_up.register_person(user_type)
        if user:
            self.display_welcome_message(user)

    def sign_in_menu(self):
        user = self.sign_in.authenticate()
        if user:
            self.display_welcome_message(user)
            if isinstance(user, Librarian):
                self.librarian_actions(user)
            elif isinstance(user, Member):
                self.member_actions(user)

    def display_welcome_message(self, user):
        role = "Librarian" if isinstance(user, Librarian) else "Member"
        messagebox.showinfo("Welcome", f"Welcome, {user.name} ({role})!")

    def librarian_actions(self, librarian):
        action_window = tk.Toplevel(self.root)
        action_window.title("Librarian Actions")

        ttk.Label(action_window, text="Choose an action:").pack(pady=10)

        actions = [
            ("Add Book", lambda: self.add_book_action(librarian)),
            ("Remove Book", lambda: self.remove_book_action(librarian)),
            ("Add Member", lambda: self.add_member_action(librarian)),
            ("Remove Member", lambda: self.remove_member_action(librarian)),
            ("Display Books", lambda: self.library.display_books()),
            ("Display Members", lambda: self.library.display_members()),
            ("Exit", action_window.destroy)
        ]

        for text, command in actions:
            ttk.Button(action_window, text=text, command=command).pack(fill=tk.X, padx=20, pady=5)

    def add_book_action(self, librarian):
        title = simpledialog.askstring("Add Book", "Enter the title of the book:")
        author = simpledialog.askstring("Add Book", "Enter the author of the book:")
        isbn = simpledialog.askstring("Add Book", "Enter the ISBN of the book:")
        if title and author and isbn:
            book = Book(title, author, isbn)
            self.library.add_book(book)

    def remove_book_action(self, librarian):
        isbn = simpledialog.askstring("Remove Book", "Enter the ISBN of the book to remove:")
        if isbn:
            self.library.remove_book(isbn)

    def add_member_action(self, librarian):
        name = simpledialog.askstring("Add Member", "Enter the name of the member:")
        email = simpledialog.askstring("Add Member", "Enter the email of the member:")
        password = simpledialog.askstring("Add Member", "Enter the password of the member:", show='*')
        phone_number = simpledialog.askstring("Add Member", "Enter the phone number of the member:")
        member_id = simpledialog.askstring("Add Member", "Enter the member ID:")
        if name and email and password and phone_number and member_id:
            member = Member(name, email, password, phone_number, member_id)
            self.library.add_member(member)

    def remove_member_action(self, librarian):
        email = simpledialog.askstring("Remove Member", "Enter the email of the member to remove:")
        if email:
            self.library.remove_member(email)

    def member_actions(self, member):
        action_window = tk.Toplevel(self.root)
        action_window.title("Member Actions")

        ttk.Label(action_window, text="Choose an action:").pack(pady=10)

        actions = [
            ("Borrow a Book", lambda: self.borrow_book_action(member)),
            ("Return a Book", lambda: self.return_book_action(member)),
            ("Display Borrowed Books", lambda: member.display_borrowed_books()),
            ("Search Books", lambda: self.search_books_action()),
            ("Exit", action_window.destroy)
        ]

        for text, command in actions:
            ttk.Button(action_window, text=text, command=command).pack(fill=tk.X, padx=20, pady=5)

    def borrow_book_action(self, member):
        isbn = simpledialog.askstring("Borrow a Book", "Enter the ISBN of the book to borrow:")
        if isbn:
            book = next((b for b in self.library.books if b.isbn == isbn), None)
            if book:
                if book.available:
                    member.borrowed_books.add(book)
                    book.available = False
                    self.library.borrowed_books.add(book)
                    messagebox.showinfo("Success", f"Book '{book.title}' borrowed.")
                else:
                    messagebox.showerror("Error", f"Book '{book.title}' is not available.")
            else:
                messagebox.showerror("Error", f"Book with ISBN '{isbn}' not found.")

    def return_book_action(self, member):
        isbn = simpledialog.askstring("Return a Book", "Enter the ISBN of the book to return:")
        if isbn:
            book = next((b for b in member.borrowed_books if b.isbn == isbn), None)
            if book:
                member.borrowed_books.remove(book)
                book.available = True
                self.library.borrowed_books.discard(book)
                messagebox.showinfo("Success", f"Book '{book.title}' returned.")
            else:
                messagebox.showerror("Error", f"You haven't borrowed a book with ISBN '{isbn}'.")

    def search_books_action(self):
        title = simpledialog.askstring("Search Books", "Enter the title to search for:")
        if title:
            self.library.search_books(title=title)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")  
    app = LibraryManagementSystem(root)
    root.mainloop()