from addressbook.records import Record
from collections import UserDict

class AddressBook(UserDict):
    """
        Class for AddressBook in the address book.

        Attributes:
            records: List[Record], The list of records in the address book.

    """


    def __str__(self):
        return f'{self.data}'

    def to_json(self):
        """ Return a JSON representation of the address book. """
        pass

    # CRUD operations, Create, Read, Update, Delete.

    def add(self, name: str, record: Record):
        """ Add a record to the address book. """
        pass
        # TODO: Implement the add method.

    def read(self, name: str):
        """ Read a record from the address book."""
        pass
        # TODO: Implement the read method.

    def change(self, name: str):
        """ Update a record in the address book. """
        pass
        # TODO: Implement the update method.

    def delete(self, name: str):
        """ Delete a record from the address book. """
        pass
        # TODO: Implement the delete method.

