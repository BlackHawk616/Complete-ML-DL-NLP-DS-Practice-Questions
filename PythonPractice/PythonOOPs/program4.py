# Design a system with classes for Book and Member to issue and return books while tracking availability.

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")

class Member:
    def __init__(self, name):
        self.name = name
        self.issuesd_books = []

    def issue_book(self, book):
        if book.available:
            book.available = False
            self.issuesd_books.append(book)
            print(f"{self.name} has issued '{book.title}'.")
        else:
            print(f"'{book.title}' is currently not available.")
    
    def return_book(self, book):
        if book in self.issuesd_books:
            book.available = True
            self.issuesd_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' issued.")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
member1 = Member("Alice")
member1.issue_book(book1)
member1.issue_book(book2)
book1.display_info()
member1.return_book(book1)
book1.display_info()
