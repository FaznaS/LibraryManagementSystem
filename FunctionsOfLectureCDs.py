from lectureCD import LectureCD


class LectureCDFunctions:
    def __init__(self):
        self.LectureCD_list = []
        self.lecture_cds_present_initially()

    # view books already present
    def lecture_cds_present_initially(self):
        cd1 = LectureCD(cd_number=21, title='Basics of Western Music', subject='Music',
                        rental_price_per_day=1.50, number_of_copies=11)
        cd2 = LectureCD(cd_number=22, title='Japanese Language', subject='Foreign Languages',
                        rental_price_per_day=2.00, number_of_copies=3)

        self.LectureCD_list.append(cd1)
        self.LectureCD_list.append(cd2)

    def add(self):
        print('Enter the details of the LectureCDs to be added')
        try:
            cd_number = int(input('Enter the Lecture CD number: '))
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

        new_cd = LectureCD(cd_number, title, subject, rental_price_per_day, number_of_copies)

        self.LectureCD_list.append(new_cd)
        print('The Lecture CD was successfully added to the library')

    def remove(self):
        try:
            cd_number = int(input("Enter the Lecture CD number of the CD you want to remove: "))
        except ValueError:
            print('Invalid! Please enter the proper Number')
            print('Ending process..')
            quit()

        for cd in self.LectureCD_list:
            if cd.cd_number == cd_number:
                self.LectureCD_list.remove(cd)
                print('The CD was successfully removed from the library')

    # To view currently available books
    def currently_available(self):
        # iterating inside the list to check the availability
        available_sub = False
        for cd in self.LectureCD_list:
            if cd.number_of_copies > 0:
                available_sub = True
                print(f'The Lecture CD with CD number {cd.cd_number} and title {cd.title} is available')
        if not available_sub:
            print('Sorry the Lecture CD is not available')

    # To view currently unavailable books
    def currently_unavailable(self):
        # iterating inside the list to check the unavailability
        available_sub = False
        for cd in self.LectureCD_list:
            if cd.number_of_copies <= 0:
                available_sub = True
                print(f'Sorry.The educational DVD with DVD number {cd.cd_number} and '
                      f'title {cd.title} is not available')
        if not available_sub:
            print('All resources are available')

    def search_by_subject(self, subject):
        available_sub = False
        for resource in self.LectureCD_list:
            if resource.subject == subject:
                available_sub = True
                print(f'The {resource.title} CD is available')
        if not available_sub:
            print(f'Sorry {subject} CDs are currently unavailable')

    def lend(self):
        try:
            cd_number = int(input('Enter the CD number: '))
        except ValueError:
            print('Invalid! Please enter the proper Number')
            print('Ending process..')
            quit()

        for cd in self.LectureCD_list:
            if cd.cd_number == cd_number and cd.number_of_copies > 0:
                print(f'The CD with CD number {cd_number} with title {cd.title} is available to be lent')
                cd.number_of_copies -= 1
        if cd.cd_number != cd_number and cd.number_of_copies <= 0:
            print('Sorry the CD is unavailable')

    def resource_received(self):
        try:
            cd_number = int(input('Enter the CD number: '))
        except ValueError:
            print('Invalid! Please enter the proper Number')
            print('Ending process..')
            quit()

        for cd in self.LectureCD_list:
            if cd.cd_number == cd_number:
                print(f'The CD details are successfully updated')
                cd.number_of_copies += 1
