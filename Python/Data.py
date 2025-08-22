import mysql.connector

class DatabaseHandler:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Meino@10",
            database="library"
        )
        self.cursor = self.conn.cursor()


    def fetch_books(self):
        self.cursor.execute("SELECT id, title, is_borrowed FROM Books")
        return self.cursor.fetchall()


    def fetch_borrowed_books(self):
        self.cursor.execute("""SELECT Readers.name, Books.title 
                               FROM BorrowedBooks 
                               JOIN Readers ON Readers.id = BorrowedBooks.reader_id 
                               JOIN Books ON Books.id = BorrowedBooks.book_id""")
        return self.cursor.fetchall()


    def add_reader(self, reader):
        try:
            query = """
            INSERT INTO Readers (id, name, age, gender) 
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(
                query, (reader.id, reader.name, reader.age, reader.gender)
            )
            self.conn.commit()
            print(f"Reader {reader.name} added successfully!")
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
        except ValueError:
            print("Invalid data type provided. Age and ID must be numbers.")

    def reader_exists(self, reader_id):
        query = "SELECT COUNT(*) FROM Readers WHERE id = %s"
        self.cursor.execute(query, (reader_id,))
        result = self.cursor.fetchone()
        return result[0] > 0



    def borrow_book(self, reader_id, book_id):
        self.cursor.execute("SELECT is_borrowed FROM Books WHERE id = %s", (book_id,))
        result = self.cursor.fetchone()

        if not result:
            return False, "Book not found."

        if result[0] == 1:
            return False, "Book already borrowed."

        self.cursor.execute("UPDATE Books SET is_borrowed = 1 WHERE id = %s", (book_id,))
        self.cursor.execute("INSERT INTO BorrowedBooks (reader_id, book_id) VALUES (%s, %s)", (reader_id, book_id))
        self.conn.commit()
        return True, "Book borrowed successfully."


    def return_book(self, reader_id, book_id):
        self.cursor.execute("UPDATE Books SET is_borrowed = 0 WHERE id = %s", (book_id,))
        self.cursor.execute("DELETE FROM BorrowedBooks WHERE reader_id = %s AND book_id = %s", (reader_id, book_id))
        self.conn.commit()


    def close(self):
        self.cursor.close()
        self.conn.close()
