class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_email):
        self.email = new_email
        print("This user's email has been updated")

    def __repr__(self):
        return "User: {name}, email: {email}, books read: {book_nums}".format(name=self.name, email=self.email, book_nums=len(self.books))

    def __eq__(self, other):
        return self.name == other.name and self.email == other.email

    def read_book(self, book, rating=None):
        book = {book:rating}
        self.books.update(book)

    def get_average_rating(self):

        # iterates through all values in self.books which are ratings
        # calculate the average ratings
        # it should return this average

        total_rating = 0

        for book, rating in self.books.items():
            total_rating += rating
        num_of_ratings = len(self.books)

        average = total_rating / num_of_ratings
        return average








