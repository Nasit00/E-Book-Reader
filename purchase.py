from book import Book 
class Purchase: 
    def __init__(self):
        self.purchases = []
    def add_purchase(self, book: Book):
        self.purchases.append(book.title)
    def list_purchases(self):
        return self.purchases
