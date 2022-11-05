class Review:
    def __init__(self, id, description, rating) -> None:
        self.id = id
        self. description = description
        self.rating = rating
    
    def __str__(self) -> str:
        return f"""
        ---------------------
        Review {self.id} : {self.description}  - Rating : {self.rating} 
        """


class Book:
    def __init__(self, id, name, author) -> None:
        self.id = id
        self.name = name
        self.author = author
        self.reviews = list()
        self.review_count = 0

    def add_review(self, review: Review):
        self.reviews.append(review)
        self.review_count += 1

    def __str__(self) -> str:
        book_str=f"""
        ====================================
        ID : {self.id}
        Book : {self.name}
        Author : {self.author}
        ====================================
        """
        if self.review_count > 0:
            book_str += f"""
        Which has {self.review_count} reviews:"""
            book_str+= "".join([f"{x}" for x in self.reviews])

        return book_str 

book = Book(123, "Object Oriented Programming with Python", "Ranga")
book.add_review(Review(10,"Great Book",5))
book.add_review(Review(101,"Awesome",5))

print(book)