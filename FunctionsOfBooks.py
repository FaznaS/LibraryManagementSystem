from book import Book


class BookFunctions:
    def __init__(self):
        self.book_list = []
        self.books_present_initially()

    # view books already present
    def books_present_initially(self):
        book1 = Book(isbn_number='ISBN1234', title='The Solar System', format='Hardcover', subject='Science',
                     rental_price_per_day=15.00, number_of_copies=5)
        book2 = Book(isbn_number='ISBN9876', title='Types of Animal Species', format='Paperback',
                     subject='Science', rental_price_per_day=10.00, number_of_copies=8)
        book3 = Book(isbn_number='ISBN1290', title='Second World War', format='Hardcover', subject='History',
                     rental_price_per_day=12.50, number_of_copies=1)

        self.book_list.append(book1)
        self.book_list.append(book2)
        self.book_list.append(book3)

    def add(self):
        print('Enter the details of the books to be added')

        isbn_number = input('Enter the ISBN number: ')
        title = input('Enter the title: ')
        format = input('Enter the format: ')
        subject = input('Enter the subject: ')

        try:
            rental_price_per_day = float(input('Enter the rental price per day: '))
        except ValueError:
            print('Invalid! Please enter the price with decimals')
            print('Ending process..')
            quit()

        try:
            number_of_copies = int(input('Enter the number of copies available: '))
        except ValueError:
            print('Invalid input')
            print('Ending process..')
            quit()

        new_book = Book(isbn_number, title, format, subject, rental_price_per_day, number_of_copies)

        self.book_list.append(new_book)
        print('The book was successfully added to the library')

    def remove(self):
        book_isbn = input("Enter the ISBN number of the book you want to remove: ")
        for book in self.book_list:
            if book.isbn_number == book_isbn:
                self.book_list.remove(book)
                print('The book was successfully removed from the library')

    # To view currently available books
    def currently_available(self):
        # iterating inside the list to check the availability
        book_found = False
        for book in self.book_list:
            if book.number_of_copies > 0:
                book_found = True
                print(f'The book with ISBN number {book.isbn_number} and title {book.title} is available in '
                      f'the form of {book.format}')
        if not book_found:
            print('There are no books available')

    # To view currently unavailable books
    def currently_unavailable(self):
        # iterating inside the list to check the unavailability
        book_found = False
        for book in self.book_list:
            if book.number_of_copies <= 0:
                book_found = True
                print(f'Sorry.The book with ISBN number {book.isbn_number} and '
                      f'title {book.title} is currently unavailable')
        if not book_found:
            print('All books are available')

    def search_by_subject(self, subject):
        available_sub = False
        for resource in self.book_list:
            if resource.subject == subject:
                available_sub = True
                print(f'The book with {resource.title} is available')
        if not available_sub:
            print(f'Sorry {subject} books are currently unavailable')

    def lend(self):
        book_isbn = input('Enter the ISBN number: ')
        for book in self.book_list:
            if book.isbn_number == book_isbn and book.number_of_copies > 0:
                print(f'The book with ISBN number {book_isbn} with title {book.title} is available to be lent')
                book.number_of_copies -= 1
                print('Book is lent')
        if book.isbn_number != book_isbn and book.number_of_copies <= 0:
            print('Sorry the book is unavailable')

    def resource_received(self):
        book_isbn = input('Enter the ISBN number: ')
        for book in self.book_list:
            if book.isbn_number == book_isbn:
                print(f'The book details are successfully updated')
                book.number_of_copies += 1
