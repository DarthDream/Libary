class Libary:
    def __init__(self,name):
        self.name=name
        self.books=[]
        self.student=[]

    def addBook(self,book):
       book=input("Kitab adi de:")
       if book in self.books:
           print("Book is already append")
       else:
           self.books.append(book)
           print("Book addde sucsesfuly")

    def addStudent(self,student):
       student=input("Kitab adi de:")
       if student in self.student:
           print("Student is already append")
       else:
           self.books.append(student)
           print("Studetn addde sucsesfuly")

    def showBooks(self):
        if len(self.books)==0:
            print("There have not book")
            return

        for book in self.books:
            book.showInfo()
            print("------------------")

    def showStudent(self):
        if len(self.student)==0:
            print("There have not student")
            return

        for student in self.student:
            student.showInfo()
            print("------------------")        