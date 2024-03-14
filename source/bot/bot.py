from addressbook import AddressBook
from addressbook.records import Record
from bot.bot_errors import *

class Bot:
    def __init__(self, book_file_path) -> None:
        self.book = AddressBook()
        self.book_file_path = book_file_path 

    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

    def __load_book(self):
        pass

    def __save_book(self):
        pass

    @error_handler    
    def add_contact(self, args):
        if len(args) >= 2:
            name = args[0]
            # Combine the remaining elements in args to form the phone number
            phone = ' '.join(args[1:])
            record = Record(name)
            res = record.add("phone", phone)
            if res:
                return res
            self.book.add(record)
            return "Contact added."
        else:
            raise BotContactAddException

    def hello(self):
        return "How can I help you?"

    @error_handler
    def update_contact(self, name, old_phone, new_phone):
        record = self.book.read(name)
        if record:
            res = record.update("phone", old_phone, new_phone)
            return "Contact updated." if not res else res
        else:
            raise BotContactNotExistsException

    @error_handler
    def show_phone(self, name):
        record = self.book.read(name)
        if record:
            return record.read('phone')
        else:
            raise BotContactNotExistsException

    @error_handler
    def show_all_contacts(self):
        if self.book.data:
            return "\n".join([str(record) for record in self.book.data.values()])
        else:
            raise BotContactsNotAvailableException

    def add_birthday(self, book, name, birthday):
        record = book.read(name)
        if record:
            res = record.add("birthday", birthday)
            return "Birthday added." if not res else res
        else:
            raise BotContactNotExistsException
        
    @error_handler
    def show_birthday(self, name):
        record = self.book.read(name)
        if record:
            return record.read("birthday")
        else:
            raise BotContactNotExistsException

    @error_handler
    def book_save(self):
        self.__save_book()

#    @input_error
#    def print_birthdays_per_week(self, book):
#        users = [{"name": name, "birthday": record.show_birthday()} for name, record in book.data.items()]
#        return get_birthdays_per_week(users)

    def idle(self) -> None:
        print("Welcome to the personal assistant bot!")
        while True:
            user_input = input("Enter a command: ")
            command, *args = self.parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print(self.hello())
            elif command == "add" and len(args) >= 2:
                print(self.add_contact(args, self.book))
            elif command == "change" and len(args) == 2:
                print(self.update_contact(self.book, args[0], args[1]))
            elif command == "phone" and len(args) == 1:
                print(self.show_phone(self.book, args[0]))
            elif command == "all" and not args:
                print(self.show_all_contacts(self.book))
            elif command == "add-birthday" and len(args) == 2:
                print(self.add_birthday(self.book, args[0], args[1]))
            elif command == "show-birthday" and len(args) == 1:
                print(self.show_birthday(self.book, args[0]))
            ##elif command == "birthdays" and not args:
            ##    results = print_birthdays_per_week(book)
            elif command == "save" and not args:
                print(self.book_save)
            else:
                print("Invalid command.")
            pass
