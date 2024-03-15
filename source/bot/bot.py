from addressbook import AddressBook
from addressbook.records import Record
from bot.bot_errors import *
from notebook import NoteBook
from bot.utils import MARKDOWN
import os
from search.search import search


from rich.console import Console
from rich.markdown import Markdown


class Bot:
    """
    The main class. All operation and infinity loop placed here.
    Read the README.md for information about supported commands.
    """

    def __init__(self, folder: str) -> None:
        self.book = AddressBook()
        self.notebook = NoteBook()

        self.address_book_path = f"{folder}/address_book.json"
        self.note_book_path = f"{folder}/notebook.json"

        self.COMAND_MAPPING = {
            "add": self.add_contact,
            "add-field": self.add_field,
            "change": self.update_contact,
            "phone": self.show_phone,
            "all": self.show_all_contacts,
            "show-birthday": self.show_birthday,
            "save": self.book_save,
            "load": self.load_book,
            "help": self.show_help,
            "add-note": self.add_note,
            "edit-note": self.edit_note,
            "search-note": self.search_note,
            "delete-note": self.delete_note,
            "add-note-tags": self.add_note_tags,
            "remove-note-tags": self.remove_note_tags,
            "show-note": self.show_note,
            "search": self.search_by_field,
        }

        self.__load_book()

    def require_args(n_args):
        """Function for validation incomming parameters"""

        def decorator(func):
            def wrapper(self, args, *args_passed, **kwargs_passed):
                if len(args) != n_args:
                    return f"You need to provide exactly {n_args} argument(s) to {func.__name__}."
                return func(self, args, *args_passed, **kwargs_passed)

            return wrapper

        return decorator

    @error_handler
    def parse_input(self, user_input):
        """Parsing user input"""
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

    def __load_book(self):
        """
        Private function.
        Load address book from local storage
        """
        if os.path.exists(self.address_book_path):
            self.book.load_from_file(self.address_book_path)
        if os.path.exists(self.note_book_path):
            self.notebook.load_from_file(self.note_book_path)

    def __save_book(self):
        """
        Private function
        Save address book to the local storage
        """
        self.book.save_to_file(self.address_book_path)
        self.notebook.save_to_file(self.note_book_path)

    @error_handler
    @require_args(2)
    def add_contact(self, args):
        """Add new contact"""
        name = args[0]
        # Combine the remaining elements in args to form the phone number
        phone = " ".join(args[1:])
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
        """Show phones of the contact"""
        name = args[0]
        record = self.book.read(name)
        if record:
            return record.read("phone")
        else:
            raise BotContactNotExistsException

    @error_handler
    def show_all_contacts(self):
        """Show all contacts and with all information"""
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
        """Show birthday of the contact"""
        name = args[0]
        record = self.book.read(name)
        if record:
            return record.read("birthday")
        else:
            raise BotContactNotExistsException

    @error_handler
    @require_args(2)
    def search_by_field(self, args):
        field_type, field_value = args
        record = self.book.search_by_field(field_type, field_value)
        if record:
            return str(record)
        else:
            raise BotContactNotExistsException

    @error_handler
    def book_save(self):
        """Save address book to the storage"""
        self.__save_book()
        return "Book saved."

    @error_handler
    def load_book(self):
        """Load address book from the storage"""
        self.__load_book()
        return "Book loaded."

    def show_help(self):
        """Show help information"""
        console = Console()
        md = Markdown(MARKDOWN)
        console.print(md)

    @error_handler
    @require_args(1)
    def add_note(self, args):
        """Add note to the notebook"""
        title = args[0]
        note = input("Enter new note: ")
        self.notebook.add(title, note)
        return "Note added."

    @error_handler
    @require_args(1)
    def edit_note(self, args):
        """Edit note in the notebook"""
        title = args[0]
        old_note = self.notebook.read(title)
        if not old_note:
            raise BotNoteNotExistsException
        print(f"Old note: {old_note}")
        new_note = input("Enter new note: ")
        self.notebook.update(title, new_note)
        return "Note updated."

    @error_handler
    def search_note(self, args):
        """Search note in the notebook"""
        if args[0] == "tags:":
            return self.notebook.search_by_tags(args[1:])
        query = " ".join(args)
        return self.notebook.search_by_text(query)

    @error_handler
    @require_args(1)
    def delete_note(self, args):
        """Delete note from the notebook"""
        title = args[0]
        self.notebook.delete(title)
        return "Note deleted."

    @error_handler
    def add_note_tags(self, args):
        """Add tags to the note"""
        title = args[0]
        tags = args[1:]
        for tag in tags:
            self.notebook.add_tag(title, tag)
        return "Tags added."

    @error_handler
    def remove_note_tags(self, args):
        """Remove tags from the note"""
        title = args[0]
        tags = args[1:]
        for tag in tags:
            self.notebook.remove_tag(title, tag)
        return "Tags removed."

    @error_handler
    @require_args(1)
    def show_note(self, args):
        """Show note from the notebook"""
        title = args[0]
        note = self.notebook.read(title)
        if note:
            return note
        else:
            raise BotNoteNotExistsException

    def wrong_input(self, command):
        """Searches for closest match to the input"""
        match = search(command, self.COMAND_MAPPING.keys(), top_n=1)
        if match:
            return f"Invalid command. Did you mean '{match[0]}'?"

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
                print(self.wrong_input(command))
