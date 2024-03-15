from addressbook import AddressBook
from addressbook.records import Record
from bot.bot_errors import *

from rich.console import Console
from rich.markdown import Markdown

class Bot:
    """
    The main class. All operation and infinity loop placed here.
    Read the README.md for information about supported commands.
    """
    def __init__(self, book_file_path) -> None:
        self.book = AddressBook()
        self.book_file_path = book_file_path 

        self.COMAND_MAPPING = {
            "add": self.add_contact,
            "add-field": self.add_field,
            "change": self.update_contact,
            "phone": self.show_phone,
            "all": self.show_all_contacts,
            #"add-birthday": self.add_birthday,
            "show-birthday": self.show_birthday,
            "save": self.book_save,
            "load": self.load_book,
            "help": self.show_help
        }
        #TODO: autoload the address book if exists
        #self.__load_book()

    def require_args(n_args):
        """ Function for validation incomming parameters """
        def decorator(func):
            def wrapper(self, args, *args_passed, **kwargs_passed):
                if len(args) != n_args:
                    return f"You need to provide exactly {n_args} argument(s) to {func.__name__}."
                return func(self, args, *args_passed, **kwargs_passed)
            return wrapper
        return decorator

    @error_handler
    def parse_input(self, user_input):
        """ Parsing user input """
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

    def __load_book(self):
        """
        Private function.
        Load address book from local storage
        """
        self.book.load_from_file(self.book_file_path)

    def __save_book(self):
        """
        Private function
        Save address book to the local storage
        """
        self.book.save_to_file(self.book_file_path)

    @error_handler
    @require_args(2)  
    def add_contact(self, args):
        """ Add new contact """
        name = args[0]
        # Combine the remaining elements in args to form the phone number
        phone = ' '.join(args[1:])
        print(name, phone)
        record = Record(name)
        res = record.add("phone", phone)
        if res:
            return res
        self.book.add(record)
        return "Contact added."
        
    @error_handler
    @require_args(3)
    def add_field(self, args):
        """ 
        Add field to the contact 
        field type
            - phone
            - email
            - birthday
            - address
        """
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
        """ 
        Update field in the contact 
        field type
            - phone
            - email
            - birthday
            - address
        """
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
        """ Show phones of the contact """
        name = args[0]
        record = self.book.read(name)
        if record:
            return record.read('phone')
        else:
            raise BotContactNotExistsException

    @error_handler
    def show_all_contacts(self):
        """ Show all contacts and with all information """
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
        """ Show birthday of the contact """
        name = args[0]
        record = self.book.read(name)
        if record:
            return record.read("birthday")
        else:
            raise BotContactNotExistsException

    @error_handler
    def book_save(self):
        """ Save address book to the storage """
        self.__save_book()
        return "Book saved."

    @error_handler
    def load_book(self):
        """ Load address book from the storage """
        self.__load_book()
        return "Book loaded."
    
    def show_help(self):
        """ Show help information """
        MARKDOWN = """
# Manual for Bot Assistant

Assistant bot help keep contact information in one place.  
Each contact can have multiple email and phone records.

## The next command are supported

* add [name] [phone] - Create the new record in address book
* add-field [name] [field-type] [value] - add field to the record
* change [name] [field-type] [old_value] [new_value] - change field value
* phone [name] - show all phones for given contact name
* all - show all contacts in the Address Book
* show-birthday [name] - show contact birtday
* save - save address book to the local file
* load - load address book from the local file
* help - print this help

### field-type one of the next

* phone - the phone number. min 10 digit
* email - the email
* birthday - birthday date in format dd.mm.yyyy
* address - the address
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
