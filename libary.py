class Libary:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.students = []

    def addBook(self, book):
        self.books.append(book)

    def addStudent(self, student):
        self.students.append(student)

    def showBooks(self):
        if len(self.books) == 0:
            print("There are no books!")
            return

        for book in self.books:
            book.showInfo()
            print("------------------")

    def showStudent(self):
        if len(self.students) == 0:
            print("There are no students!")
            return

        for student in self.students:
            student.showInfo()
            print("------------------")

    def searchBook(self, bookID):
        for b in self.books:
            if b.id == bookID:
                return b

        return None

    def searchStudent(self, studentID):
        for s in self.students:
            if s.id == studentID:
                return s

        return None

    def returnBook(self, studentID, bookID):
        s = self.searchStudent(studentID)
        b = self.searchBook(bookID)

        if s and b and bookID in s.borrowedBooks:
            s.borrowedBooks.remove(bookID)
            b.available = True
            return True

        return False

    def borrowBook(self, studentID, bookID):
        s = self.searchStudent(studentID)
        b = self.searchBook(bookID)

        if s and b and b.available:
            s.borrowedBooks.append(bookID)
            b.available = False
            return True

        return False