# creating a class for magazines

class Magazine:
    def __init__(self, magazine_number, title, color_or_black, subject, rental_price_per_day, number_of_copies):
        self.magazine_number = magazine_number
        self.title = title
        self.color_or_black = color_or_black
        self.subject = subject
        self.rental_price_per_day = rental_price_per_day
        self.number_of_copies = number_of_copies
