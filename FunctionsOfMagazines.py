from magazine import Magazine


class MagazineFunctions:
    def __init__(self):
        self.magazine_list = []
        self.magazines_present_initially()

    # view books already present
    def magazines_present_initially(self):
        magazine1 = Magazine(magazine_number='01', title='History of Cricket', color_or_black='color', subject='Sports',
                             rental_price_per_day=5.00, number_of_copies=7)
        magazine2 = Magazine(magazine_number='02', title='Evolution of the Computer', color_or_black='black&white',
                             subject='Technology', rental_price_per_day=3.00, number_of_copies=21)

        self.magazine_list.append(magazine1)
        self.magazine_list.append(magazine2)

    def add(self):
        print('Enter the details of the magazines to be added')

        magazine_number = input('Enter the Magazine number: ')
        title = input('Enter the title: ')
        color_or_black = input('Enter the color format (color/black): ')
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

        new_magazine = Magazine(magazine_number, title, color_or_black, subject, rental_price_per_day, number_of_copies)

        self.magazine_list.append(new_magazine)
        print('The magazine was successfully added to the library')

    def remove(self):
        mag_number = input("Enter the Magazine number of the magazine you want to remove: ")
        for mag in self.magazine_list:
            if mag.magazine_number == mag_number:
                self.magazine_list.remove(mag)
                print('The magazine was successfully removed from the library')

    # To view currently available books
    def currently_available(self):
        # iterating inside the list to check the availability
        available = False
        for mag in self.magazine_list:
            if mag.number_of_copies > 0:
                available = True
                print(f'The magazine with magazine number {mag.magazine_number} and title {mag.title} is available in '
                      f'the form of {mag.color_or_black}')
        if not available:
            print('Sorry the magazine is currently unavailable')

    # To view currently unavailable books
    def currently_unavailable(self):
        # iterating inside the list to check the unavailability
        available = False
        for mag in self.magazine_list:
            if mag.number_of_copies <= 0:
                available = True
                print(f'The magazine with magazine number {mag.magazine_number} and title {mag.title} is not available')
        if not available:
            print(f'The book with ISBN number {mag.magazine_number} and title {mag.title} is available '
                  f'in the form of {mag.color_or_black}')

    def search_by_subject(self, subject):
        available_sub = False
        for resource in self.magazine_list:
            if resource.subject == subject:
                available_sub = True
                print(f'The {resource.title} magazine is available')
        if not available_sub:
            print(f'Sorry {subject} magazines are currently unavailable')

    def lend(self):
        magazine_number = input('Enter the magazine number: ')
        for mag in self.magazine_list:
            if mag.magazine_number == magazine_number and mag.number_of_copies > 0:
                print(f'The magazine with number {magazine_number} with title {mag.title} is available to be lent')
                mag.number_of_copies -= 1
                print('Magazine lent')
        if mag.magazine_number != magazine_number and mag.number_of_copies <= 0:
            print('Sorry the magazine is unavailable')

    def resource_received(self):
        magazine_number = input('Enter the magazine number: ')
        for mag in self.magazine_list:
            if mag.magazine_number == magazine_number:
                print(f'The magazine details are successfully updated')
                mag.number_of_copies += 1
