class Book:
    def __init__(self, name, copies=0) -> None:
        self.name = name
        self.copies = copies

    def increase_copies(self, how_much):
        self.copies += how_much

    def decrease_copies(self, how_much):
        self.copies -= how_much


book1 = Book("Lord of the Rings", 100)
book2 = Book("Hunger Games", 200)
book3 = Book("Maze Runner", 150)

print(book1.name)
print(book2.name)
print(book3.name)


book1.increase_copies(200)
print(book1.copies)

book2.decrease_copies(100)
print(book2.copies)
