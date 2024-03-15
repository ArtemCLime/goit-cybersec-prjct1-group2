from addressbook import AddressBook
from addressbook.records import Record
from bot.bot_errors import *

from rich.console import Console
from rich.markdown import Markdown

class Bot:
    def __init__(self, book_file_path) -> None:
        self.book = AddressBook()
        self.book_file_path = book_file_path 

        self.COMAND_MAPPING = {
            "add": self.add_contact,
            "add-field": self.add_field,
            "change": self.update_contact,
            "phone": self.show_phone,
            "all": self.show_all_contacts,
            "add-birthday": self.add_birthday,
            "show-birthday": self.show_birthday,
            "save": self.book_save,
            "load": self.load_book,
            "help": self.show_help
        }

    def require_args(n_args):
        def decorator(func):
            def wrapper(self, args, *args_passed, **kwargs_passed):
                if len(args) != n_args:
                    return f"You need to provide exactly {n_args} argument(s) to {func.__name__}."
                return func(self, args, *args_passed, **kwargs_passed)
            return wrapper
        return decorator

    @error_handler
    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

    def __load_book(self):
        self.book.load_from_file(self.book_file_path)

    def __save_book(self):
        self.book.save_to_file(self.book_file_path)

    @error_handler
    @require_args(2)  
    def add_contact(self, args):
        name = args[0]
        # Combine the remaining elements in args to form the phone number
        phone = ' '.join(args[1:])
        print(name, phone)
        record = Record(name)
        record.add("phone", phone)
        self.book.add(record)
        return "Contact added."
        
    @error_handler
    @require_args(3)
    def add_field(self, args):
        name, field_type, value = args
        record = self.book.read(name)
        if record:
            res = record.add(field_type, value)
            return "Field added." if not res else res
        else:
            raise BotContactNotExistsException

    def hello(self):
        return "How can I help you?"

    @error_handler
    @require_args(4)
    def update_contact(self, args):
        name, field_type, old_value, new_value = args
        record = self.book.read(name)
        if record:
            res = record.update(field_type, old_value, new_value)
            return "Contact updated." if not res else res
        else:
            raise BotContactNotExistsException
    

    @error_handler
    @require_args(1)
    def show_phone(self, args):
        name = args[0]
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

    @error_handler
    @require_args(2)
    def add_birthday(self, args):
        name, birthday = args
        record = self.book.read(name)
        if record:
            res = record.add("birthday", birthday)
            return "Birthday added." if not res else res
        else:
            raise BotContactNotExistsException
        
    @error_handler
    @require_args(1)
    def show_birthday(self, args):
        name = args[0]
        record = self.book.read(name)
        if record:
            return record.read("birthday")
        else:
            raise BotContactNotExistsException

    @error_handler
    def book_save(self):
        self.__save_book()
        return "Book saved."

    @error_handler
    def load_book(self):
        self.__load_book()
        return "Book loaded."
    
    def show_help(self):
        MARKDOWN = """
# Manual for Bot Assistans
"""
        console = Console()
        md = Markdown(MARKDOWN)
        console.print(md)

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
            elif command in self.COMAND_MAPPING:
                if args:
                    print(self.COMAND_MAPPING[command](args))
                else:
                    print(self.COMAND_MAPPING[command]())
            else:
                print("Invalid command.")
