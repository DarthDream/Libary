class Book:
    def __init__(self,bookID,title,author,pageCount):
        self.bookID=bookID
        self.title=title
        self.author=author
        self.pageCount=pageCount
        self.isAvalible=True

    def showInfo(self):
        print(f'''
         
        ID:{self.bookID}
        Title:{self.title}
        Author:{self.author}
        PageCount:{self.pageCount}

       ''')
        
        if self.isAvalible:
            print("Status: Available")
        else:
            print("Status:Borrowed")

    def borrow(self):
        if  self.isAvalible:
            self.isAvalible=False
            print(f"{self.title} borrowed")
        else:
            print("Book is already borrowed")

    def returnBook(self):
        if not self.isAvalible:
            self.isAvalible=True
            print(f"{self.title} returned")
        else:
            print("\nBook is already in the libary")


book1 = Book(1, "Clean Code", "Robert Martin", 464)
book2 = Book(2, "Python Crash Course", "Eric Matthes", 560)
book3 = Book(3, "Atomis Habits", "James Clear", 320)