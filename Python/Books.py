class BOOK:
    def __init__(self , title , id , author_id , is_borrowed = False):
        self.title = title
        self.id = id
        self.author_id = author_id
        self.is_borrowed = bool (is_borrowed)

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.id}: {self.title} ({status})"