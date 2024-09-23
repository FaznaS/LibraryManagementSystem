# creating a class for books

class Book:
    def __init__(self, isbn_number, title, format, subject, rental_price_per_day, number_of_copies):
        self.isbn_number = isbn_number
        self.title = title
        self.format = format
        self.subject = subject
        self.rental_price_per_day = rental_price_per_day
        self.number_of_copies = number_of_copies
