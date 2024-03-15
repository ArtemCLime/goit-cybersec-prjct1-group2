from addressbook.records import Record
import json
from collections import UserDict
from typing import Union
from search.search import search
from bot.bot_errors import *


class AddressBook(UserDict):
    """
    Class for AddressBook in the address book.

    Attributes:
        self.data: Dict[str, Record] : The data of the address book

    """

    def __str__(self):
        return f"{self.data}"

    def to_json(self):
        """Return a JSON representation of the address book."""
        return {key: value.to_json() for key, value in self.data.items()}

    def from_json(self, data: Union[str, dict]):
        """Load the address book from a JSON representation."""
        self.data = {name: Record.from_json(record) for name, record in data.items()}

    # CRUD operations, Create, Read, Update, Delete.

    def add(self, record: Record):
        """Add a record to the address book."""
        self.data[record.name.value] = record

    def read(self, name: str):
        """Read a record from the address book."""
        return self.data[name]

    def update(self, name: str, record: Record):
        """Update a record in the address book."""
        self.data[name] = record

    def delete(self, name: str):
        """Delete a record from the address book."""
        del self.data[name]

    def save_to_file(self, filename: str):
        """Save the address book to a file."""
        with open(filename, "w") as file:
            json.dump(self.to_json(), file)

    def load_from_file(self, filename: str):
        """Load the address book from a file."""
        with open(filename, "r") as file:
            data = json.load(file)
            self.from_json(data)

    def search_by_field(self, field_name: str, field_value: str):
        if field_name == "name":
            return self.search_by_name(field_value)
        elif field_name == "phone":
            return self.search_by_phone(field_value)
        elif field_name == "email":
            return self.search_by_email(field_value)

    def search_by_name(self, name: str):
        """Search for a name in the address book."""
        try:
            contact = self.data.get(name)
            if contact != None:
                return contact
            else:
                raise BotRecordNotFoundException
        except Exception:
            raise BotContactSearchByNameException

    def search_by_phone(self, phone: str):
        """Search for a phone in the address book."""
        try:
            for key in self.data.keys():
                for p in self.data[key].phones:
                    if p.value == phone:
                        return self.data[key]
                raise BotRecordNotFoundException
        except Exception:
            raise BotContactSearchByPhoneException

    def search_by_email(self, email: str):
        """Search for an email in the address book."""
        try:
            for key in self.data.keys():
                for e in self.data[key].emails:
                    if e.value == email:
                        return self.data[key]
                raise BotRecordNotFoundException
        except Exception:
            raise BotContactSearchByEmailException
