class Author :
    def __init__(self , name ,age , id  ):
        self .name = name
        self . age = age
        self . id = id
        self . Books = []


    def __str__ (self) :
        return f"Auhtor id : {self.id}\nAuthor name : {self.name} \nAge : {self.age}\n "