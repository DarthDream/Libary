from book import*

class Student:
    def __init__(self,name,studentID):
        self.name=name
        self.studentID=studentID
        self.borrowedBooks=[]


    def showInfo(self):
        print(f'''

        ID:{self.studentID}
        Title:{self.name}
        Author:{len(self.borrowedBooks)}
         
        ''')


    def borrowedBook(self,book):
        if book.isAvalible:
            book.borrow()
        else:
            print("Book is not avalible")

    def returnBook(self,book):
        if book in self.borrowedBooks:
            book.returnBook()
            self.borrowedBooks.remove(book)
        else:
            print("Book is not avalible...")