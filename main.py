from FunctionsOfBooks import BookFunctions
from FunctionsOfMagazines import MagazineFunctions
from FunctionsOfEducationalDVDs import EducationalDvdFunctions
from FunctionsOfLectureCDs import LectureCDFunctions

bookTask = BookFunctions()
magazineTask = MagazineFunctions()
educationalDVDTask = EducationalDvdFunctions()
lectureCDTask = LectureCDFunctions()


def select_type_of_resource():
    print('Select a Resource Menu')
    print('----------------------')
    print('1.Book')
    print('2.Magazine')
    print('3.Educational DVD')
    print('4.Lecture CD')
    print('5.Search by Subject(Any type)')
    print('9.Exit the system')
    print('')


def select_operation():
    print('Select an Action Menu')
    print('----------------------')
    print('1.Add a new resource')
    print('2.Remove a resource')
    print('3.View the availability of resources')
    print('4.View the unavailability of resource')
    print('5.Lend a resource')
    print('6.Update the resource received')
    print('7.Go back to the resource menu')
    print('9.Exit the system')
    print('')


def main_function():
    task = None
    type_of_resource = 0
    operation = 0

    select_type_of_resource()
    try:
        type_of_resource = int(input('Please select the resource type you want: '))
        # Related to resource
        if type_of_resource == 1:
            task = bookTask
        elif type_of_resource == 2:
            task = magazineTask
        elif type_of_resource == 3:
            task = educationalDVDTask
        elif type_of_resource == 4:
            task = lectureCDTask
        elif type_of_resource == 5:
            resource_subject = input('Enter the subject: ')
            case1 = bookTask.search_by_subject(subject=resource_subject)
            case2 = magazineTask.search_by_subject(subject=resource_subject)
            case3 = educationalDVDTask.search_by_subject(subject=resource_subject)
            case4 = lectureCDTask.search_by_subject(subject=resource_subject)
            main_function()
        elif type_of_resource == 9:
            print('Quiting....')
            quit()

        while 0 <= operation < 9:
            try:
                select_operation()
                operation = int(input('Please select the operation you want to perform: '))
                # Related to operations
                if operation == 1:
                    task.add()
                elif operation == 2:
                    task.remove()
                elif operation == 3:
                    task.currently_available()
                elif operation == 4:
                    task.currently_unavailable()
                elif operation == 5:
                    task.lend()
                elif operation == 6:
                    task.resource_received()
                elif operation == 7:
                    main_function()
                elif operation == 9:
                    print('Quiting....')
                    quit()
                else:
                    print('Sorry! Seems like something went wrong')
                    quit()
                print('')
                pause = input('Press enter to continue...')
            except ValueError:
                print('Invalid! Please enter the number corresponding to the operation')
                quit()
    except ValueError:
        print('Invalid! Please enter the number corresponding to the resource')
        quit()


# first view
print('Welcome to the University Library')
print('')
count = 0
while count >= 0:
    print('')
    count = count + 1
    main_function()
