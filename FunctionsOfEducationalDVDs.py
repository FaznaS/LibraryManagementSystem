from educationalDVD import EducationalDvd


class EducationalDvdFunctions:
    def __init__(self):
        self.educationalDVD_list = []
        self.educational_dvd_present_initially()

    # view books already present
    def educational_dvd_present_initially(self):
        dvd1 = EducationalDvd(dvd_number=10, title='Birth of the Solar System', subject='Astronomy',
                              rental_price_per_day=2.50, number_of_copies=10)
        dvd2 = EducationalDvd(dvd_number=11, title='Pythagoras Theorem', subject='Math',
                              rental_price_per_day=1.00, number_of_copies=50)

        self.educationalDVD_list.append(dvd1)
        self.educationalDVD_list.append(dvd2)

    def add(self):
        print('Enter the details of the DVD to be added')
        try:
            dvd_number = int(input('Enter the DVD number: '))
        except ValueError:
            print('Invalid! Please enter the proper Number')
            print('Ending process..')
            quit()

        title = input('Enter the title: ')
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

        new_dvd = EducationalDvd(dvd_number, title, subject, rental_price_per_day, number_of_copies)

        self.educationalDVD_list.append(new_dvd)
        print('The educational DVD was successfully added to the library')

    # remove resource
    def remove(self):
        try:
            dvd_number = int(input("Enter the DVD number of the DVD you want to remove: "))
        except ValueError:
            print('Invalid! Please enter the proper Number')
            print('Ending process..')
            quit()

        for dvd in self.educationalDVD_list:
            if dvd.dvd_number == dvd_number:
                self.educationalDVD_list.remove(dvd)
                print('The DVD was successfully removed from the library')

    # To view currently available books
    def currently_available(self):
        # iterating inside the list to check the availability
        available_sub = False
        for dvd in self.educationalDVD_list:
            if dvd.number_of_copies > 0:
                available_sub = True
                print(f'The educational DVD with DVD number {dvd.dvd_number} and title {dvd.title} is available')
        if not available_sub:
            print('Sorry the DVD is not available')

    # To view currently unavailable books
    def currently_unavailable(self):
        # iterating inside the list to check the unavailability
        available_sub = False
        for dvd in self.educationalDVD_list:
            if dvd.number_of_copies <= 0:
                available_sub = True
                print(f'The educational DVD with DVD number {dvd.dvd_number} and '
                      f'title {dvd.title} is not available')
        if not available_sub:
            print('All resources are available')

    def search_by_subject(self, subject):
        available_sub = False
        for resource in self.educationalDVD_list:
            if resource.subject == subject:
                available_sub = True
                print(f'The {resource.title} DVD is available')
        if not available_sub:
            print(f'Sorry {subject} DVDs are currently unavailable')

    def lend(self):
        try:
            dvd_number = int(input('Enter the DVD number: '))
        except ValueError:
            print('Invalid! Please enter the proper Number')
            print('Ending process..')
            quit()

        for dvd in self.educationalDVD_list:
            if dvd.dvd_number == dvd_number and dvd.number_of_copies > 0:
                print(f'The DVD with DVD number {dvd_number} with title {dvd.title} is available to be lent')
                dvd.number_of_copies -= 1
        if dvd.dvd_number != dvd_number and dvd.number_of_copies <= 0:
            print('Sorry the DVD is unavailable')

    def resource_received(self):
        try:
            dvd_number = int(input('Enter the DVD number: '))
        except ValueError:
            print('Invalid! Please enter the proper Number')
            print('Ending process..')
            quit()

        for dvd in self.educationalDVD_list:
            if dvd.dvd_number == dvd_number:
                print(f'The DVD details are successfully updated')
                dvd.number_of_copies += 1
