CREATE DATABASE library;
USE library;

CREATE TABLE Authors (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL
);
CREATE TABLE Books (
    id INT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author_id INT NOT NULL,
    is_borrowed BOOLEAN DEFAULT 0,
    FOREIGN KEY (author_id) REFERENCES Authors(id)
);

CREATE TABLE Readers (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL CHECK (age > 0),
    gender ENUM('Male', 'Female') NOT NULL
);

CREATE TABLE BorrowedBooks (
    reader_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY (reader_id, book_id),
    FOREIGN KEY (reader_id) REFERENCES Readers(id),
    FOREIGN KEY (book_id) REFERENCES Books(id)
);
INSERT INTO Authors (id, name, age)
VALUES
(1, 'J.K. Rowling', 58),
(2, 'George R.R. Martin', 76),
(3, 'Agatha Christie', 85),
(4, 'Stephen King', 77);


INSERT INTO Books (id, title, author_id, is_borrowed)
VALUES
(101, 'Harry Potter and the Sorcerer''s Stone', 1, 0),
(102, 'Harry Potter and the Chamber of Secrets', 1, 0),
(103, 'A Game of Thrones', 2, 0),
(104, 'A Clash of Kings', 2, 0),
(105, 'Murder on the Orient Express', 3, 0),
(106, 'Thereaders Shining', 4, 0),
(107, 'IT', 4, 0);

