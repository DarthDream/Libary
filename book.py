class Book:
    def __init__(self, bookID, title, author, pageCount):
        self.id = bookID
        self.title = title
        self.author = author
        self.pageCount = pageCount
        self.available = True

    def showInfo(self):
        print(f"""
        ID: {self.id}
        Title: {self.title}
        Author: {self.author}
        PageCount: {self.pageCount}
        """)

        if self.available:
            print("Status: Available")
        else:
            print("Status: Borrowed")

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} borrowed")
        else:
            print("Book is already borrowed")

    def returnBook(self):
        if not self.available:
            self.available = True
            print(f"{self.title} returned")
        else:
            print("\nBook is already in the library")
