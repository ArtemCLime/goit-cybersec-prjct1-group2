from addressbook import AddressBook
from addressbook.records import Record

class Bot:
    def __init__(self) -> None:
        self.book = AddressBook()        

    def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (ValueError, KeyError, IndexError):
                return "Invalid input. Check your data."
            except Exception as e:
                return f"An error occurred: {str(e)}"

        return inner

    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

    @input_error    
    def add_contact(self, args, book):
        if len(args) >= 2:
            name = args[0]
            # Combine the remaining elements in args to form the phone number
            phone = ' '.join(args[1:])
            record = Record(name)
            record.add("phone", phone)
            book.add(record)
            return "Contact added."
        else:
            return "Invalid command. Please provide both name and phone number."

    def hello(self):
        return "How can I help you?"

    @input_error
    def update_contact(self, book, name, new_phone):
        record = book.read(name)
        if record:
            record.update("phone", new_phone)
            return "Contact updated."
        else:
            return "Contact not found."

    @input_error
    def show_phone(self, book, name):
        record = book.read(name)
        return record.phones[0].value if record else "Contact not found."

    @input_error
    def show_all_contacts(self, book):
        if book.data:
            return "\n".join([str(record) for record in book.data.values()])
        else:
            return "No contacts available."
        
    @input_error
    def add_birthday(self, book, name, birthday):
        record = book.read(name)
        if record:
            record.add("birthday", birthday)
            return "Birthday added."
        else:
            return "Contact not found."
        
    @input_error
    def show_birthday(self, book, name):
        record = book.read(name)
        return record.show_birthday() if record else "Contact not found."

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
            else:
                print("Invalid command.")
            pass
