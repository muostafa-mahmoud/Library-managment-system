from Data import DatabaseHandler
from Reader import Reader

class LibraryService:
    def __init__(self):
        self.db = DatabaseHandler()

    def register_reader(self):
        try:
            reader_id = int(input("Enter Reader ID: "))
            if self.db.reader_exists(reader_id):
                print (f"Reader {reader_id} already exists.")
                return
            name = input("Enter Reader Name: ")
            age = int(input("Enter Reader Age: "))
            gender = input("Enter Reader Gender (male/female): ")
            reader = Reader(reader_id, name, age, gender)
            self.db.add_reader(reader)
        except ValueError:
            print("Invalid input! ID and Age must be integers.")

    def borrow_book(self):
        print("\nAvailable Books:")
        books = self.db.fetch_books()
        for book in books:
            if book[2] == 0:
                print(f"ID: {book[0]}, Title: {book[1]}")

        reader_id = int(input("Enter Reader ID: "))
        book_id = int(input("Enter Book ID to Borrow: "))
        success, message = self.db.borrow_book(reader_id, book_id)
        print(message)

    def return_book(self):
        reader_id = int(input("Enter Reader ID: "))
        book_id = int(input("Enter Book ID to Return: "))
        self.db.return_book(reader_id, book_id)
        print("Book returned successfully!")

    def list_borrowed_books(self):
        borrowed = self.db.fetch_borrowed_books()
        if not borrowed:
            print("No borrowed books.")
        else:
            print("\nBorrowed Books:")
            for record in borrowed:
                print(f"Reader: {record[0]}, Borrowed {record[1]}")

    def close_service(self):
        self.db.close()
