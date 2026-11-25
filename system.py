from libary import Libary
from student import Student
from book import Book

library = Libary("My Library")


def menu():
    print("""
    ===== LIBRARY SYSTEM =====
        1. Add Student
        2. Add Book
        3. Search Student
        4. Search Book
        5. Borrow Book
        6. Return Book
           0. Exit
    """)


def app():
    while True:
        menu()
        choice = input("Choose: ")

        if choice == "0":
            print("Goodbye...")
            break

        elif choice == "1":
            studentID = input("Enter Student ID: ")
            name = input("Enter Student Name: ")

            student = Student(studentID, name)
            library.addStudent(student)

        elif choice == "2":
            bookID = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")

            book = Book(bookID, title, author)
            library.addBook(book)

        elif choice == "3":
            studentID = input("Enter Student ID: ")
            student = library.searchStudent(studentID)

            if student:
                student.showInfo()
            else:
                print("Student not found!")

        elif choice == "4":
            bookID = input("Enter Book ID: ")
            book = library.searchBook(bookID)

            if book:
                book.showInfo()
            else:
                print("Book not found!")

        elif choice == "5":
            studentID = input("Enter Student ID: ")
            bookID = input("Enter Book ID: ")

            if library.borrowBook(studentID, bookID):
                print("Book borrowed successfully!")
            else:
                print("Borrow failed!")

        elif choice == "6":
            studentID = input("Enter Student ID: ")
            bookID = input("Enter Book ID: ")

            if library.returnBook(studentID, bookID):
                print("Book returned successfully!")
            else:
                print("Return failed!")

        else:
            print("Invalid choice!")