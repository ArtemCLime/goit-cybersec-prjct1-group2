from addressbook import AddressBook
from addressbook.records.record import Record
from datetime import datetime
from collections import defaultdict


class Bot:
    def __init__(self) -> None:
        self.book = AddressBook()
        pass

    def idle(self) -> None:
        while True:
            print("This is your address book. Here are the commands you can use:"
                  " \n<add contact>\n<show address book>\n<update contact>"
                  "\n<delete contact>\n<find contact>\n<birthdays>\n<close>")
            command = input('Enter your command:')
            if command == 'close':
                print("Good bye!")
                break

            elif command == 'add contact':
                typed_name = input('Enter contact name:')
                typed_phone = input('Enter phone:')
                new_record = Record(typed_name, typed_phone)
                self.book.add(typed_name, new_record)

            elif command == 'show address book':
                for record in self.book.data:
                    print(record)

            elif command == 'find contact':
                contact_to_find = input('name of contact you want to find')
                self.book.read(contact_to_find)

            elif command == 'update contact':
                contact_to_update = input('Enter name of the contact you want to update:')
                if self.book.data.get(contact_to_update, 'No such contact was found') == 'No such contact was found':
                    continue
                else:
                    print(self.book.data.get(contact_to_update, 'No such contact was found'))
                    self.book.change(contact_to_update)
            elif command == 'delete contact':
                contact_to_delete = input('Enter name of the contact you want to delete:')
                if self.book.data.get(contact_to_delete, 'No such contact was found') == 'No such contact was found':
                    continue
                else:
                    confirm = input(f'Are you sure you want to delete {self.book.data[contact_to_delete].name}?\nyes/no\n')
                    if confirm == 'yes':
                        self.book.delete(contact_to_delete)
                    else:
                        continue

            elif command == 'birthdays':
                # function needs nothing but instance of AddressBook
                # I also suggest moving it somewhere else
                weekdays_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
                now = datetime.today().date()
                people_to_congratulate = defaultdict(list)
                for contact in self.book:
                    birthday = datetime.strptime(self.book[contact].birthday, '%d.%m.%Y')
                    next_birthday = datetime(
                        year=now.year,
                        month=birthday.month,
                        day=birthday.day).date()
                    if next_birthday < now:
                        next_birthday.replace(year=now.year + 1)
                    delta_days = (next_birthday - now).days
                    if 7 >= delta_days >= 0:
                        weekday = next_birthday.isoweekday()
                        if weekday == 6 or weekday == 7:
                            weekday = 1
                        people_to_congratulate[weekday].append(contact)
                for i in range(1, 6):
                    if people_to_congratulate.get(i) is not None:
                        names = ", ".join(people_to_congratulate[i])
                        print(f'{weekdays_list[i - 1]}: {names}')
