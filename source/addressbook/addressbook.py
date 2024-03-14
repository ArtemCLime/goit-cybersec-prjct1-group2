from addressbook.records import Record
import json
from collections import UserDict
from typing import Union
from search.search import search


class AddressBook(UserDict):
    """
        Class for AddressBook in the address book.

        Attributes:
            self.data: Dict[str, Record] : The data of the address book

    """
    def __str__(self):
        return f'{self.data}'

    def to_json(self):
        """ Return a JSON representation of the address book. """
        return {key: value.to_json() for key, value in self.data.items()}
    
    def from_json(self, data: Union[str, dict]):
        """ Load the address book from a JSON representation. """
        self.data = {name: Record.from_json(record) for name, record in data.items()}

    # CRUD operations, Create, Read, Update, Delete.

    def add(self, record: Record):
        """ Add a record to the address book. """
        self.data[record.name.value] = record

    def read(self, name: str):
        """ Read a record from the address book. """
        return self.data[name]
    
    def update(self, name: str, record: Record):
        """ Update a record in the address book. """
        self.data[name] = record
    
    def delete(self, name: str):
        """ Delete a record from the address book. """
        del self.data[name]
    

    def save_to_file(self, filename: str):
        """ Save the address book to a file. """
        with open(filename, 'w') as file:
            json.dump(self.to_json(), file)

    def load_from_file(self, filename: str):
        """ Load the address book from a file. """
        with open(filename, 'r') as file:
            data = json.load(file)
            self.from_json(data)

    def search_by_name(self, name: str):
        """ Search for a name in the address book. """
        return search(name, [record.name.value for record in self.data.values()], top_n=3)
    
    def search_by_phone(self, phone: str):
        """ Search for a phone in the address book. """
        return search(phone, [phone.value for record in self.data.values() for phone in record.phones], top_n=3)
    
    def search_by_email(self, email: str):
        """ Search for an email in the address book. """
        return search(email, [email.value for record in self.data.values() for email in record.emails], top_n=3)

    