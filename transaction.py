from datetime import datetime
from user import User
from book import Book

class Transaction:
    def __init__(self, user:User, book:Book):
        self.user = user
        self.book = book
        self.date = datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - {self.user.name} bought '{self.book.title}' for Rs.{self.book.amount}"
