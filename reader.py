class Reader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.pages = []
        self.current_page = 0
    def read(self):
        with open(self.file_path + ".txt", 'r') as file:
            content=file.read()
            self.pages = content.split('@@@')
    def open_book(self):
        print("Book opened.")
        print(self.pages[0])

    def next_page(self):
        if self.current_page == len(self.pages) - 1:
            print("You are on the last page.")
            return
        print(self.pages[self.current_page + 1])
        self.current_page += 1
    def previous_page(self):
        if self.current_page == 0:
            print("You are on the first page.")
            return
        print(self.pages[self.current_page - 1])
        self.current_page -= 1

    def close_book(self):
        print("Book closed.")

