from store import Store
from book import Book
from reader import Reader
from purchase import Purchase
store = Store()
b1 = Book("Python", "F. Scott Fitzgerald", "9780743273565", 1925, 180, 1099)
store.booklist.add_book(b1)

def main():
    while True:
        print("\n=== BOOK STORE MENU ===")
        print("1. Show all books")
        print("2. Purchase a book")
        print("3. Show transactions")
        print("4. Show all users")
        print("5. Read E-Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            store.show_books()    
        elif choice == "2":
            store.purchase_book()
        elif choice == "3":
            store.show_transactions()
        elif choice == "4":
            store.show_users()   
        elif choice == "5":
            ask = input("Enter book name :")
            if ask not in store.purchase.purchases:
                print("You have not purchased this book yet.")
            elif ask in store.purchase.purchases:
                reader = Reader(ask.lower() or ask.capitalize())
                reader.read()
                reader.open_book()
                while True:
                    print("\n--- E-BOOK READER MENU ---")
                    print("1. Next Page")
                    print("2. Previous Page")
                    print("3. Close Book")
                    action = input("Enter choice: ")
                    if action == "1":
                        reader.next_page()
                    elif action == "2":
                        reader.previous_page()
                    elif action == "3":
                        reader.close_book()
                        break
                    else:
                        print("Invalid choice.")    
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
