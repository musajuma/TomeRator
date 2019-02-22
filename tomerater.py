from book import Book
from fiction import Fiction
from non_fiction import NonFiction
from user import User


class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book

    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        return new_fiction

    def create_non_fiction(self, title, subject, level, isbn):
        new_fon_fiction = NonFiction(title, subject, level, isbn)
        return new_fon_fiction

    def add_book_to_user(self, book, email, rating=None):
        # get user in self.users with key email
        # if user doesnt exist, it should print out "no user with email{email}
        # if user exist it should call read_book on this user with book and rating
        # call add_rating on book, with rating

        user = self.users.get_email(email, None)
        if user is None:
            print("No user with email!")
        else:
            user.read_book(book, rating)

            book.add_rating(rating)

        # check if book is in TomeRators self.books already
        # if it is not, add the book to self.books with a value of 1 (because one has read it)
        # if book already in the catalog increase the value of it in self.books by 1 (because one more user has read it)

        book = self.books.get(book, None)
        if book is None:
            self.books[book] = 1
        else:
            self.books[book] += 1

    def add_user(self, name, email, user_books=None):
        new_user = User(name, email)
        self.users[email] = new_user

        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for Book in self.books.keys():
            print(Book)

    def print_users(self):
        for User in self.users.values():
            print(User)























