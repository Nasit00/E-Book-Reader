from booklist import BookList
from userlist import UserList
from transaction import Transaction
from user import User
from purchase import Purchase

class Store:
    def __init__(self):
        self.booklist = BookList()    
        self.userlist = UserList()
        self.transactions = []
        self.purchase = Purchase()

    def purchase_book(self):
        name = input("Enter your name: ")
        user_id = int(input("Enter your ID: "))
        user = User(name, user_id)
        self.userlist.add_user(user)

        isbn = input("Enter ISBN of the book you want to purchase: ")
        book = self.booklist.find_book(isbn)
        if not book:
            print("❌ Book not found or out of stock.")
            return

        print(f"💰 {book.title} costs Rs.{book.amount}")
        confirm = input("Do you want to buy this book? (yes/no): ")

        if confirm.lower() == "yes":
            transaction = Transaction(user, book)
            self.transactions.append(transaction)
            self.purchase.add_purchase(book)
            print(f"✅ {user.name} purchased '{book.title}' successfully!")
        else:
            print("❌ Purchase cancelled.")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("\n📘 Transaction History:")
            for t in self.transactions:
                print(t)

    def show_users(self):
        if not self.userlist._users:
            print("No users registered yet.")
        else:
            print("\n👤 Registered Users:")
            for user in self.userlist._users:
                print(user.get_info())

    def show_books(self):
        if not self.booklist.books:
            print("No books available.")
        else:
            print("\n📚 Available Books:")
            for book in self.booklist.books:
                print(book.get_info())
