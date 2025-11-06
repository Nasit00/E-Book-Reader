from book import Book
class BookList:
    def __init__(self):
        self.books = []
    
    def add_book(self,book:Book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.id != isbn]

    def find_book(self, isbn):
        for book in self.books:
            if book.id == isbn:   # use .id instead of .isbn
                return book
        return None

    def list_books(self):
        return [str(book) for book in self.books]
    
# Example usage
# b1=Book("The Great Gatsby","F. Scott Fitzgerald","9780743273565",1925,180,10.99)
# b2=Book("1984","George Orwell","9780451524935",1949,328,8.99)
# a=BookList()
# a.add_book(b1)
# a.add_book(b2)
# print(a.list_books())