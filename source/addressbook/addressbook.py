from addressbook.records import Record
import json
from collections import UserDict
from typing import Union


class AddressBook:
    """
        Class for AddressBook in the address book.

        Attributes:
            self.data: Dict[str, Record] : The data of the address book

    """
    def __str__(self):
        return f'{self.records}'

    def to_json(self):
        """ Return a JSON representation of the address book. """
        return {key: value.to_json() for key, value in self.records.items()}
    
    def from_json(self, data: Union[str, dict]):
        """ Load the address book from a JSON representation. """
        self.data = {name: Record.from_json(record) for name, record in data.items()}

    # CRUD operations, Create, Read, Update, Delete.

    def add(self, record: Record):
        """ Add a record to the address book. """
        pass
        # TODO: Implement the add method.

    def read(self, name: str):
        """ Read a record from the address book. """
        pass
        # TODO: Implement the read method.
    
    def update(self, name: str, record: Record):
        """ Update a record in the address book. """
        pass
        # TODO: Implement the update method.
    
    def delete(self, name: str):
        """ Delete a record from the address book. """
        pass
        # TODO: Implement the delete method.
    

    def save_to_file(self, filename: str):
        """ Save the address book to a file. """
        with open(filename, 'w') as file:
            json.dump(self.to_json(), file)

    def load_from_file(self, filename: str):
        """ Load the address book from a file. """
        with open(filename, 'r') as file:
            data = json.load(file)
            self.from_json(data)

    