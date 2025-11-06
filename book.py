from abcItem import Item
class Book(Item):
    def __init__(self,title,author,isbn,year,pages,amount):
        super().__init__(isbn)
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.amount = amount

    def get_info(self):
        return (f"Title: {self.title}, Author: {self.author}, ISBN: {self.id}, Year: {self.year}, Pages: {self.pages}, Price: Rs.{self.amount}")

    def __str__(self):
        return self.get_info()
    